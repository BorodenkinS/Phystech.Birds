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


class Bird:
    body = None
    shape = None
    image = None
    mass = None
    size = None
    moment = None
    launch_status = False
    calm_res = 120
    is_move = True

    def __init__(self, x, y, space, screen):
        self.body.position = pm.Vec2d(x, y)
        space.add(self.body, self.shape)
        self.sc = screen
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
        self.sc.blit(self.image, self.body.position - pm.Vec2d(self.size, self.size))

    def remove(self):
        self.space.remove(self.body, self.shape)

    def state_checker(self):
        return abs(self.body.velocity) > 0.1 and abs(self.body.angular_velocity) > 0.1

    def recalculate_calm_res(self):
        if self.state_checker():
            self.calm_res = 120
        else:
            self.calm_res = min(self.calm_res - 1, 0)


class RedBird(Bird):
    mass = 5
    life = 20
    size = 15
    moment = pm.moment_for_circle(mass, 0, size)

    def __init__(self, x, y, space, screen):
        self.body = pm.Body(self.mass, self.moment, pm.Body.KINEMATIC)
        self.shape = pm.Circle(self.body, self.size, (0, 0))
        self.shape.elasticity = 0.95
        self.shape.friction = 1
        self.shape.collision_type = 0
        self.image = pg.image.load("redbird.png").convert_alpha()
        super().__init__(x, y, space, screen)


class TriangleBird(Bird):
    mass = 4
    life = 10
    size = 14
    moment = moment_for_triangle(mass, size)

    is_accelerated = False

    def __init__(self, x, y, space, screen):
        self.image = pg.image.load("trianglebird.png").convert_alpha()
        self.body = pm.Body(self.mass, self.moment, pm.Body.KINEMATIC)
        self.shape = pm.Poly(self.body, ((0, 0), (self.size / 2, 0.5 * self.size * 3 ** 0.5), (self.size, 0)))
        self.shape.elasticity = 0.95
        self.shape.friction = 1
        self.shape.collision_type = 0
        super().__init__(x, y, space, screen)

    def accelerate(self):
        if not self.is_accelerated and self.launch_status:
            self.body.velocity *= 10
            self.is_accelerated = True


class BigBird(Bird):
    mass = 20
    life = 20
    size = 30
    moment = pm.moment_for_circle(mass, 0, size)

    def __init__(self, x, y, space, screen):
        self.body = pm.Body(self.mass, self.moment, pm.Body.KINEMATIC)
        self.shape = pm.Circle(self.body, self.size, (0, 0))
        self.shape.elasticity = 0.7
        self.shape.friction = 1.2
        self.shape.collision_type = 0
        self.image = pg.image.load("bigbird.png").convert_alpha()
        super().__init__(x, y, space, screen)
