import pymunk as pm
import pygame as pg
import math


class Pig:
    body = None
    shape = None
    image = None
    size = None

    def __init__(self, x, y, space, screen):
        self.body.position = pm.Vec2d(x, y)
        space.add(self.body, self.shape)
        self.screen = screen
        self.space = space

    def draw(self):
        angle_degrees = math.degrees(self.body.angle)
        self.image = pg.transform.rotate(self.image, angle_degrees)
        self.screen.blit(self.image, self.body.position - pm.Vec2d(self.size, self.size))

    def remove(self):
        self.space.remove(self.body, self.shape)


class DefaultPig(Pig):
    mass = 5
    life = 20
    radius = 14
    moment = pm.moment_for_circle(mass, 0, radius)
    body = pm.Body(mass, moment)
    shape = pm.Circle(body, radius, (0, 0))
    shape.elasticity = 0.95
    shape.friction = 1
    shape.collision_type = 0

    def __init__(self, x, y, space, screen):
        super().__init__(x, y, space, screen)
        self.image = pg.image.load("defaultpig.png").convert_alpha()


class KingPig(Pig):
    mass = 10
    life = 40
    radius = 30
    moment = pm.moment_for_circle(mass, 0, radius)
    body = pm.Body(mass, moment)
    shape = pm.Circle(body, radius, (0, 0))
    shape.elasticity = 0.4
    shape.friction = 2
    shape.collision_type = 0

    def __init__(self, x, y, space, screen):
        super().__init__(x, y, space, screen)
        self.image = pg.image.load("kingpig.png").convert_alpha()
