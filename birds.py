import pymunk as pm
import pygame as pg
import pymunk.pygame_util
import math


class Bird:
    """Класс-родитель для всех птиц"""

    body = None
    shape = None
    image = None
    mass = None
    size = None
    moment = None
    calm_res = 240
    is_flying = False
    is_flying_times = 0
    life = None
    launch_status = False
    

    def __init__(self, x, y, space, screen):
        """Инициализация птички как тела в pymunk"""
        self.track = []
        self.body.position = pm.Vec2d(x, y)
        space.add(self.body, self.shape)
        self.sc = screen
        self.space = space

    def launch(self, velocity):
        """Запуск птички"""
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
        """Отрисовка птички на экране pygame, отрисовка траектории её полёта"""
        angle = math.degrees(self.body.angle)
        rot_image = pg.transform.rotate(self.image, -angle)
        self.sc.blit(rot_image, self.body.position - pm.Vec2d(self.size, self.size))
        for pos in self.track:
            pg.draw.circle(self.sc, (255, 255, 255), pos, 4)
        if self.is_flying:
            self.is_flying_times += 1
            if self.is_flying_times % 10 == 0:
                self.track.append(self.body.position)

    def remove(self):
        """Удаление птички"""
        self.space.remove(self.body, self.shape)

    def velocity_checker(self):
        """Обработчик движения птички"""
        return abs(self.body.velocity) > 0.5 or abs(self.body.angular_velocity) > 0.5 or not self.launch_status

    def recalculate_state(self):
        """Обработчик состояния птицы, её удаление после использования"""
        if not self.velocity_checker():
            self.body.velocity = pm.Vec2d(0, 0)
            self.body.angular_velocity = 0
            self.calm_res -= 1

        life_factor = self.life > 0 and self.calm_res > 0
        if not life_factor:
            self.remove()
        return life_factor

    def bird_function(self):
        """Некоторые птицы могут иметь дополнительные функции"""
        pass


class RedBird(Bird):
    """Классическая птица"""

    mass = 5
    life = 20
    size = 15
    moment = pm.moment_for_circle(mass, 0, size)

    def __init__(self, x, y, space, screen):
        self.body = pm.Body(self.mass, self.moment, pm.Body.KINEMATIC)
        self.shape = pm.Circle(self.body, self.size, (0, 0))
        self.shape.elasticity = 0.5
        self.shape.friction = 4
        self.shape.collision_type = 0
        self.image = pg.image.load('Sprites\\monchenko.png').convert_alpha()
        super().__init__(x, y, space, screen)


class TriangleBird(Bird):
    """Ускоряющаяся птица (в оригинальной игре имеет треугольную форму)"""

    mass = 4
    life = 20
    size = 15
    moment = pm.moment_for_circle(mass, size, 0)

    is_accelerated = False

    def __init__(self, x, y, space, screen):
        self.image = pg.image.load("Sprites\\vladimir angemych.png").convert_alpha()
        self.body = pm.Body(self.mass, self.moment, pm.Body.KINEMATIC)
        self.shape = pm.Circle(self.body, self.size, (0, 0))
        self.shape.elasticity = 0.2
        self.shape.friction = 4
        self.shape.collision_type = 0
        super().__init__(x, y, space, screen)

    def bird_function(self):
        """Функция ускорения птицы (реализуется при нажатии)"""
        if not self.is_accelerated and self.is_flying:
            self.body.velocity *= 3
            self.is_accelerated = True


class BigBird(Bird):
    """Большая птица"""

    mass = 20
    life = 30
    size = 30
    moment = pm.moment_for_circle(mass, 0, size)

    def __init__(self, x, y, space, screen):
        self.body = pm.Body(self.mass, self.moment, pm.Body.KINEMATIC)
        self.shape = pm.Circle(self.body, self.size, (0, 0))
        self.shape.elasticity = 0.2
        self.shape.friction = 4
        self.shape.collision_type = 0
        self.image = pg.image.load("Sprites\\ivanov.png").convert_alpha()
        super().__init__(x, y, space, screen)
