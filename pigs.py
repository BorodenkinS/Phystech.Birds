import pymunk as pm
import pygame as pg
import math


class Pig:
    """Класс-родитель для всех свинок"""
    body = None
    shape = None
    image = None
    size = None
    life = None

    def __init__(self, x, y, space, screen):
        """Инициализация свинки"""
        self.body.position = pm.Vec2d(x, y)
        space.add(self.body, self.shape)
        self.sc = screen
        self.space = space

    def draw(self):
        """Отрисовка свинки"""
        angle = math.degrees(self.body.angle)
        rot_image = pg.transform.rotate(self.image, -angle)
        self.sc.blit(rot_image, self.body.position - pm.Vec2d(self.size, self.size))

    def remove(self):
        """Удаление свинки"""
        self.space.remove(self.body, self.shape)

    def velocity_checker(self):
        """Обработчик движения свинки"""
        return abs(self.body.velocity) > 1 or abs(self.body.angular_velocity) > 1

    def recalculate_state(self):
        """Обработчик состояния свинки, её удаление после уничтожения"""
        if not self.velocity_checker():
            self.body.velocity = pm.Vec2d(0, 0)
            self.body.angular_velocity = 0
            self.body.angle = 0
        life_factor = self.life > 0
        if not life_factor:
            self.remove()
        return life_factor


class DefaultPig(Pig):
    """Стандартная свинка"""
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
        self.image = pg.image.load("Sprites\\it's me.png").convert_alpha()
        super().__init__(x, y, space, screen)


class KingPig(Pig):
    """Король Свинок (имеет больше жизней)"""
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


class LittlePig(Pig):
    """Маленькая свинка"""
    mass = 5
    life = 10
    size = 8
    cost = 500
    moment = pm.moment_for_circle(mass, 0, size)

    def __init__(self, x, y, space, screen):
        self.body = pm.Body(self.mass, self.moment)
        self.shape = pm.Circle(self.body, self.size, (0, 0))
        self.shape.elasticity = 1.2
        self.shape.friction = 0.5
        self.shape.collision_type = 1
        self.image = pg.image.load("Sprites\\abramovets.png").convert_alpha()
        super().__init__(x, y, space, screen)


class DefaultPig2(Pig):
    """Обычная свинья, но другой персонаж"""
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
        self.image = pg.image.load("Sprites\\andrew.png").convert_alpha()
        super().__init__(x, y, space, screen)
