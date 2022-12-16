

import pygame as pg
import thorpy


class OpeningMenu:
    def __init__(self, screen, game_state):
        self.sc = screen
        self.g_s = game_state
        self.w, self.h = self.sc.get_size()
        self.background_surf = pg.image.load('Sprites\\bg for menu 1200x600.png')
        self.play_button = thorpy.make_button("Начать игру", func=self.change_menu)
        self.quit_button = thorpy.make_button("Выход", func=quit)
        self.box = thorpy.Box(elements=[self.play_button, self.quit_button])
        self.menu = thorpy.Menu(self.box)

        for button in [self.play_button, self.quit_button]:
            button.set_size((180, 50))
            button.set_main_color((255, 255, 255))
            button.set_font_color((150, 0, 0))
            button.set_font_size(28)
        thorpy.store(self.box)

    def __call__(self):
        return self.draw()

    def draw(self):
        self.sc.blit(self.background_surf, self.background_surf.get_rect(bottomright=(self.w, self.h)))
        for element in self.menu.get_population():
            element.surface = self.sc
        self.box.blit()
        self.box.update()

    def change_menu(self):
        self.g_s = 0


class LevelMenu:
    def __init__(self, screen, game_state):
        self.sc = screen
        self.g_s = game_state
        self.w, self.h = self.sc.get_size()
        self.background_surf = pg.image.load('Sprites\\bg 1 1200x600.png')
        self.kold_surf = pg.image.load('Sprites\\Kold.png')
        self.level_button_1 = thorpy.make_button("Уровень 1", func=self.choose_option, params={'n': 1})
        self.level_button_2 = thorpy.make_button("Уровень 2", func=self.choose_option, params={'n': 2})
        self.level_button_3 = thorpy.make_button("Уровень 3", func=self.choose_option, params={'n': 3})
        self.level_button_4 = thorpy.make_button("Уровень 4", func=self.choose_option, params={'n': 4})
        self.level_button_5 = thorpy.make_button("Уровень 5", func=self.choose_option, params={'n': 5})
        self.back_button = thorpy.make_button("Назад", func=self.choose_option, params={'n': -1})
        self.box = thorpy.Box(elements=[self.level_button_1, self.level_button_2, self.level_button_3,
                                        self.level_button_4, self.level_button_5, self.back_button])
        self.box.set_size((400, 300))
        self.menu = thorpy.Menu(self.box)

        for button_level in [self.level_button_1, self.level_button_2, self.level_button_3, self.level_button_4,
                             self.level_button_5, self.back_button]:
            button_level.set_size((200, 45), None, True)
            button_level.set_main_color((255, 255, 255))
            button_level.set_font_color((150, 0, 0))
            button_level.set_font_size(25)
        thorpy.store(self.box)

    def __call__(self, *args, **kwargs):
        return self.draw()

    def draw(self):
        self.sc.blit(self.background_surf, self.background_surf.get_rect(bottomright=(self.w, self.h)))
        self.sc.blit(self.kold_surf, (self.w / 2, 0))
        for element in self.menu.get_population():
            element.surface = self.sc
        self.box.set_center((self.w / 2, self.h / 2))
        self.box.blit()
        self.box.update()

    def choose_option(self, n):
        self.g_s = n


