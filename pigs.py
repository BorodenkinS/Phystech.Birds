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
        self.sc = screen
        self.space = space

    def draw(self):
        angle_degrees = math.degrees(self.body.angle)
        # self.image = pg.transform.rotate(self.image, angle_degrees)
        self.sc.blit(self.image, self.body.position - pm.Vec2d(self.size, self.size))

    def remove(self):
        self.space.remove(self.body, self.shape)


class DefaultPig(Pig):
    mass = 5
    life = 20
    size = 15
    cost = 1000
    moment = pm.moment_for_circle(mass, 0, size)

    def __init__(self, x, y, space, screen):
        self.body = pm.Body(self.mass, self.moment)
        self.shape = pm.Circle(self.body, self.size, (0, 0))
        self.shape.elasticity = 0.95
        self.shape.friction = 1
        self.shape.collision_type = 1
        self.image = pg.image.load("Sprites\\abramovets.png").convert_alpha()
        super().__init__(x, y, space, screen)


    def __str__(self):
        return f"Def pos={self.body.position}"

class KingPig(Pig):
    mass = 10
    life = 40
    size = 30
    moment = pm.moment_for_circle(mass, 0, size)
    cost = 5000

    def __init__(self, x, y, space, screen):
        self.body = pm.Body(self.mass, self.moment)
        self.shape = pm.Circle(self.body, self.size, (0, 0))
        self.shape.elasticity = 0.4
        self.shape.friction = 2
        self.shape.collision_type = 1
        self.image = pg.image.load("Sprites\\smgshnic.png").convert_alpha()
        super().__init__(x, y, space, screen)


    def __str__(self):
        return f"King pos={self.body.position}"
