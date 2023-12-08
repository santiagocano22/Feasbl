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
    def __init__(
        self, matrix: Matrix, sequences: list[Sequence], max_path_length: int
    ) -> None:
        self.matrix = matrix
        self.sequences = sequences
        self.max_path_length = max_path_length

    def run(self) -> Path:
        # TODO: Implement me.
        return Path()

    # You can add your own class members here.
