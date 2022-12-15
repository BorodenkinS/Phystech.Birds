import pygame as pg
import thorpy
import pymunk as pm
from pymunk import pygame_util
from menu import *
from level import *
from obstructions import *
from birds import *
from pigs import *
from obstructions import *

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


class Game:
    WIDTH = 1200
    HEIGHT = 600
    FPS = 60

    def __init__(self):
        self.display = pg.display
        self.sc = pg.display.set_mode((Game.WIDTH, Game.HEIGHT))
        self.clock = pg.time.Clock()
        self.draw_options = pygame_util.DrawOptions(self.sc)
        self.space = pm.Space()
        self.space.gravity = 0, 9806

        self.game_state = -1

        self.opening_menu = OpeningMenu(self.sc, self.game_state)
        self.level_menu = LevelMenu(self.sc, self.game_state)
        self.level = Level(self.space, self.sc)
        self.windows = [self.level_menu] + self.level.levels + [self.opening_menu]

        self.display.set_caption("Phystech.Birds")

        pg.init()

    def __call__(self, *args, **kwargs):
        return self.gameloop()

    def gameloop(self):
        finished = False
        self.clock.tick(self.FPS)
        self.space.step(1 / self.FPS)
        while not finished:
            for event in pg.event.get():
                if event.type == pg.QUIT or event.type == pg.K_ESCAPE:
                    finished = not finished
                elif self.game_state == 1:  # т.е. состояние уровня
                    if self.mouse_pressed() and self.level.number_of_birds > 0 or not self.level.mouse_is_up:
                        self.prepare_to_fire()
                    ...
            self.drawer()
            self.remover()

        pg.quit()

    def start_level_1(self):
        self.level.level1()

    def drawer(self):
        self.sc.fill(WHITE)
        if self.game_state == 1:  # т.е. запущен уровень
            for bird in self.level.birds:
                bird.draw()
            for pig in self.level.pigs:
                pig.draw()
            for beam in self.level.beams:
                beam.draw()
            self.level.sling.draw()
        self.display.update()

    def remover(self):
        for pig in self.level.pigs_to_remove:
            pig.remove()
            self.level.pigs.remove(pig)
        for bird in self.level.birds_to_remove:
            bird.remove()
            self.level.birds.remove(bird)
        for beam in self.level.beams_to_remove:
            beam.remove()
            self.level.beams.remove(beam)

    def mouse_pressed(self):
        x_mouse, y_mouse = pg.mouse.get_pos()
        cond1 = x_mouse > 80
        cond2 = x_mouse < 262
        cond3 = y_mouse > 350
        cond4 = y_mouse < 562
        cond5 = pg.mouse.get_pressed()[0]
        return cond1 * cond2 * cond3 * cond4 * cond5

    def prepare_to_fire(self):
        sling1 = self.level.sling.sling_1
        sling_length = self.level.sling.sling_length

        if self.level.mouse_is_up:
            self.level.mouse_is_up = False
            self.level.number_of_birds -= 1
        mouse = pg.mouse.get_pos()
        direction = sling1 - mouse
        mouse_distance = abs(direction)
        unit = direction / mouse_distance
        bird_distance = min(mouse_distance, sling_length)
        bird_position = sling1 - bird_distance * unit
        bird = self.level.birds[self.level.number_of_birds]
        bird.body.position = bird_position
        self.level.sling.slings_end = bird_position - unit * bird.size


if __name__ == "__main__":
    game = Game()
    game()
