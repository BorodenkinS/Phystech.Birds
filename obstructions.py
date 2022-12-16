import pymunk as pm
import pygame as pg
import pymunk.pygame_util
import math

pymunk.pygame_util.positive_y_is_up = False


class Sling:
    image = None
    position = (0, 0)

    def __init__(self, screen):
        self.sc = screen
        self.sling_1 = pm.Vec2d(135, 412)
        self.sling_2 = pm.Vec2d(160, 412)
        self.sling_length = 100
        self.sling_end = (self.sling_1 + self.sling_2) / 2

    def draw(self):
        self.sc.blit(self.image, self.position)
        pg.draw.line(self.sc, (0, 0, 0), self.sling_end, self.sling_1, 5)
        pg.draw.line(self.sc, (0, 0, 0), self.sling_end, self.sling_2, 5)


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
        self.sc = screen
        self.space = space

    def draw(self):
        angle_degrees = math.degrees(self.body.angle)
        self.image = pg.transform.rotate(self.image, angle_degrees)
        self.sc.blit(self.image, self.body.position - 0.5 * pm.Vec2d(self.lenx, self.leny))

    def remove(self):
        self.space.remove(self.body, self.shape)


class WoodBeam(Beam):
    mass = 1
    life = 1
    length = 100
    width = 10
    moment = mass * (width ** 2 + length ** 2) / 12

    def __init__(self, x, y, is_hor, space, screen):
        self.body = pm.Body(self.mass, self.moment)
        self.shape = pm.Segment(self.body, (0, 0), (self.length, 0), self.width)
        self.shape.elasticity = 1
        self.shape.friction = 1
        self.shape.collision_type = 0
        self.image = pg.image.load("woodbeamhorizontal.png").convert_alpha()
        super().__init__(x, y, is_hor, space, screen)


class GlassBeam(Beam):
    mass = 1
    life = 1
    width = 10
    length = 100
    moment = mass * (width ** 2 + length ** 2) / 12

    def __init__(self, x, y, is_hor, space, screen):
        self.body = pm.Body(self.mass, self.moment)
        self.shape = pm.Segment(self.body, (0, 0), (self.length, 0), self.width)
        self.shape.elasticity = 1
        self.shape.friction = 1
        self.shape.collision_type = 0
        self.image = pg.image.load("glassbeamhorizontal.png").convert_alpha()
        super().__init__(x, y, is_hor, space, screen)
