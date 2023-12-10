# ---------------------------------------------------------------------------------------------
# PLEASE DO NOT MODIFY, RENAME OR REMOVE ANY OF CLASSES, METHODS AND VARIABLES BELOW.
# YOU CAN ADD YOUR OWN METHODS AND VARIABLES TO THE EXISTING CLASSES AND USE THEM IN YOUR WORK.
# ---------------------------------------------------------------------------------------------


class Position:
    def __init__(self, row: int, column: int) -> None:
        self.row = row
        self.column = column

    def __eq__(self, other) -> bool:
        return self.row == other.row and self.column == other.column

    def __str__(self) -> str:
        return f"({self.row}, {self.column})"

    # You can add your own class members here.
    def __hash__(self) -> int:
        return hash((self.row, self.column))
