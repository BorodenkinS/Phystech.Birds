import pymunk as pm
import pygame as pg
import pymunk.pygame_util
import math


def moment_for_triangle(mass, size):
    '''Для долбоёпов.
    Осторожно! Интегрирование в уме!
    '''
    h = 0.5 * size * 3 ** 0.5
    return 7 * size * h ** 3 * mass / 144


class Bird():
    body = None
    shape = None
    image = None
    mass = None
    size = None
    moment = None
    launch_status = False

    def __init__(self, x, y, space, screen):
        self.body.position = pm.Vec2d(x, y)
        space.add(self.body, self.shape)
        self.screen = screen
        self.space = space

    def launch(self, velocity):
        dynamic_body = pm.Body(self.mass, self.moment)
        dynamic_body.position = self.body.position
        dynamic_body.velocity = velocity
        dynamic_shape = pm.Shape.copy(self.shape)
        dynamic_shape.body = dynamic_body
        self.remove()
        self.body = dynamic_body
        self.shape = dynamic_shape
        self.space.add(self.body, self.shape)
        self.launch_status = True

    def draw(self):
        angle_degrees = math.degrees(self.body.angle)
        self.image = pg.transform.rotate(self.image, angle_degrees)
        self.screen.blit(self.image, self.body.position - pm.Vec2d(self.size, self.size))

    def remove(self):
        self.space.remove(self.body, self.shape)


class RedBird(Bird):
    mass = 5
    life = 20
    size = 15
    moment = pm.moment_for_circle(mass, 0, size)
    body = pm.Body(mass, moment, pm.Body.KINEMATIC)
    shape = pm.Circle(body, size, (0, 0))
    shape.elasticity = 0.95
    shape.friction = 1
    shape.collision_type = 0

    def __init__(self, x, y, space, screen):
        super().__init__(x, y, space, screen)
        self.image = pg.image.load("redbird.png").convert_alpha()


class TriangleBird(Bird):
    mass = 4
    life = 10
    size = 14
    moment = moment_for_triangle(mass, size)
    body = pm.Body(mass, moment, pm.Body.KINEMATIC)
    shape = pm.Poly(body, ((0, 0), (size / 2, 0.5 * size * 3 ** 0.5), (size, 0)))
    shape.elasticity = 0.95
    shape.friction = 1
    shape.collision_type = 0
    is_accelerated = False

    def __init__(self, x, y, space, screen):
        super().__init__(x, y, space, screen)
        self.image = pg.image.load("trianglebird.png").convert_alpha()

    def accelerate(self):
        if not self.is_accelerated and self.launch_status:
            self.body.velocity *= 10
            self.is_accelerated = True


class BigBird(Bird):
    mass = 20
    life = 20
    size = 30
    moment = pm.moment_for_circle(mass, 0, size)
    body = pm.Body(mass, moment, pm.Body.KINEMATIC)
    shape = pm.Circle(body, size, (0, 0))
    shape.elasticity = 0.7
    shape.friction = 1.2
    shape.collision_type = 0

    def __init__(self, x, y, space, screen):
        super().__init__(x, y, space, screen)
        self.image = pg.image.load("bigbird.png").convert_alpha()
