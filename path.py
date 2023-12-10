# ---------------------------------------------------------------------------------------------
# PLEASE DO NOT MODIFY, RENAME OR REMOVE ANY OF CLASSES, METHODS AND VARIABLES BELOW.
# YOU CAN ADD YOUR OWN METHODS AND VARIABLES TO THE EXISTING CLASSES AND USE THEM IN YOUR WORK.
# ---------------------------------------------------------------------------------------------

from .position import Position


class Path:
    def __init__(self, positions: list[Position] | None = None) -> None:
        self.positions = positions or []

    def __eq__(self, other) -> bool:
        return self.positions == other.positions

    def __str__(self) -> str:
        return ", ".join(str(position) for position in self.positions)

    # You can add your own class members here.
    def add_position(self, position: Position) -> None:
            self.positions.append(position)

    def delete_last_position(self):
        if self.positions:
            self.positions.pop()