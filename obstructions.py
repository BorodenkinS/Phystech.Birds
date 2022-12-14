import pygame
import pymunk


class Sling:

    image = None

    def __init__(self, screen):
        self.sc = screen
        self.sling_1 = pymunk.Vec2d(135, 412)
        self.sling_2 = pymunk.Vec2d(160, 412)
        self.sling_length = 100
        self.sling_end = (self.sling_1 + self.sling_2)/2
