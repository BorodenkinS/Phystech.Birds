import pymunk as pm
import pygame as pg
import pymunk.pygame_util
import math

pymunk.pygame_util.positive_y_is_up = False


class Sling:
    position = None
    direction = None

    def __init__(self, screen):
        self.image = pg.image.load("Sprites\\sling.png").convert_alpha()
        self.sc = screen
        self.sling_1 = pm.Vec2d(135, 497)
        self.sling_2 = pm.Vec2d(160, 497)
        self.sling_length = 100
        self.sling_end = (self.sling_1 + self.sling_2) / 2

    def draw(self):
        self.sc.blit(self.image, self.position)
        pg.draw.line(self.sc, (0, 0, 0), self.sling_end, self.sling_1, 5)
        pg.draw.line(self.sc, (0, 0, 0), self.sling_end, self.sling_2, 5)

    def reset(self):
        self.sling_end = (self.sling_1 + self.sling_2) / 2
        self.direction = None


class Beam:
    body = None
    shape = None
    image = None
    width = None
    length = None
    life = None

    def __init__(self, x, y, is_hor, space, screen):
        if not is_hor:
            self.image = pg.transform.rotate(self.image, 90)
            shape_options = self.shape.elasticity, self.shape.friction, self.shape.collision_type
            self.shape = pm.Poly.create_box(self.body, (self.width, self.length))
            self.shape.elasticity, self.shape.friction, self.shape.collision_type = shape_options
            self.lenx, self.leny = self.width, self.length
        else:
            self.lenx, self.leny = self.length, self.width

        self.body.position = pm.Vec2d(x, y)
        space.add(self.body, self.shape)
        self.sc = screen
        self.space = space

    def draw(self):
        angle = math.degrees(self.body.angle)
        rot_image = pg.transform.rotate(self.image, angle)
        self.sc.blit(rot_image, self.body.position - 0.5 * pm.Vec2d(self.lenx, self.leny))

    def remove(self):
        self.space.remove(self.body, self.shape)

    def velocity_checker(self):
        return abs(self.body.velocity) > 0.1 or abs(self.body.angular_velocity) > 0.1

    def recalculate_state(self):
        if not self.velocity_checker():
            self.body.velocity = pm.Vec2d(0, 0)
            self.body.angular_velocity = 0
        life_factor = self.life > 0
        if not life_factor:
            self.remove()
        return life_factor


class WoodBeam(Beam):
    mass = 1
    life = 1
    length = 100
    width = 10
    cost = 500
    moment = mass * (width ** 2 + length ** 2) / 12

    def __init__(self, x, y, is_hor, space, screen):
        self.body = pm  .Body(self.mass, self.moment)
        self.shape = pm.Poly.create_box(self.body, (self.length, self.width))
        self.shape.color = (255, 0, 0)
        self.shape.elasticity = 0.1
        self.shape.friction = 3
        self.shape.collision_type = 2
        self.body.angle = 0
        self.image = pg.image.load("Sprites\\wood.png").convert_alpha()
        super().__init__(x, y, is_hor, space, screen)


class GlassBeam(Beam):
    mass = 1
    life = 1
    width = 10
    cost = 100
    length = 100
    moment = mass * (width ** 2 + length ** 2) / 12

    def __init__(self, x, y, is_hor, space, screen):
        self.body = pm.Body(self.mass, self.moment)
        self.shape = pm.Poly.create_box(self.body, (self.length, self.width))
        self.shape.elasticity = 0.1
        self.shape.friction = 3
        self.shape.collision_type = 2
        self.image = pg.image.load("Sprites\\glass.png").convert_alpha()
        super().__init__(x, y, is_hor, space, screen)
