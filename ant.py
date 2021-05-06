from enum import Enum
from typing import List


class Direction(int, Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3


class Ant:
    def __init__(self, ant_position: List[int]):
        """
        Parameters
        ----------
        ant_position : List[int, int]
            A list with two integers representing the x and y coordinates
        """
        self.position = ant_position
        self.direction = Direction.EAST
    
    def move(self, box_state: int):
        """
        If the state of the box is 1 the ant will move 90° to the right.
        If the state of the box is 0 the ant will move 90° to the left.
        """
        if box_state == 1:
            right_left = -1
        else:
            right_left = 1
        self.change_direction(right_left)

        # Update ant position
        if self.direction == Direction.EAST:
            self.position[0] += 1
        elif self.direction == Direction.WEST:
            self.position[0] -= 1
        elif self.direction == Direction.SOUTH:
            self.position[1] -= 1
        else:
            self.position[1] += 1
    
    def change_direction(self, right_left: int):
        """modify the ant's direction according to the state of the box"""
        self.direction = (self.direction + right_left) % 4
        
