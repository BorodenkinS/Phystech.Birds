import pymunk as pm
import pygame as pg
from characters import *
from obstructions import *


class Level:
    def __init__(self, screen):
        self.screen = screen
        self.birds = []
        self.pigs = []
        self.obstructions = []
        self.levels = [self.level1, self.level2, self.level3, self.level4, self.level5]

    def __getitem__(self, item):
        return self.levels[item]()

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
