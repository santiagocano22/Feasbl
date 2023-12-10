# Define las excepciones personalizadas
class InvalidArgumentError(RuntimeError):
    pass

class PathNotFoundError(RuntimeError):
    pass

# Define las clases y métodos necesarios para la funcionalidad
class DataValidator:
    @staticmethod
    def apply(matrix, sequences, max_path_length):
        if matrix.row_count == 0 or matrix.column_count == 0:
            raise InvalidArgumentError("Matrix must not be empty.")
        if not sequences:
            raise InvalidArgumentError("There should be at least one sequence.")
        for sequence in sequences:
            if not sequence.codes:
                raise InvalidArgumentError("All sequences should be non-empty.")
            if sequence.score <= 0:
                raise InvalidArgumentError("All sequences should have a score greater than zero.")
        if max_path_length <= 0:
            raise InvalidArgumentError("Maximum path length should be greater than zero.")

class SequenceOverlapping:
    @staticmethod
    def apply(sequences):
        if len(sequences) == 1:
            return sequences
        
        if len(sequences) > 2:
            for i in range(len(sequences) - 1):
                for j in range(1, len(sequences)):
                    sequences_to_combine = [sequences[i], sequences[j]]
                    combined_sequences = SequenceOverlapping.combining_two_sequences(sequences_to_combine)
                    if combined_sequences:
                        sequences.pop(i)
                        sequences.pop(j-1)
                        sequences.append(combined_sequences[0])
                        return SequenceOverlapping.apply(sequences)
            return sequences

        result = SequenceOverlapping.combining_two_sequences(sequences)

        if not result:
            total_score = sequences[0].score + sequences[1].score
            joined_codes1 = sequences[0].codes + sequences[1].codes
            result.append(Sequence(joined_codes1, total_score))
            joined_codes2 = sequences[1].codes + sequences[0].codes
            result.append(Sequence(joined_codes2, total_score))

        return result

    @staticmethod
    def combining_two_sequences(sequences):
        result = []
        codes_seq1 = sequences[0].codes
        codes_seq2 = sequences[1].codes
        if codes_seq1[0] in codes_seq2:
            sequence = SequenceOverlapping.overlapping_two_sequences(sequences[0], sequences[1])
            if sequence:
                result.append(sequence)
        if codes_seq2[0] in codes_seq1:
            sequence = SequenceOverlapping.overlapping_two_sequences(sequences[1], sequences[0])
            if sequence:
                result.append(sequence)
        return result

    @staticmethod
    def overlapping_two_sequences(sequence1, sequence2):
        for i in range(len(sequence1.codes)):
            if sequence1.codes[i] == sequence2.codes[0]:
                sub_list_codes_seq1 = sequence1.codes[i:]
                if len(sub_list_codes_seq1) > len(sequence2.codes):
                    shortest_sub_list_codes_seq1 = sub_list_codes_seq1[:len(sequence2.codes)]
                    if shortest_sub_list_codes_seq1 == sequence2.codes:
                        sequence1.score += sequence2.score
                        return sequence1
                else:
                    sub_list_codes_seq2 = sequence2.codes[:len(sub_list_codes_seq1)]
                    if sub_list_codes_seq1 == sub_list_codes_seq2:
                        total_codes = sequence1.codes + sequence2.codes[len(sub_list_codes_seq1):]
                        return Sequence(total_codes, sequence1.score + sequence2.score)
        return None


# ---------------------------------------------------------------------------------------------
# PLEASE DO NOT MODIFY, RENAME OR REMOVE ANY OF CLASSES, METHODS AND VARIABLES BELOW
# EXCEPT PATHFINDER.RUN() METHOD THAT YOU NEED TO IMPLEMENT.
# YOU CAN ADD YOUR OWN METHODS AND VARIABLES TO THE EXISTING CLASSES AND USE THEM IN YOUR WORK.
# ---------------------------------------------------------------------------------------------

