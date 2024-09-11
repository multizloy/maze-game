import pygame
from random import choice


class Cell:
    def __init__(self, x, y, thickness):
        self.x = x
        self.y = y
        self.thickness = thickness
        self.walls = {"top": True, "bottom": True, "left": True, "right": True}
        self.visited = False

    # draw grid cell walls
    def draw(self, sc: pygame.Surface, tile: int):
        x = self.x * tile
        y = self.y * tile

        if self.walls["top"]:
            pygame.draw.line(
                sc, pygame.Color("darkgreen"), (x, y), (x + tile, y), self.thickness
            )

        if self.walls["bottom"]:
            pygame.draw.line(
                sc,
                pygame.Color("darkgreen"),
                (x, y + tile),
                (x + tile, y + tile),
                self.thickness,
            )

        if self.walls["left"]:
            pygame.draw.line(
                sc, pygame.Color("darkgreen"), (x, y), (x, y + tile), self.thickness
            )

        if self.walls["right"]:
            pygame.draw.line(
                sc,
                pygame.Color("darkgreen"),
                (x + tile, y),
                (x + tile, y + tile),
                self.thickness,
            )

    # check if cell does exist and returns it if it does
    def check_cell(self, x: int, y: int, cols: int, rows: int, grid_cells: list):
        find_index = lambda x, y: x + y * cols
        if x < 0 or x > cols - 1 or y < 0 or y > rows - 1:
            return False
        return grid_cells[find_index(x, y)]

    # checking cell neighbors of current cell if visited (carved) or not
    def check_neighbors(self, cols: int, rows: int, grid_cells: list):
        neighbors = []
        top = self.check_cell(self.x, self.y - 1, cols, rows, grid_cells)
        bottom = self.check_cell(self.x, self.y + 1, cols, rows, grid_cells)
        left = self.check_cell(self.x - 1, self.y, cols, rows, grid_cells)
        right = self.check_cell(self.x + 1, self.y, cols, rows, grid_cells)

        if top and not top.visited:
            neighbors.append(top)
        if bottom and not bottom.visited:
            neighbors.append(bottom)
        if left and not left.visited:
            neighbors.append(left)
        if right and not right.visited:
            neighbors.append(right)

        return choice(neighbors) if neighbors else False
