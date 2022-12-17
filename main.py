import pygame
import pymunk
from pymunk import pygame_util

from level import Level

from birds import *
from pigs import *
from obstructions import *


class Game:

    WIDTH = 1200
    HEIGHT = 600
    FPS = 60

    def __init__(self):
        pygame.init()
        self.display = pygame.display.set_mode((Game.WIDTH, Game.HEIGHT))
        self.icon = pygame.image.load("Sprites\\cat dgap.ico")
        pygame.display.set_icon(self.icon)
        pygame.display.set_caption("Phystech.Birds")
        self.space = pymunk.Space()

        self.game_state = -1

        self.clock = pygame.time.Clock()
        self.draw_options = pygame_util.DrawOptions(self.display)
        self.space = pymunk.Space()
        self.space.gravity = 0, 9806

        self.level = Level(self.space, self.display)
        self.windows = [self.level_menu] + self.level.levels + [self.opening_menu]

    def __call__(self, *args, **kwargs):
        return self.gameloop()

    def opening_menu(self):
        self.display.fill((255, 255, 255))

    def level_menu(self):
        self.display.fill((255, 0, 255))
        self.display.blit(pygame.image.load("Sprites\\bg for menu 1200x600.png"), (0, 0))

    def gameloop(self):
        finished = False
        while not finished:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or event.type == pygame.K_ESCAPE:
                    finished = not finished
                if event.type == pygame.KEYDOWN:
                    if (self.game_state == -1 and event.key == pygame.K_RETURN) or \
                            (self.game_state in range(1, 6) and event.key == pygame.K_BACKSPACE):
                        self.game_state = 0
                    elif self.game_state == 0 and event.key == pygame.K_BACKSPACE:
                        self.game_state = -1
                    elif self.game_state == 0 and event.key in [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4,
                                                                pygame.K_5]:
                        states = {pygame.K_1: 1, pygame.K_2: 2, pygame.K_3: 3, pygame.K_4: 4, pygame.K_5: 5}
                        self.game_state = states[event.key]
            self.windows[self.game_state]()
            self.clock.tick(Game.FPS)
            pygame.display.update()

        pygame.quit()


if __name__ == "__main__":
    game = Game()
    game()
