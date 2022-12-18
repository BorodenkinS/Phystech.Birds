import pygame as pg
import thorpy
import pymunk as pm
from pymunk import pygame_util
# from menu import *
from level import *
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
        self.icon = pg.image.load("Sprites\\cat dgap.ico")
        pg.display.set_icon(self.icon)
        self.clock = pg.time.Clock()
        self.draw_options = pygame_util.DrawOptions(self.sc)
        self.space = pm.Space()
        self.space.gravity = 0, 1000

        self.game_state = 5
        # self.opening_menu = OpeningMenu(self.sc, self.game_state)
        # self.level_menu = LevelMenu(self.sc, self.game_state)
        self.level = Level(self.space, self.sc)
        self.windows = [self.level_menu] + self.level.levels + [self.opening_menu]

        self.display.set_caption("Phystech.Birds")

        self.space.add_collision_handler(0, 1).post_solve = self.post_solve_bird_pig
        self.space.add_collision_handler(0, 2).post_solve = self.post_solve_bird_beam
        self.space.add_collision_handler(1, 2).post_solve = self.post_solve_pig_beam
        self.space.add_collision_handler(0, 3).post_solve = self.post_solve_pig_ground
        self.space.add_collision_handler(1, 3).post_solve = self.post_solve_pig_ground
        self.space.add_collision_handler(2, 3).post_solve = self.post_solve_beam_ground
        self.start_level_5()

        pg.init()

    def opening_menu(self):
        self.sc.fill((255, 255, 255))

    def level_menu(self):
        self.sc.fill((255, 0, 255))
        self.sc.blit(pg.image.load("Sprites\\bg for menu 1200x600.png"), (0, 0))

    def __call__(self, *args, **kwargs):
        return self.gameloop()

    def gameloop(self):
        finished = False

        while not finished:
            self.clock.tick(self.FPS)
            self.space.step(1 / self.FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT or event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                    finished = not finished
                elif self.game_state > 0:
                    if self.mouse_pressed(event) and self.level.number_of_birds > 0 or not self.level.mouse_is_up:
                        self.prepare_to_fire()
                    if not self.level.flying_bird is None:
                        if self.mouse_pressed2(event):
                            self.level.flying_bird.bird_function()

                    if event.type == pg.MOUSEBUTTONUP and event.button == 1 and not self.level.mouse_is_up:
                        self.level.mouse_is_up = True
                        self.shot()

            if self.game_state > 0:
                self.bird_checker()
                # self.remover()
                self.drawer()

        pg.quit()

    def start_level_1(self):
        self.level.level1()

    def start_level_2(self):
        self.level.level2()

    def start_level_3(self):
        self.level.level3()

    def start_level_4(self):
        self.level.level4()

    def start_level_5(self):
        self.level.level5()

    def drawer(self):
        self.sc.blit(self.level.background_surf, self.level.background_surf.get_rect(bottomright=(1200, 600)))
        self.sc.blit(self.level.ground_surf, self.level.ground_surf.get_rect(bottomright=(1200, 600)))
        for bird in self.level.birds:
            bird.draw()
        for pig in self.level.pigs:
            pig.draw()
        for beam in self.level.beams:
            beam.draw()
        self.level.sling.draw()
        self.display.update()

    def bird_checker(self):
        for bird in self.level.birds:
            bird.recalculate_calm_res()
            if not bird.calm_res:
                self.level.birds_to_remove.append(bird)

    def remover(self):
        for bird in self.level.birds_to_remove:
            bird.remove()
            self.level.birds.remove(bird)
        for pig in self.level.pigs_to_remove:
            pig.remove()
            self.level.pigs.remove(pig)
        for beam in self.level.beams_to_remove:
            beam.remove()
            self.level.beams.remove(beam)

    def mouse_pressed2(self, event):
        x_mouse, y_mouse = pg.mouse.get_pos()
        cond1 = x_mouse >= 262
        cond2 = y_mouse <= 350
        cond3 = (event.type == pg.MOUSEBUTTONDOWN and event.button == 1)
        return cond1 * cond2 * cond3

    def mouse_pressed(self, event):
        x_mouse, y_mouse = pg.mouse.get_pos()
        cond1 = x_mouse > 80
        cond2 = x_mouse < 262
        cond3 = y_mouse > 350
        cond4 = y_mouse < 562
        # cond5 = pg.mouse.get_pressed()[0]
        cond5 = (event.type == pg.MOUSEBUTTONDOWN and event.button == 1)
        return cond1 * cond2 * cond3 * cond4 * cond5

    def prepare_to_fire(self):
        sling1 = self.level.sling.sling_1
        sling_length = self.level.sling.sling_length

        if self.level.mouse_is_up:
            self.level.mouse_is_up = False
            self.level.number_of_birds -= 1
        mouse = pg.mouse.get_pos()
        direction = sling1 - mouse
        self.level.sling.direction = direction
        mouse_distance = abs(direction)
        unit = direction / mouse_distance
        bird_distance = min(mouse_distance, sling_length)
        bird_position = sling1 - bird_distance * unit
        bird = self.level.birds[self.level.number_of_birds]
        bird.body.position = bird_position
        self.level.sling.sling_end = bird_position - unit * bird.size

    def shot(self):
        bird = self.level.birds[self.level.number_of_birds]
        velocity = self.level.sling.direction * 5

        self.level.sling.reset()
        bird.body.position = self.level.sling.sling_end
        bird.launch(velocity)
        self.level.flying_bird = bird

    #     обработка у каждого объекта состояния, типа нужно удалять или нет - бред
    #     проще всего все основные решения принимать во время коллизий
    #     сейчас реализуется удаление путём списков. Что делать с удалением медленных птичек - хз
    #     если бы мы делали обработку состояния, то не нужно было бы условий life<=0 и т.п.
    #     если делать без обработки, но и без списков, то после условий сразу стояли бы remove

    def post_solve_bird_pig(self, arbiter, space, _):
        # здесь нужно затем продумать, сколько хпшек отнимать в зависимости от силы выстрела
        # и в зависимости от типа объекта. Это тривиальная задача, поэтому до тестировки не прописана

        ev_bird, ev_pig = arbiter.shapes
        for pig in self.level.pigs:
            if pig.body == ev_pig.body:
                pig.life -= 20
                if pig.life <= 0 and pig not in self.level.pigs_to_remove:
                    self.level.pigs_to_remove.append(pig)
                    self.level.score += pig.cost
        for bird in self.level.birds[self.level.number_of_birds:]:
            if bird.body == ev_bird.body:
                bird.life -= 20
                bird.is_flying = False
                if bird.life <= 0 and bird not in self.level.birds_to_remove:
                    self.level.birds_to_remove.append(bird)

    def post_solve_bird_beam(self, arbiter, space, _):
        ev_bird, ev_beam = arbiter.shapes
        for beam in self.level.beams:
            if beam.body == ev_beam.body:
                beam.life -= 20
                if beam.life <= 0:
                    self.level.beams_to_remove.append(beam)
                    self.level.score += beam.cost
        for bird in self.level.birds[self.level.number_of_birds:]:
            if bird.body == ev_bird.body:
                bird.life -= 20
                bird.is_flying = False
                if bird.life <= 0 and bird not in self.level.birds_to_remove:
                    self.level.birds_to_remove.append(bird)

    def post_solve_pig_beam(self, arbiter, space, _):
        ev_pig, ev_beam = arbiter.shapes
        for beam in self.level.beams:
            if beam.body == ev_beam.body:
                beam.life -= 20
                if beam.life <= 0 and beam not in self.level.beams_to_remove:
                    self.level.beams_to_remove.append(beam)
        for pig in self.level.pigs:
            if pig.body == ev_pig.body:
                pig.life -= 20
            if pig.life <= 0 and pig not in self.level.pigs_to_remove:
                self.level.pigs_to_remove.append(pig)

    def post_solve_bird_ground(self, arbiter, space, _):
        ev_bird, ev_ground = arbiter.shapes

        if arbiter.total_impulse.length > 1000 or ev_bird.is_flying:
            for bird in self.level.birds:
                if bird.body == ev_bird.body:
                    if arbiter.total_impulse_length > 1000:
                        bird.life -= 5
                    bird.is_flying = False
                    if bird.life <= 0 and bird not in self.level.birds_to_remove:
                        self.level.birds_to_remove.append(bird)

    def post_solve_pig_ground(self, arbiter, space, _):
        ev_pig, ev_ground = arbiter.shapes
        if arbiter.total_impulse.length > 1000:
            for pig in self.level.pigs:
                if pig.body == ev_pig.body:
                    pig.life -= 5
                    if pig.life <= 0 and pig not in self.level.pigs_to_remove:
                        self.level.pigs_to_remove.append(pig)

    def post_solve_beam_ground(self, arbiter, space, _):
        ev_beam, ev_ground = arbiter.shapes
        if arbiter.total_impulse.length > 1000:
            for beam in self.level.beams:
                if beam.body == ev_beam.body:
                    beam.life -= 5
                    if beam.life <= 0 and beam not in self.level.beams_to_remove:
                        self.level.beams_to_remove.append(beam)


if __name__ == "__main__":
    game = Game()
    game()
