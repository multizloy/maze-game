import pygame
from cell import Cell


class Maze:
    def __init__(self, cols: int, rows: int):
        self.cols = cols
        self.rows = rows
        self.thickness = 4

        self.grid_cells = [
            Cell(cols, rows, self.thickness)
            for row in range(self.rows)
            for col in range(self.cols)
        ]

    # carve grid cell walls
    def remove_walls(self, current: Cell, next: Cell):
        dx = current.x - next.x
        if dx == 1:
            current.walls["left"] = False
            next.walls["right"] = False
        elif dx == -1:
            current.walls["right"] = False
            next.walls["left"] = False
        dy = current.y - next.y
        if dy == 1:
            current.walls["top"] = False
            next.walls["bottom"] = False
        elif dy == -1:
            current.walls["top"] = False
            next.walls["bottom"] = False
