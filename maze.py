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
