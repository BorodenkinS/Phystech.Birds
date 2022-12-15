import pygame as pg
import pymunk as pm


class Sling:

    image = None
    position = (0,0)

    def __init__(self, screen):
        self.screen = screen
        self.sling_1 = pm.Vec2d(135, 412)
        self.sling_2 = pm.Vec2d(160, 412)
        self.sling_length = 100
        self.sling_end = (self.sling_1 + self.sling_2)/2

    def draw(self):
        self.screen.blit(self.image, self.position)
        pg.draw.line(self.screen, (0, 0, 0), self.sling_end, self.sling_1, 5)
        pg.draw.line(self.screen, (0, 0, 0), self.sling_end, self.sling_2, 5)
