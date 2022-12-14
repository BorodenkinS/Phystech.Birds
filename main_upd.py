# Поменять в main
'''
1) HEIGHT = 600
2) Вставить в gameloop:

- в цикл обработки событий:
                    if self.level_state: (здесь параметр, определяющий, что запущен режим "уровень"
                    if (self.mouse_pressed() and self.number_of_birds > 0) or not self.mouse_is_up:
                        self.prepare_to_fire()
                    else:
                        self.slings_ends = []
- в основной цикл:
           -добавить сверху:
               clock.tick(self.FPS)
               space.step(1 / self.FPS)
           -добавить после обработки событий:
            screen.fill(WHITE)
            if self.level_state:
                for bird in self.birds_list:
                    bird.draw(screen)
                if self.slings_ends:
                    pg.draw.line(screen, (0, 0, 0), (self.slings_ends[0]), (self.sling1), 5)
                    pg.draw.line(screen, (0, 0, 0), (self.slings_ends[1]), (self.sling2), 5)
            pg.display.update()

Что должно быть прописано в уровне:
    sling1 = pm.Vec2d(135, 412)
    sling2 = pm.Vec2d(160, 412)
    number_of_birds = ...
    birds_list = [birds.RedBird(...,..., space)]
    rope_length = 100
    slings_ends = []
У меня это используется как атрибуты в Game

Что должно быть добавлено в game:
self.mouse_is_up = True

Методы, которые добавляются целиком:
    def mouse_pressed(self):
        x_mouse, y_mouse = pg.mouse.get_pos()
        cond1 = x_mouse > 80
        cond2 = x_mouse < 262
        cond3 = y_mouse > 350
        cond4 = y_mouse < 562
        cond5 = pg.mouse.get_pressed()[0]
        return cond1 * cond2 * cond3 * cond4 * cond5

    def prepare_to_fire(self):
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
'''
