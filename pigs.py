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

    def __init__(self, x, y, space, screen):
        self.body = pm.Body(self.mass, self.moment)
        self.shape = pm.Circle(self.body, self.radius, (0, 0))
        self.shape.elasticity = 0.95
        self.shape.friction = 1
        self.shape.collision_type = 0
        self.image = pg.image.load("defaultpig.png").convert_alpha()
        super().__init__(x, y, space, screen)


class KingPig(Pig):
    mass = 10
    life = 40
    radius = 30
    moment = pm.moment_for_circle(mass, 0, radius)

    def __init__(self, x, y, space, screen):
        self.body = pm.Body(self.mass, self.moment)
        self.shape = pm.Circle(self.body, self.radius, (0, 0))
        self.shape.elasticity = 0.4
        self.shape.friction = 2
        self.shape.collision_type = 0
        self.image = pg.image.load("kingpig.png").convert_alpha()
        super().__init__(x, y, space, screen)
