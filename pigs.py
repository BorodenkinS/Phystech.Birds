import pymunk as pm
import pygame as pg
import math


class Pig():
    body = None
    shape = None
    image = None

    def __init__(self, x, y, space):
        self.body.position = pm.Vec2d(x, y)
        space.add(self.body, self.shape)

    def draw(self, screen):
        angle_degrees = math.degrees(self.body.angle)
        self.image = pg.transform.rotate(self.image, angle_degrees)
        screen.blit(self.image, self.body.position)

    def remove(self, space):
        space.remove(self.body, self.shape)


class DefaultPig(Pig):
    mass = 5
    life = 20
    radius = 14
    moment = pm.moment_for_circle(mass, 0, radius)
    body = pm.Body(mass, moment)
    shape = pm.Circle(body, radius, (0, 0))
    shape.elasticity = 0.95
    shape.friction = 1
    shape.collision_type = 1
    image = pg.image.load("defaultpig.png").convert_alpha()


class KingPig(Pig):
    mass = 10
    life = 40
    radius = 30
    moment = pm.moment_for_circle(mass, 0, radius)
    body = pm.Body(mass, moment)
    shape = pm.Circle(body, radius, (0, 0))
    shape.elasticity = 0.4
    shape.friction = 2
    shape.collision_type = 1
    image = pg.image.load("kingpig.png").convert_alpha()
