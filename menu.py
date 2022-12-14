# Здесь меню
import thorpy
from level import *
'Кринге левель хэс бин дикрисед ту фифти персентс'

class OpeningMenu:
    def __init__(self,screen):
        self.screen = screen
        self.menu = thorpy.Menu()
        self.background_surf = pygame.image.load('Sprites\\backgroung 1200х900.png')
        self.draw_background()
        self.menu_buttons()
        self.menu_text()

    def draw_background(self):
        background_rect = self.background_surf.get_rect(bottomright=(WIDTH, HEIGHT))
        self.screen.blit(self.background_surf, background_rect)

    def menu_text(self):
        f = pygame.font.Font(None, 80)
        text1 = f.render('Добро пожаловать в ', True, (255,255,0))
        text2 = f.render('Phystech.Birds ', True, (255, 255, 0))
        self.screen.blit(text1, (300, 100))
        self.screen.blit(text2, (400, 160))


    def menu_buttons(self):
        button_to_level_choose = thorpy.make_button("Начать игру", func=self.change_menu)
        button_quit = thorpy.make_button("Quit", func=quit)
        for button in [button_to_level_choose, button_quit]:
            button.set_size((180, 50), None, True)
            button.set_main_color((255, 255, 255))
            button.set_font_color((150, 0, 0))
            button.set_font_size(28)


        self.box = thorpy.Box(elements=[button_to_level_choose, button_quit])
        self.box.set_main_color((255, 255, 255))

        self.menu = thorpy.Menu(self.box)
        for element in self.menu.get_population():
            element.surface = self.screen

        self.box.set_center((WIDTH / 2, HEIGHT / 2 ))
        self.box.blit()
        self.box.update()


    def change_menu(self):
        self.menu.remove_from_population(self.box)
        LevelMenu(screen)


class LevelMenu:
    def __init__(self,screen):
        self.screen = screen
        self.menu = thorpy.Menu()
        self.background_surf = pygame.image.load('Sprites\\backgroung 1200х900.png')
        self.kold_surf = pygame.image.load('Sprites\\Kold.png')
        self.draw_background()
        self.menu_text()
        self.menu_buttons()

    def draw_background(self):
        background_rect = self.background_surf.get_rect(bottomright=(WIDTH, HEIGHT))
        self.kold_surf.set_colorkey((255,255,255))
        kold_rect = self.background_surf.get_rect(center=(WIDTH / 2 + 480, 725))
        self.screen.blit(self.background_surf, background_rect)
        self.screen.blit(self.kold_surf, kold_rect)

    def menu_text(self):
        f1 = pygame.font.Font(None, 60)
        f2 = pygame.font.Font(None, 80)
        text1 = f1.render('Выберите уровень', True, (150,0,0))
        text2 = f2.render('Добро пожаловать в ', True, (255,255,0))
        text3 = f2.render('Phystech.Birds ', True, (255, 255, 0))
        self.screen.blit(text1, (WIDTH/2-180, HEIGHT/2+80))
        self.screen.blit(text2, (300, 100))
        self.screen.blit(text3, (400, 160))

    def menu_buttons(self):
        button_level_1 = thorpy.make_button("Level 1", func=level1)
        button_level_2 = thorpy.make_button("Level 2", func=level2)
        button_level_3 = thorpy.make_button("Level 3", func=level3)
        button_level_4 = thorpy.make_button("Level 4", func=level4)
        button_level_5 = thorpy.make_button("Level 5", func=level5)
        for button_level in [button_level_1, button_level_2, button_level_3,
                             button_level_4, button_level_5]:
            button_level.set_size((100, 45), None, True)
            button_level.set_main_color((255, 255, 255))
            button_level.set_font_color((150, 0, 0))
            button_level.set_font_size(25)

        box = thorpy.Box(elements=[
            button_level_1,
            button_level_2,
            button_level_3,
            button_level_4,
            button_level_5])
        box.set_main_color((255, 255, 255))


        self.menu = thorpy.Menu(box)
        for element in self.menu.get_population():
            element.surface = self.screen


        box.set_center((WIDTH/2, HEIGHT/2+250))
        box.blit()
        box.update()
        button_level_2 = thorpy.make_button("Level 2", func=level2)
        button_level_3 = thorpy.make_button("Level 3", func=level3)
        button_level_4 = thorpy.make_button("Level 4", func=level4)
        button_level_5 = thorpy.make_button("Level 5", func=level5)
        for button_level in [button_level_1, button_level_2, button_level_3,
                             button_level_4, button_level_5]:
            button_level.set_size((100, 45), None, True)
            button_level.set_main_color((255, 255, 255))
            button_level.set_font_color((150, 0, 0))
            button_level.set_font_size(25)

        box = thorpy.Box(elements=[
            button_level_1,
            button_level_2,
            button_level_3,
            button_level_4,
            button_level_5])
        box.set_main_color((255, 255, 255))
        self.menu = thorpy.Menu(box)
        for element in self.menu.get_population():
            element.surface = self.screen

        box.set_center((WIDTH/2, HEIGHT/2+250))
        box.blit()
        box.update()

class LevelMenu():
    def __init__(self, screen):
        self.screen = screen
        self.menu1 = thorpy.Menu()
        self.menu2 = thorpy.Menu()
        self.kold_surf = pygame.image.load('Sprites\\Kold.png')
        self.Menu_draw()
        self.Menu_buttons()


    def Menu_draw(self):
        pygame.draw.rect(self.screen, (255,255,255),(450,220,310,380))
        self.kold_surf.set_colorkey((255,255,255))
        kold_rect = self.screen.get_rect(center=(WIDTH / 2 + 480, 725))
        self.screen.blit(self.kold_surf, kold_rect)
        f = pygame.font.Font(None, 60)
        text = f.render('ПАУЗА', True, (150, 0, 0))
        self.screen.blit(text, (WIDTH / 2 - 75, 235))

    def Menu_buttons(self):
        button_restart = thorpy.make_button("Restart", func=level1)
        button_quit = thorpy.make_button("Quit", func=quit)
        for button in [button_restart, button_quit]:
            button.set_size((100, 45), None, True)
            button.set_main_color((255, 255, 255))
            button.set_font_color((150, 0, 0))
            button.set_font_size(25)

        box1 = thorpy.Box(elements=[button_restart])
        box1.set_main_color((255, 255, 255))
        box2 = thorpy.Box(elements=[button_quit])
        box2.set_main_color((255, 255, 255))
        self.menu1 = thorpy.Menu(box1)
        for element in self.menu1.get_population():
            element.surface = self.screen
        self.menu2 = thorpy.Menu(box2)
        for element in self.menu2.get_population():
            element.surface = self.screen

        box1.set_center((WIDTH / 2-80, HEIGHT / 2 + 120))
        box1.blit()
        box1.update()
        box2.set_center((WIDTH / 2 + 80 , HEIGHT / 2 + 120))
        box2.blit()
        box2.update()
