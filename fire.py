import pygame as pg
import pymunk as pm
import pymunk.pygame_util
import birds

pg.init()
clock = pg.time.Clock()
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
WIDTH, HEIGHT = 800, 800

screen = pg.display.set_mode((WIDTH, HEIGHT))
space = pm.Space()
pm.pygame_util.positive_y_is_up = False


class Game:
    FPS = 30
    finished = False
    level_state = True
    sling1_x, sling1_y = 135, 450
    sling2_x, sling2_y = 160, 450
    number_of_birds = 1
    birds_list = [birds.RedBird(700, 700, space)]
    rope_length = 10
    slings = []
    mouse_is_up = True

    def main(self):
        screen.fill(WHITE)
        pg.display.update()
        while not self.finished:
            clock.tick(self.FPS)
            space.step(1 / self.FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.finished = True
                if self.level_state:
                    if self.mouse_pressed() and (self.number_of_birds > 0 or not self.mouse_is_up):
                        self.prepare_to_fire()
                    else:
                        self.slings = []

            screen.fill(WHITE)
            pg.draw.line(screen, (255,0,0), (100, 370),(100, 550), 5)
            pg.draw.line(screen, (255, 0,0), (250, 370), (250, 550), 5)
            pg.draw.line(screen, (255, 0, 0), (100, 370), (250, 370), 5)
            pg.draw.line(screen, (255, 0, 0), (100, 550), (250, 550), 5)
            if self.level_state:
                for bird in self.birds_list:
                    bird.draw(screen)
                if self.slings:
                    pg.draw.line(screen, (0, 0, 0), (self.slings[0][0], self.slings[0][1]),
                                 (self.sling1_x, self.sling1_y), 5)
                    pg.draw.line(screen, (0, 0, 0), (self.slings[1][0], self.slings[1][1]),
                                 (self.sling1_x, self.sling1_y), 5)
            pg.display.update()

    def mouse_pressed(self):
        '''ЛКМ нажата в нужном месте экрана'''
        x_mouse, y_mouse = pg.mouse.get_pos()
        cond1 = x_mouse > 100
        cond2 = x_mouse < 250
        cond3 = y_mouse > 370
        cond4 = y_mouse < 550
        cond5 = pg.mouse.get_pressed()[0]
        return cond1 * cond2 * cond3 * cond4 * cond5

    def prepare_to_fire(self):
        if self.mouse_is_up:
            self.mouse_is_up = False
            self.number_of_birds -= 1
        x_mouse, y_mouse = pg.mouse.get_pos()
        direction = pm.Vec2d(self.sling1_x - x_mouse, self.sling1_y - y_mouse)
        mouse_distance = abs(direction)
        bird_distance = min(self.rope_length, mouse_distance)
        similarity_factor = bird_distance / mouse_distance
        bird = self.birds_list[self.number_of_birds]
        bird_x = similarity_factor * x_mouse  # возможно, здесь из-за левого верхнего угла была добавка
        bird_y = similarity_factor * y_mouse  # если что для модуля bird используем другие к-ты, а эти
        # оставим рабочими
        bird.body.x, bird.body.y = bird_x, bird_y
        # очень кринжовые вычисления. Можно немного оптимизировать, но суть верна.
        unit_x = bird_x / bird_distance
        unit_y = bird_y / bird_distance
        sling1_end = sling2_end = (bird_x - unit_x * bird.size, bird_y - unit_y * bird.size)
        self.slings = [sling1_end, sling2_end]


g = Game()
g.main()
pg.quit()
