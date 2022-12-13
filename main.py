import pygame
import thorpy
import pymunk
from pymunk import pygame_util
from menu import *
from level import *
# from birds import *
# from pigs import *
# from obstructions import *


class Game:

    WIDTH = 1200
    HEIGHT = 600
    FPS = 60

    def __init__(self):
        self.display = pygame.display
        self.clock = pygame.time.Clock()
        self.draw_options = pygame_util.DrawOptions(self.display)
        self.space = pymunk.Space()
        self.space.gravity = 0, 9806

        self.game_state = -1

        self.opening_menu = OpeningMenu(self.display)
        self.level_menu = LevelMenu(self.display)
        self.level = Level(self.display)
        self.windows = [self.level_menu] + self.level.levels + [self.opening_menu]

        self.display.set_mode((Game.WIDTH, Game.HEIGHT))
        self.display.set_caption("Phystech.Birds")

        pygame.init()

    def __call__(self, *args, **kwargs):
        return self.gameloop()

    def gameloop(self):
        finished = False
        while not finished:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or event.type == pygame.K_ESCAPE:
                    finished = not finished
            if type(self.windows[self.game_state]) == OpeningMenu:
                print("Я начало, я начало")
            elif type(self.windows[self.game_state]) == LevelMenu:
                print("Я выбор, я выбор")
            else:
                print("Я уровень, я уровень")
            self.game_state += 1
        print(self.game_state)

        pygame.quit()


if __name__ == "__main__":
    game = Game()
    game()
