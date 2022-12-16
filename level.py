import pymunk
import pygame
from birds import *
from pigs import *
from obstructions import *
from beams import *


class Level:
    def __init__(self, space,  screen):
        self.sc = screen
        self.space = space
        self.birds = []
        self.pigs = []
        self.obstructions = []
        self.levels = [self.level1, self.level2, self.level3, self.level4, self.level5]
        self.sling = Sling(self.sc)

        self.sc.blit(self.sling.image)

    def level1(self):
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

    def level2(self):
        pass

    def level3(self):
        pass

    def level4(self):
        pass

    def level5(self):
        pass
