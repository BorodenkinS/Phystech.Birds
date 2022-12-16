import pymunk as pm
import pygame as pg
from birds import *
from pigs import *
from obstructions import *
from beams import *


class Level:
    birds = []
    pigs = []
    beams = []
    obstructions = []
    number_of_birds = 0
    mouse_is_up = True
    pigs_to_remove = []
    birds_to_remove = []
    beams_to_remove = []

    def __init__(self, space, screen):
        self.sc = screen
        self.space = space
        self.levels = [self.level1, self.level2, self.level3, self.level4, self.level5]
        self.sling = Sling(self.sc)
        self.sling.position = ...

        # self.sc.blit(self.sling.image) больше не нужно

    def level1(self):
        # проработать механизм удаления прошлых объектов.
        # просто заносить в список на удаление, наверное, недостаточно, ибо функция удаления сработает позже
        # создания новых объектов
        woodbeam = WoodBeam(905, 750, False, self.space, self.sc)
        self.obstructions.append(woodbeam)
        woodbeam = WoodBeam(995, 750, False, self.space, self.sc)
        self.obstructions.append(woodbeam)
        woodbeam = WoodBeam(950, 695, True, self.space, self.sc)
        self.obstructions.append(woodbeam)
        woodbeam = WoodBeam(905, 640, False, self.space, self.sc)
        self.obstructions.append(woodbeam)
        woodbeam = WoodBeam(995, 640, False, self.space, self.sc)
        self.obstructions.append(woodbeam)
        woodbeam = WoodBeam(950, 535, True, self.space, self.sc)
        self.obstructions.append(woodbeam)
        glassbeam = GlassBeam(895, 750, False, self.space, self.sc)
        self.obstructions.append(glassbeam)
        glassbeam = GlassBeam(800, 750, False, self.space, self.sc)
        self.obstructions.append(glassbeam)
        glassbeam = GlassBeam(845, 695, True, self.space, self.sc)
        self.obstructions.append(glassbeam)

        pig = DefaultPig(950, 675, self.space, self.sc)
        self.pigs.append(pig)
        pig = DefaultPig(845, 785, self.space, self.sc)
        self.pigs.append(pig)
        pig = KingPig(950, 785, self.space, self.sc)
        self.pigs.append(pig)

        bird = RedBird(100, 785, self.space, self.sc)
        self.birds.append(bird)
        bird = RedBird(75, 785, self.space, self.sc)
        self.birds.append(bird)
        bird = RedBird(50, 785, self.space, self.sc)
        self.birds.append(bird)
        self.number_of_birds = 3

        # beams ...

    def level2(self):
        pass

    def level3(self):
        pass

    def level4(self):
        pass

    def level5(self):
        pass
