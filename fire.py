import pygame as pg
import pymunk as pm
import pymunk.pygame_util
import birds

pg.init()
clock = pg.time.Clock()
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
WIDTH, HEIGHT = 1200, 800

screen = pg.display.set_mode((WIDTH, HEIGHT))
space = pm.Space()
pm.pygame_util.positive_y_is_up = False


class Game:
    FPS = 60
    finished = False
    level_state = True
    sling1 = pm.Vec2d(135, 550)
    sling2 = pm.Vec2d(160, 550)
    number_of_birds = 1
    birds_list = [birds.RedBird(700, 700, space)]
    rope_length = 100
    slings_ends = []
    mouse_is_up = True

    def main(self):
        while not self.finished:
            clock.tick(self.FPS)
            space.step(1 / self.FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.finished = True
                if self.level_state:
                    if (self.mouse_pressed() and self.number_of_birds > 0) or not self.mouse_is_up:
                        self.prepare_to_fire2()
                    else:
                        self.slings_ends = []

            screen.fill(WHITE)
            if self.level_state:
                for bird in self.birds_list:
                    bird.draw(screen)
                if self.slings_ends:
                    pg.draw.line(screen, (0, 0, 0), (self.slings_ends[0]), (self.sling1), 5)
                    pg.draw.line(screen, (0, 0, 0), (self.slings_ends[1]), (self.sling2), 5)
            pg.display.update()

    def mouse_pressed(self):
        '''ЛКМ нажата в нужном месте экрана'''
        x_mouse, y_mouse = pg.mouse.get_pos()
        cond1 = x_mouse > 80
        cond2 = x_mouse < 250
        cond3 = y_mouse > 350
        cond4 = y_mouse < 750
        cond5 = pg.mouse.get_pressed()[0]
        return cond1 * cond2 * cond3 * cond4 * cond5

    def prepare_to_fire2(self):
        if self.mouse_is_up:
            self.mouse_is_up = False
            self.number_of_birds -= 1
        mouse = pg.mouse.get_pos()
        direction = self.sling1 - mouse
        mouse_distance = abs(direction)
        unit = direction / mouse_distance
        bird_distance = min(mouse_distance, self.rope_length)
        bird_position = self.sling1 - bird_distance * unit
        bird = self.birds_list[self.number_of_birds]
        bird.body.position = bird_position
        sling1_end = sling2_end = bird_position - unit * bird.size
        self.slings_ends = [sling1_end, sling2_end]


g = Game()
g.main()
pg.quit()
