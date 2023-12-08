# ---------------------------------------------------------------------------------------------
# THIS IS A TESTING PROJECT. YOU CAN FREELY MODIFY THE CODE BELOW IN ORDER TO TEST YOUR WORK.
# ---------------------------------------------------------------------------------------------

from ..solver.invalid_argument_error import InvalidArgumentError
from ..solver.matrix import Matrix
from ..solver.path import Path
from ..solver.path_finder import PathFinder
from ..solver.path_not_found_error import PathNotFoundError
from ..solver.position import Position
from ..solver.sequence import Sequence


class Application:
    def run(self) -> None:
        self.run_example_1()
        self.run_example_2()
        self.run_example_3()
        self.run_example_4()
        self.run_example_5()
        self.run_example_6()
        self.run_example_7()
        self.run_example_8()

        # NOTE: Uncomment this example only if you have developed fast algorithm that can handle large matrices and paths.
        # self.run_example_9()

    def run_example_1(self) -> None:
        matrix = Matrix(
            [
                [0x3A, 0x3A, 0x10, 0x9B, 0x72],
                [0x9B, 0x72, 0x3A, 0x10, 0x72],
                [0x10, 0x3A, 0x3A, 0x3A, 0x10],
                [0x3A, 0x10, 0x3A, 0x9B, 0x72],
                [0x10, 0x10, 0x3A, 0x72, 0x72],
            ]
        )

        sequences = [Sequence([0x3A, 0x10, 0x9B], 10)]

        max_path_length = 3

        positions = [(0, 1), (3, 1), (3, 3)]
        expected_solution = Path([Position(row, column) for row, column in positions])

        self.run_example(
            "example of a simple puzzle with one sequence",
            matrix,
            sequences,
            max_path_length,
            expected_solution,
        )

    def run_example_2(self) -> None:
        matrix = Matrix(
            [
                [0x3A, 0x3A, 0x10, 0x9B, 0x72],
                [0x9B, 0x72, 0x3A, 0x10, 0x72],
                [0x10, 0x3A, 0x3A, 0x3A, 0x10],
                [0x3A, 0x10, 0x3A, 0x9B, 0x72],
                [0x10, 0x10, 0x3A, 0x72, 0x72],
            ]
        )

        sequences = [Sequence([0x9B, 0x3A], 20), Sequence([0x10, 0x10, 0x3A], 30)]

        max_path_length = 5

        positions = [(0, 3), (2, 3), (2, 0), (4, 0), (4, 2)]
        expected_solution = Path([Position(row, column) for row, column in positions])

        self.run_example(
            "example of a puzzle with two sequences",
            matrix,
            sequences,
            max_path_length,
            expected_solution,
        )

    def run_example_3(self) -> None:
        matrix = Matrix(
            [
                [0x9B, 0x9B, 0x72, 0x9B, 0xD4],
                [0x10, 0xD4, 0xD4, 0x9B, 0x10],
                [0x72, 0x9B, 0x3A, 0x10, 0x9B],
                [0x3A, 0xD4, 0x9B, 0x3A, 0x9B],
                [0x72, 0x10, 0x10, 0xD4, 0x10],
            ]
        )

        sequences = [
            Sequence([0x10, 0xD4, 0x72, 0x72], 20),
            Sequence([0x3A, 0x10, 0xD4], 10),
        ]

        max_path_length = 7

        positions = [(0, 2), (2, 2), (2, 3), (4, 3), (4, 0), (2, 0)]
        expected_solution = Path([Position(row, column) for row, column in positions])

        self.run_example(
            "example of a puzzle with one wasted move",
            matrix,
            sequences,
            max_path_length,
            expected_solution,
        )

    def run_example_4(self) -> None:
        matrix = Matrix(
            [
                [0x10, 0x10, 0x10, 0x10, 0x10],
                [0x10, 0x10, 0x10, 0x10, 0x10],
                [0x3A, 0xD4, 0x10, 0x9B, 0x72],
                [0x10, 0x10, 0x10, 0x10, 0x10],
                [0x10, 0x10, 0x10, 0x10, 0x10],
            ]
        )

        sequences = [Sequence([0x3A, 0x9B], 10), Sequence([0x72, 0xD4], 10)]

        max_path_length = 7

        # NOTE: There are multiple possible solutions. Uncomment the suitable one below.
        positions = [(0, 0), (2, 0), (2, 3), (0, 3), (0, 4), (2, 4), (2, 1)]
        # positions = [(0, 0), (2, 0), (2, 3), (1, 3), (1, 4), (2, 4), (2, 1)]
        # positions = [(0, 0), (2, 0), (2, 3), (3, 3), (3, 4), (2, 4), (2, 1)]
        # positions = [(0, 0), (2, 0), (2, 3), (4, 3), (4, 4), (2, 4), (2, 1)]
        # positions = [(0, 4), (2, 4), (2, 1), (0, 1), (0, 0), (2, 0), (2, 3)]
        # positions = [(0, 4), (2, 4), (2, 1), (1, 1), (1, 0), (2, 0), (2, 3)]
        # positions = [(0, 4), (2, 4), (2, 1), (3, 1), (3, 0), (2, 0), (2, 3)]
        # positions = [(0, 4), (2, 4), (2, 1), (4, 1), (4, 0), (2, 0), (2, 3)]
        expected_solution = Path([Position(row, column) for row, column in positions])

        self.run_example(
            "example of a puzzle with three wasted moves",
            matrix,
            sequences,
            max_path_length,
            expected_solution,
        )

    def run_example_5(self) -> None:
        matrix = Matrix(
            [
                [0x9B, 0x10, 0x72, 0x10, 0x10],
                [0x10, 0x3A, 0x3A, 0x3A, 0x10],
                [0x72, 0xD4, 0x10, 0x10, 0x9B],
                [0x3A, 0x72, 0xD4, 0x3A, 0x9B],
                [0x72, 0x10, 0x10, 0x10, 0x10],
            ]
        )

        sequences = [
            Sequence([0x9B, 0x3A, 0x72, 0xD4], 20),
            Sequence([0x72, 0xD4, 0x3A], 10),
        ]

        max_path_length = 5

        positions = [(0, 0), (3, 0), (3, 1), (2, 1)]
        expected_solution = Path([Position(row, column) for row, column in positions])

        self.run_example(
            "example of a puzzle with competing sequences",
            matrix,
            sequences,
            max_path_length,
            expected_solution,
        )

    def run_example_6(self) -> None:
        matrix = Matrix(
            [
                [0x9B, 0x3A, 0x3A, 0x9B],
                [0x10, 0x3A, 0x3A, 0x10],
                [0x3A, 0x3A, 0x72, 0x9B],
            ]
        )

        sequences = [Sequence([0x3A, 0xD4], 10), Sequence([0x72, 0x10], 10)]

        max_path_length = 6

        self.run_example_without_solution(
            "example of a puzzle without any solution",
            matrix,
            sequences,
            max_path_length,
        )

    def run_example_7(self) -> None:
        matrix = Matrix(
            [
                [0x9B, 0x10, 0x72, 0x10, 0x10],
                [0x10, 0x3A, 0x3A, 0x3A, 0x10],
                [0x72, 0xD4, 0x10, 0x10, 0x9B],
                [0x3A, 0x72, 0xD4, 0x9B, 0x9B],
                [0x72, 0x10, 0x10, 0x10, 0x10],
            ]
        )

        sequences = [
            Sequence([0x9B, 0x3A, 0x72, 0xD4], 10),
            Sequence([0x72, 0xD4, 0x3A], 10),
        ]

        max_path_length = 5

        positions = [(0, 2), (3, 2), (3, 0)]
        expected_solution = Path([Position(row, column) for row, column in positions])

        self.run_example(
            "example of a puzzle with the shortest competing sequence",
            matrix,
            sequences,
            max_path_length,
            expected_solution,
        )

    def run_example_8(self) -> None:
        matrix = Matrix(
            [
                [0x3A, 0x3A, 0x10, 0x9B, 0x72],
                [0x9B, 0x72, 0x3A, 0x10, 0x72],
                [0x10, 0xD4, 0x3A, 0x3A, 0x10],
                [0x3A, 0x10, 0x3A, 0x9B, 0x72],
                [0x10, 0x10, 0x3A, 0x72, 0x72],
            ]
        )

        sequences = [
            Sequence([0x9B, 0x3A, 0xFF], 30),
            Sequence([0x3A, 0xD4, 0x9B], 30),
            Sequence([0x3A, 0x3A, 0x72], 30),
        ]

        max_path_length = 6

        positions = [(0, 0), (3, 0), (3, 4)]
        expected_solution = Path([Position(row, column) for row, column in positions])

        self.run_example(
            "example of a puzzle with one possible sequence out of three",
            matrix,
            sequences,
            max_path_length,
            expected_solution,
        )

    def run_example_9(self) -> None:
        matrix = Matrix(
            [
                [0x00, 0x10, 0xD4, 0x9B, 0x10, 0x9B, 0xD4, 0x72, 0xF0, 0x10],
                [0x9B, 0x3A, 0x9B, 0x9B, 0x72, 0xD4, 0x10, 0xD4, 0x72, 0x72],
                [0xF9, 0x3A, 0xD4, 0xD4, 0x9B, 0x3A, 0xFA, 0x10, 0x9B, 0x10],
                [0xD4, 0x3A, 0x9B, 0x3A, 0x3A, 0x72, 0x72, 0xD4, 0xF1, 0xF2],
                [0xF8, 0x10, 0x72, 0x3A, 0xF7, 0x72, 0xD4, 0x10, 0xD4, 0x3A],
                [0x10, 0xD4, 0x9B, 0x10, 0xF6, 0xF5, 0x3A, 0x10, 0x10, 0x72],
                [0x72, 0x10, 0xD4, 0x3A, 0x72, 0x10, 0x72, 0xD4, 0x3A, 0x9B],
                [0xD4, 0x3A, 0x72, 0xD4, 0x9B, 0x9B, 0xFB, 0x3A, 0x9B, 0x72],
                [0x10, 0x10, 0x9B, 0x3A, 0x3A, 0x72, 0x10, 0x9B, 0x72, 0x9B],
                [0x9B, 0x72, 0x10, 0x10, 0xD4, 0xF4, 0x72, 0x10, 0xD4, 0xF3],
            ]
        )

        sequences = [
            Sequence([0xFB], 10),
            Sequence([0xF8, 0xF9], 20),
            Sequence([0xF2, 0xF3], 20),
            Sequence([0xF0, 0xF1, 0xF2], 30),
            Sequence([0xF7, 0xF8, 0xF9, 0xFA], 40),
            Sequence([0xF4, 0xF5, 0xF6, 0xF7, 0xF8], 50),
        ]

        max_path_length = 12

        positions = [
            (0, 8),
            (3, 8),
            (3, 9),
            (9, 9),
            (9, 5),
            (5, 5),
            (5, 4),
            (4, 4),
            (4, 0),
            (2, 0),
            (2, 6),
            (7, 6),
        ]
        expected_solution = Path([Position(row, column) for row, column in positions])

        self.run_example(
            "example of a complex puzzle with six sequences",
            matrix,
            sequences,
            max_path_length,
            expected_solution,
        )

    def run_example(
        self,
        name: str,
        matrix: Matrix,
        sequences: list[Sequence],
        max_path_length: int,
        expected_solution: Path,
    ) -> None:
        print(f"Running {name}")

        try:
            path_finder = PathFinder(matrix, sequences, max_path_length)
            actual_solution = path_finder.run()
        except InvalidArgumentError as error:
            print(f"InvalidArgumentError: {str(error)}")
            raise
        except PathNotFoundError as error:
            print(f"PathNotFoundError: {str(error)}")
            raise

        print(f"Actual solution:   {str(actual_solution)}")
        print(f"Expected solution: {str(expected_solution)}\n")

        assert actual_solution == expected_solution

    def run_example_without_solution(
        self, name: str, matrix: Matrix, sequences: list[Sequence], max_path_length: int
    ) -> None:
        print(f"Running {name}")

        try:
            path_finder = PathFinder(matrix, sequences, max_path_length)
            path_finder.run()
        except InvalidArgumentError:
            print("Actual exception:   InvalidArgumentError")
            print("Expected exception: PathNotFoundError")
            raise
        except PathNotFoundError:
            print("Actual exception:   PathNotFoundError")
            print("Expected exception: PathNotFoundError\n")
            return

        print("Actual exception:   It throws nothing")
        print("Expected exception: PathNotFoundError")

        assert False
