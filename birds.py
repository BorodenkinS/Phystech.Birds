import pymunk as pm
import pygame as pg
import pymunk.pygame_util
import math

WHITE = (255, 255, 255)


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
    calm_res = 120
    is_flying = False
    is_flying_times = 0
    life = None
    launch_status = False
    track = []

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
        self.is_flying = True
        self.launch_status = True

    def draw(self):
        # angle_degrees = math.degrees(self.body.angle)
        # self.image = pg.transform.rotate(self.image, angle_degrees)
        self.sc.blit(self.image, self.body.position - pm.Vec2d(self.size, self.size))
        for pos in self.track:
            pg.draw.circle(self.sc, WHITE, pos, self.size / 8)
        if self.is_flying:
            self.is_flying_times += 1
            if self.is_flying_times % 10 == 0:
                self.track.append(self.body.position)

    def remove(self):
        self.space.remove(self.body, self.shape)

    def velocity_checker(self):
        return abs(self.body.velocity) > 0.1 and abs(self.body.angular_velocity) > 0.1 or not self.launch_status


    def recalculate_state(self):
        if not self.velocity_checker():
            self.body.velocity = pm.Vec2d(0,0)
            self.body.angular_velocity = 0
            self.calm_res -= 1
        life_factor = self.life > 0 and self.calm_res > 0
        if not life_factor:
            self.remove()
        return life_factor

    def bird_function(self):
        pass


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
        self.image = pg.image.load('Sprites\\monchenko.png').convert_alpha()
        super().__init__(x, y, space, screen)


class TriangleBird(Bird):
    mass = 4
    life = 10
    size = 14
    moment = moment_for_triangle(mass, size)

    is_accelerated = False

    def __init__(self, x, y, space, screen):
        self.image = pg.image.load("Sprites\\vladimir angemych.png").convert_alpha()
        self.body = pm.Body(self.mass, self.moment, pm.Body.KINEMATIC)
        self.shape = pm.Poly(self.body, ((0, 0), (self.size / 2, 0.5 * self.size * 3 ** 0.5), (self.size, 0)))
        self.shape.elasticity = 0.95
        self.shape.friction = 1
        self.shape.collision_type = 0
        super().__init__(x, y, space, screen)

    def bird_function(self):
        '''acceleration'''
        if not self.is_accelerated and self.is_flying:
            self.body.velocity *= 5
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
        self.image = pg.image.load("Sprites\\ivanov.png").convert_alpha()
        super().__init__(x, y, space, screen)
