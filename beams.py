import pymunk as pm
import pygame as pg
import pymunk.pygame_util
import math


class Beam:
    body = None
    shape = None
    image = None
    width = None
    length = None

    def __init__(self, x, y, is_hor, space, screen):
        if not is_hor:
            self.image = pg.transform.rotate(self.image, 90)
            shape_options = self.shape.elasticity, self.shape.friction, self.shape.collision_type
            self.shape = pm.Segment(self.body, (0, 0), (0, self.length), self.width)
            self.shape.elasticity, self.shape.friction, self.shape.collision_type = shape_options
            self.lenx, self.leny = self.width, self.length
        else:
            self.lenx, self.leny = self.length, self.width

        self.body.position = pm.Vec2d(x, y)
        space.add(self.body, self.shape)
        self.screen = screen
        self.space = space

    def draw(self):
        angle_degrees = math.degrees(self.body.angle)
        self.image = pg.transform.rotate(self.image, angle_degrees)
        self.screen.blit(self.image, self.body.position - 0.5 * pm.Vec2d(self.lenx, self.leny))

    def remove(self):
        self.space.remove(self.body, self.shape)


class WoodBeam(Beam):
    mass = 1
    life = 1
    width, length = 10, 100
    moment = mass * (width ** 2 + length ** 2) / 12
    body = pm.Body(mass, moment)
    shape = pm.Segment(body, (0, 0), (length, 0), width)
    shape.elasticity = 1
    shape.friction = 1
    shape.collision_type = 0

    def __init__(self, x, y, is_hor, space, screen):
        self.image = pg.image.load("woodbeamhorizontal.png").convert_alpha()
        super().__init__(x, y, is_hor, space, screen)


class GlassBeam(Beam):
    mass = 1
    life = 1
    width, length = 10, 100
    moment = mass * (width ** 2 + length ** 2) / 12
    body = pm.Body(mass, moment)
    shape = pm.Segment(body, (0, 0), (length, 0), width)
    shape.elasticity = 1
    shape.friction = 1
    shape.collision_type = 0

    def __init__(self, x, y, is_hor, space, screen):
        self.image = pg.image.load("glassbeamhorizontal.png").convert_alpha()
        super().__init__(x, y, is_hor, space, screen)