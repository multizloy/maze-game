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
