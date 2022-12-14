import pymunk
import pygame
# from birds import *
# from pigs import *
from obstructions import *


class Level:
    def __init__(self, screen):
        self.sc = screen
        self.birds = []
        self.pigs = []
        self.obstructions = []
        self.levels = [self.level1, self.level2, self.level3, self.level4, self.level5]
        self.sling = Sling(self.sc)

        self.sc.blit(self.sling.image)

    def level1(self):
        pass

    def level2(self):
        pass

    def level3(self):
        pass

    def level4(self):
        pass

    def level5(self):
        pass
