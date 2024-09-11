import pygame
from random import choice


class Cell:
    def __init__(self, x, y, thickness):
        self.x = x
        self.y = y
        self.thickness = thickness
        self.walls = {"top": True, "bottom": True, "left": True, "right": True}
        self.visited = False
