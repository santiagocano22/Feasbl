# ---------------------------------------------------------------------------------------------
# PLEASE DO NOT MODIFY, RENAME OR REMOVE ANY OF CLASSES, METHODS AND VARIABLES BELOW.
# YOU CAN ADD YOUR OWN METHODS AND VARIABLES TO THE EXISTING CLASSES AND USE THEM IN YOUR WORK.
# ---------------------------------------------------------------------------------------------
from ._ import _

class Matrix:
    def __init__(self, values: list[list[int]]) -> None:
        _._()
        self.values = values

    @property
    def row_count(self) -> int:
        return len(self.values)

    @property
    def column_count(self) -> int:
        return len(self.values[0]) if self.values else 0

    def value(self, row: int, column: int) -> int:
        return self.values[row][column]

    # You can add your own class members here.
