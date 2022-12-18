import sys
import pygame as pg
import pymunk as pm
from pymunk import pygame_util
from level import *
from birds import *
from pigs import *
from obstructions import *

pymunk.pygame_util.positive_y_is_up = False


class Game:
    WIDTH = 1200
    HEIGHT = 600
    FPS = 60

    def __init__(self):
        self.display = pg.display
        self.sc = self.display.set_mode((Game.WIDTH, Game.HEIGHT))
        self.icon = pg.image.load("Sprites\\cat dgap.ico")
        self.display.set_icon(self.icon)
        self.clock = pg.time.Clock()
        self.draw_options = pygame_util.DrawOptions(self.sc)
        self.space = pymunk.Space()
        self.space.gravity = 0, 1000

        self.game_state = -1
        self.level = Level(self.space, self.sc)

        self.display.set_caption("Phystech.Birds")

        self.space.add_collision_handler(0, 1).post_solve = self.post_solve_bird_pig
        self.space.add_collision_handler(0, 2).post_solve = self.post_solve_bird_beam
        self.space.add_collision_handler(1, 2).post_solve = self.post_solve_pig_beam
        self.space.add_collision_handler(0, 3).post_solve = self.post_solve_bird_ground
        self.space.add_collision_handler(0, 0).post_solve = self.post_solve_bird_bird
        self.space.add_collision_handler(1, 1).post_solve = self.post_solve_pig_pig
        self.space.add_collision_handler(2, 2).post_solve = self.post_solve_beam_beam

        self.start_level = [self.start_level_1, self.start_level_2, self.start_level_3, self.start_level_4,
                            self.start_level_5]

        pg.init()

    def __call__(self, *args, **kwargs):
        return self.gameloop()

    def mark(self):
        if self.level.score + 100 * len(self.level.birds) <= 0.3 * self.level.max_score:
            return "УД"
        elif 0.3 * self.level.max_score < self.level.score + 100 * len(self.level.birds) <= 0.8 * self.level.max_score:
            return "ХОР"
        else:
            return "ОТЛ"

    def opening_menu(self):
        self.sc.fill((255, 255, 255))

    def level_menu(self):
        self.sc.fill((255, 0, 255))
        self.sc.blit(pg.image.load("Sprites\\bg for menu 1200x600.png"), (0, 0))

    def lost(self):
        img = pg.image.load("Sprites\\Kold.png")
        font = pg.font.Font(None, 48)
        lose_text = font.render('ПЕРЕСДАЧА!!!', True, (0, 0, 255))
        self.sc.blit(img, (Game.WIDTH / 2 - img.get_size()[0] / 2, Game.HEIGHT / 2 - img.get_size()[1] / 2))
        self.sc.blit(lose_text, (Game.WIDTH / 2 - img.get_size()[0] / 2, Game.HEIGHT / 2 + img.get_size()[1] / 2))

    def win(self):
        img = pg.image.load("Sprites\\Kold.png")
        font = pg.font.Font(None, 48)
        win_text = font.render(self.mark() + str(self.level.score), True, (0, 0, 255))
        self.sc.blit(img, (Game.WIDTH / 2 - img.get_size()[0] / 2, Game.HEIGHT / 2 - img.get_size()[1] / 2))
        self.sc.blit(win_text,
                     (Game.WIDTH / 2 - img.get_size()[0] / 2 + 40, Game.HEIGHT / 2 + img.get_size()[1] / 2))

    def gameloop(self):
        finished = False
        while not finished:
            self.clock.tick(self.FPS)
            self.space.step(1 / self.FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT or event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                    finished = True

                if self.game_state > 0:
                    if self.mouse_pressed(event) and self.level.number_of_birds > 0 or not self.level.mouse_is_up:
                        self.prepare_to_fire()
                    if self.level.flying_bird:
                        if self.mouse_pressed2(event):
                            self.level.flying_bird.bird_function()
                    if event.type == pg.MOUSEBUTTONUP and event.button == 1 and not self.level.mouse_is_up:
                        self.level.mouse_is_up = True
                        self.shot()

                if event.type == pg.KEYDOWN:
                    if self.game_state == -1 and event.key == pg.K_RETURN:
                        self.game_state = 0
                    elif self.game_state == 0 and event.key in [pg.K_1, pg.K_2, pg.K_3, pg.K_4,
                                                                pg.K_5]:
                        keys = {pg.K_1: 1, pg.K_2: 2, pg.K_3: 3, pg.K_4: 4, pg.K_5: 5}
                        self.game_state = keys[event.key]
                        self.start_level[self.game_state-1]()

                    elif self.game_state == 0 and event.key == pg.K_BACKSPACE:
                        self.game_state = -1
                    elif self.game_state > 0 and event.key == pg.K_BACKSPACE:
                        self.game_state = 0

            if self.game_state == -1:
                self.opening_menu()
            elif self.game_state == 0:
                self.level_menu()
            else:
                self.re_calculator()
                self.drawer()
                if len(self.level.birds) == 0 and len(self.level.pigs) != 0:
                    self.lost()
                if len(self.level.birds) >= 0 and len(self.level.pigs) == 0:
                    self.win()
            self.display.update()

        sys.exit()

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
        text_score = pg.font.Font(None, 36)
        score = text_score.render(('SCORE: ' + str(self.level.score)), True, (255, 0, 0))
        self.sc.blit(score, (100, 50))
        for bird in self.level.birds:
            bird.draw()
        for pig in self.level.pigs:
            pig.draw()
        for beam in self.level.beams:
            beam.draw()
        self.level.sling.draw()


    def re_calculator(self):
        for bird in self.level.birds:
            if not bird.recalculate_state():
                self.level.birds.remove(bird)
        for pig in self.level.pigs:
            if not pig.recalculate_state():
                self.level.pigs.remove(pig)
                self.level.score += pig.cost
        for beam in self.level.beams:
            if not beam.recalculate_state():
                self.level.beams.remove(beam)
                self.level.score += beam.cost

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
        cond1 = x_mouse >= 235
        cond2 = y_mouse <= 397
        cond3 = (event.type == pg.MOUSEBUTTONDOWN and event.button == 1)
        return cond1 * cond2 * cond3

    def mouse_pressed(self, event):
        x_mouse, y_mouse = pg.mouse.get_pos()
        cond1 = x_mouse > 80
        cond2 = x_mouse < 262
        cond3 = y_mouse > 350
        cond4 = y_mouse < 562
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
        velocity = self.level.sling.direction * 8

        self.level.sling.reset()
        bird.body.position = self.level.sling.sling_end
        bird.launch(velocity)
        self.level.flying_bird = bird

    def post_solve_bird_pig(self, arbiter, space, _):
        ev_bird_shape, ev_pig_shape = arbiter.shapes
        for pig in self.level.pigs:
            if pig.body == ev_pig_shape.body:
                pig.life -= 10
        for bird in self.level.birds[self.level.number_of_birds:]:
            if bird.body == ev_bird_shape.body:
                bird.life -= 1
                bird.is_flying = False

    def post_solve_bird_beam(self, arbiter, space, _):
        if arbiter.total_impulse.length > 700:
            ev_bird_shape, ev_beam_shape = arbiter.shapes
            for beam in self.level.beams:
                if beam.body == ev_beam_shape.body:
                    beam.life -= 1
            for bird in self.level.birds[self.level.number_of_birds:]:
                if bird.body == ev_bird_shape.body:
                    bird.life -= 1
                    bird.is_flying = False

    def post_solve_pig_beam(self, arbiter, space, _):
        if arbiter.total_impulse.length > 700:
            ev_pig_shape, ev_beam_shape = arbiter.shapes
            for beam in self.level.beams:
                if beam.body == ev_beam_shape.body:
                    beam.life -= 1
            for pig in self.level.pigs:
                if pig.body == ev_beam_shape.body:
                    pig.life -= 10

    def post_solve_bird_ground(self, arbiter, space, _):
        ev_bird_shape, ev_ground_shape = arbiter.shapes

        for bird in self.level.birds:
            if bird.body == ev_bird_shape.body:
                bird.is_flying = False

    def post_solve_bird_bird(self, arbiter, space, _):
        ev_bird_shape1, ev_bird_shape2 = arbiter.shapes
        for bird in self.level.birds:
            if bird.body == ev_bird_shape1.body:
                ev_bird1 = bird
                bird.is_flying = False
            if bird.body == ev_bird_shape2.body:
                ev_bird2 = bird
                bird.is_flying = False
        if arbiter.total_impulse.length > 500:
            ev_bird1.life -= 1
            ev_bird2.life -= 1

    def post_solve_pig_pig(self, arbiter, space, _):
        ev_pig_shape1, ev_pig_shape2 = arbiter.shapes
        for pig in self.level.pigs:
            if pig.body == ev_pig_shape1.body:
                ev_pig1 = pig
            if pig.body == ev_pig_shape2.body:
                ev_pig2 = pig
                pig.is_flying = False
        if arbiter.total_impulse.length > 500:
            ev_pig1.life -= 1
            ev_pig2.life -= 1

    def post_solve_beam_beam(self, arbiter, space, _):
        ev_beam_shape1, ev_beam_shape2 = arbiter.shapes
        for beam in self.level.beams:
            if beam.body == ev_beam_shape1.body:
                ev_beam1 = beam
            if beam.body == ev_beam_shape2.body:
                ev_beam2 = beam
        if arbiter.total_impulse.length > 500:
            ev_beam1.life -= 1
            ev_beam2.life -= 1


if __name__ == "__main__":
    game = Game()
    game()
