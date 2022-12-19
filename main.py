import sys
import pygame as pg
import pymunk as pm
from pymunk import pygame_util
from level import *
from birds import *
from pigs import *
from obstructions import *

pygame_util.positive_y_is_up = False


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
        self.space = pm.Space()
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

        self.scores = [0] * 5

        pg.init()

    def __call__(self, *args, **kwargs):
        return self.gameloop()

    def mark(self):
        """Оценка - аналог звёздочкам, получаемым за прохождение уровня в оригинальной игре"""
        if self.level.score + 100 * len(self.level.birds) <= 0.3 * self.level.max_score:
            return "УД "
        elif 0.3 * self.level.max_score < self.level.score + 100 * len(self.level.birds) <= 0.8 * self.level.max_score:
            return "ХОР "
        else:
            return "ОТЛ "

    def opening_menu(self):
        """Функция вызова начального меню"""
        self.sc.blit(pg.image.load("Sprites\\start cringe menu.png"), (0, 0))
        font = pg.font.Font(None, 36)
        play_text = font.render('Чтобы начать нажмите Enter', True, (12, 101, 171))
        back_text = font.render('Для выхода нажмите Escape', True, (12, 101, 171))
        self.sc.blit(play_text, (Game.WIDTH / 2 - 200, 480))
        self.sc.blit(back_text, (Game.WIDTH / 2 - 200, 510))

    def level_menu(self):
        """Функция вызова меню выбора уровня с показателем текущего рекорда по очкам на каждм уровне"""
        self.sc.fill((0, 0, 0))
        self.sc.blit(pg.image.load("Sprites\\bg for menu 1200x600.png"), (0, 0))
        font = pg.font.Font(None, 48)
        surfs = [pg.image.load("Sprites\\bg " + str(i) + " 216x450.png") for i in range(1, 6)]
        for i in range(5):
            self.sc.blit(surfs[i], (20 + 236 * i, 30))
            text = font.render('Нажмите ' + str(i + 1), True, (0, 0, 0))
            temp_surface = pg.Surface(text.get_size())
            temp_surface.fill((255, 255, 255))
            temp_surface.blit(text, (0, 0))
            self.sc.blit(temp_surface, (44 + 236 * i, 500))
            if self.scores[i] != 0:
                score_text = font.render(str(self.scores[i]), True, (0, 0, 0))
                temp_surface_ = pg.Surface(score_text.get_size())
                temp_surface_.fill((255, 255, 255))
                temp_surface_.blit(score_text, (0, 0))
                self.sc.blit(temp_surface_, (110 + 236 * i, 450))
        font_back = pg.font.Font(None, 20)
        text_back = font_back.render('Для возврата нажмите backspace', True, (0, 0, 0))
        back_surface = pg.Surface(text_back.get_size())
        back_surface.fill((255, 255, 255))
        back_surface.blit(text_back, (0, 0))
        self.sc.blit(back_surface, (20, 550))

    def lost(self):
        """Выводится при проигрыше, то есть когда остаются живые свинки, но все птицы потрачены"""
        img = pg.image.load("Sprites\\Kold.png")
        font = pg.font.Font(None, 48)
        lose_text = font.render('ПЕРЕСДАЧА!!!', True, (0, 0, 255))
        self.sc.blit(img, (Game.WIDTH / 2 - img.get_size()[0] / 2, Game.HEIGHT / 2 - img.get_size()[1] / 2))
        self.sc.blit(lose_text, (Game.WIDTH / 2 - img.get_size()[0] / 2, Game.HEIGHT / 2 + img.get_size()[1] / 2))

    def win(self):
        """Выводится при победе, то есть когда все свинки убиты"""
        img = pg.image.load("Sprites\\Kold.png")
        font = pg.font.Font(None, 48)
        win_text = font.render(self.mark() + str(self.level.score), True, (0, 0, 255))
        self.sc.blit(img, (Game.WIDTH / 2 - img.get_size()[0] / 2, Game.HEIGHT / 2 - img.get_size()[1] / 2))
        self.sc.blit(win_text, (Game.WIDTH / 2 - img.get_size()[0] / 2 + 40, Game.HEIGHT / 2 + img.get_size()[1] / 2))
        self.scores[self.game_state - 1] = self.level.score

    def drawer(self):
        """Функция отрисовки объектов на уровне"""
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
        """Функция, обрабатывающая состояние объектов (птиц, балок, свинок)"""
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

    @staticmethod
    def mouse_pressed2(event):
        """Впомогательная функция (расширенная обработка нажатия кнопки мыши - вне зоны рогатки)"""
        x_mouse, y_mouse = pg.mouse.get_pos()
        cond1 = x_mouse >= 235
        cond2 = y_mouse <= 397
        cond3 = (event.type == pg.MOUSEBUTTONDOWN and event.button == 1)
        return cond1 * cond2 * cond3

    @staticmethod
    def mouse_pressed(event):
        """Впомогательная функция (расширенная обработка нажатия кнопки мыши - зона рогатки)"""
        x_mouse, y_mouse = pg.mouse.get_pos()
        cond1 = x_mouse > 80
        cond2 = x_mouse < 262
        cond3 = y_mouse > 350
        cond4 = y_mouse < 562
        cond5 = (event.type == pg.MOUSEBUTTONDOWN and event.button == 1)
        return cond1 * cond2 * cond3 * cond4 * cond5

    def prepare_to_fire(self):
        """Подгтовка к запуску птицы из рогатки"""
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
        """Выстрел птичкой - сообщение ей скорости"""
        bird = self.level.birds[self.level.number_of_birds]
        velocity = self.level.sling.direction * 8

        self.level.sling.reset()
        bird.body.position = self.level.sling.sling_end
        bird.launch(velocity)
        self.level.flying_bird = bird

    def post_solve_bird_pig(self, arbiter, space, _):
        """Обработка столкновения между птичкой и свинкой"""
        ev_bird_shape, ev_pig_shape = arbiter.shapes
        impulse = arbiter.total_impulse.length
        for pig in self.level.pigs:
            if pig.body == ev_pig_shape.body:
                pig.life -= 5 * impulse / 600
        for bird in self.level.birds[self.level.number_of_birds:]:
            if bird.body == ev_bird_shape.body:
                bird.is_flying = False
                bird.life -= 5 * impulse / 600

    def post_solve_bird_beam(self, arbiter, space, _):
        """Обработка столкновения между птичкой и балкой"""
        ev_bird_shape, ev_beam_shape = arbiter.shapes
        impulse = arbiter.total_impulse.length
        if impulse > 600:
            for beam in self.level.beams:
                if beam.body == ev_beam_shape.body:
                    beam.life -= 7 * impulse / 600
            for bird in self.level.birds[self.level.number_of_birds:]:
                if bird.body == ev_bird_shape.body:
                    bird.is_flying = False
                    bird.life -= 5 * impulse / 600

    def post_solve_pig_beam(self, arbiter, space, _):
        """Обработка столкновения между балкой и свинкой"""
        ev_pig_shape, ev_beam_shape = arbiter.shapes
        impulse = arbiter.total_impulse.length
        if impulse > 1200:
            for beam in self.level.beams:
                if beam.body == ev_beam_shape.body:
                    beam.life -= 0.5 * impulse / 600
        for pig in self.level.pigs:
            if pig.body == ev_beam_shape.body:
                pig.life -= 0.5 * impulse / 600

    def post_solve_bird_ground(self, arbiter, space, _):
        """Обработка столкновения птички с землёй"""
        ev_bird_shape, ev_ground_shape = arbiter.shapes

        for bird in self.level.birds:
            if bird.body == ev_bird_shape.body:
                bird.is_flying = False

    def post_solve_bird_bird(self, arbiter, space, _):
        """Обработка столкновения птицы с птицей"""
        ev_bird_shape1, ev_bird_shape2 = arbiter.shapes
        impulse = arbiter.total_impulse.length
        for bird in self.level.birds:
            if bird.body == ev_bird_shape1.body:
                bird.is_flying = False
                bird.life -= 0.5 * impulse / 600
            if bird.body == ev_bird_shape2.body:
                bird.is_flying = False
                bird.life -= 0.5 * impulse / 600

    def post_solve_pig_pig(self, arbiter, space, _):
        """Обработка столкновения свинки со свинкой"""
        ev_pig_shape1, ev_pig_shape2 = arbiter.shapes
        impulse = arbiter.total_impulse.length
        for pig in self.level.pigs:
            if pig.body == ev_pig_shape1.body:
                pig.life -= 0.5 * impulse / 600
            if pig.body == ev_pig_shape2.body:
                pig.life -= 0.5 * impulse / 600

    def post_solve_beam_beam(self, arbiter, space, _):
        """Обработка столкновения балки с балкой"""
        ev_beam_shape1, ev_beam_shape2 = arbiter.shapes
        impulse = arbiter.total_impulse.length
        if impulse > 1200:
            for beam in self.level.beams:
                if beam.body == ev_beam_shape1.body:
                    beam.life -= 0.5 * impulse / 600
                if beam.body == ev_beam_shape2.body:
                    beam.life -= 0.5 * impulse / 600

    def gameloop(self):
        """Основной игровой цикл собработками всех нажатий, вызовом всех отрисовывающих функций"""
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
                        # self.start_level[self.game_state - 1]()
                        self.level.levels[self.game_state - 1]()
                    elif self.game_state == 0 and event.key == pg.K_BACKSPACE:
                        self.game_state = -1
                    elif self.game_state > 0 and event.key == pg.K_BACKSPACE:
                        self.game_state = 0

                    elif self.game_state > 0 and event.key == pg.K_r:
                        self.level.levels[self.game_state - 1]()

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


if __name__ == "__main__":
    game = Game()
    game()