from .invalid_argument_error import InvalidArgumentError
from .matrix import Matrix
from .path import Path
from .path_not_found_error import PathNotFoundError
from .position import Position
from .sequence import Sequence


class PathFinder:
    def __init__(self, matrix: Matrix, sequences: list[Sequence], max_path_length: int) -> None:
        self.matrix = matrix
        self.sequences = sequences
        self.max_path_length = max_path_length

    def run(self) -> Path:
        self.data_validate()
        path = Path()
        self.sequences_finder(SequenceOverlapping.apply(self.sequences), path)
        if len(path.positions) > self.max_path_length or not path.positions:
            self.separate_sequence_finder(path)
        return path

    def sequences_finder(self, sequences, path):
        for sequence in sequences:
            for start_row in range(self.matrix.row_count):
                self.find_path_for_sequence(sequence, path, start_row)
                if path.positions:
                    return sequence
        return None

    def separate_sequence_finder(self, path):
        path.positions.clear()
        self.sequences.sort(key=lambda seq: (seq.score, len(seq.codes)))

        sequence_with_solution = self.sequences_finder(self.sequences, path)

        if sequence_with_solution:
            path1 = list(path.positions)
            path.positions.clear()
            for sequence in self.sequences:
                if sequence != sequence_with_solution:
                    sequences = [sequence]
                    self.sequences_finder(sequences, path)
            if path.positions:
                path2 = list(path.positions)
                if path1[-1] != path2[0]:
                    position_connector = Position(path2[0].row, path1[-1].column)
                    if position_connector not in path1 and position_connector not in path2:
                        path.positions.clear()
                        path.positions.extend(path1)
                        path.positions.append(position_connector)
                        path.positions.extend(path2)
                        if len(path.positions) > self.max_path_length:
                            path.positions.clear()
                            path.positions.extend(path1)
            else:
                path.positions.extend(path1)

        if not path.positions:
            raise PathNotFoundError("Path not found")

    def find_path_for_sequence(self, sequence, path, row):
        codes = sequence.codes
        sequence_length = len(codes)
        code_index = 0
        col = 0
        visited_positions = {}

        while code_index < sequence_length:
            code = codes[code_index]
            if code_index % 2 == 0:
                col = self.find_col_in_row(code, self.matrix, row)
                if col != -1:
                    visited_positions[Position(row, col)] = code
                    if row > 0 and code_index == 0:
                        self.matrix.values[row][col] = code
                        self.add_wasted_move(sequence, path, col, codes)
                        break
                    path.add_position(Position(row, col))
                    code_index += 1
            else:
                row = self.find_row_in_col(code, self.matrix, col)
                if row != -1:
                    visited_positions[Position(row, col)] = code
                    path.add_position(Position(row, col))
                    code_index += 1

            if row == -1 or col == -1:
                path.delete_last_position()
                if not path.positions:
                    row = 0
                    col = 0
                else:
                    last_position = path.positions[-1]
                    row = last_position.row
                    col = last_position.column
                code_index -= 1

            if code_index < 0:
                break

        for position, saved_code in visited_positions.items():
            self.matrix.values[position.row][position.column] = saved_code

    def add_wasted_move(self, sequence, path, col, codes):
        new_sequence = [self.matrix.value(0, col)] + codes
        self.find_path_for_sequence(Sequence(new_sequence, sequence.score), path, 0)

    def find_col_in_row(self, code, matrix, row):
        for col in range(matrix.column_count):
            if matrix.value(row, col) == code:
                matrix.values[row][col] = -1
                return col
        return -1

    def find_row_in_col(self, code, matrix, col):
        for row in range(matrix.row_count):
            if matrix.value(row, col) == code:
                matrix.values[row][col] = -1
                return row
        return -1

    def data_validate(self):
        DataValidator.apply(self.matrix, self.sequences, self.max_path_length)
