import pygame
import thorpy

"""
def background():
    Background_surf = pygame.image.load('Sprites\\backgroung 1200х900.png')
    Background_rect = Background_surf.get_rect(bottomright = (WIDTH, HEIGHT))
    Kold_surf = pygame.image.load('Sprites\\Kold.png')
    Kold_surf.set_colorkey((255,255,255))
    Kold_rect = Background_surf.get_rect(center=(WIDTH/2+760, 725))
    screen.blit(Background_surf, Background_rect)
    screen.blit(Kold_surf, Kold_rect)


    f1 = pygame.font.Font(None, 60)
    f2 = pygame.font.Font(None, 80)
    text1 = f1.render('Выберите уровень', True, (150,0,0))
    text2 = f2.render('Добро пожаловать в ', True, (255,255,0))
    text3 = f2.render('Phystech.Birds ', True, (255, 255, 0))
    screen.blit(text1, (WIDTH/2-180, HEIGHT/2+80))
    screen.blit(text2, (300, 100))
    screen.blit(text3, (400, 160))


def menu_buttons():
    button_level_1 = thorpy.make_button("Level 1", func=start_level_1)
    button_level_1.set_size((100,50), None, True)
    button_level_1.set_main_color((255,255,255))
    button_level_1.set_font_color((150, 0, 0))
    button_level_1.set_font_size(25)
    button_level_2 = thorpy.make_button("Level 2", func=start_level_2)
    button_level_2.set_size((100,50), None, True)
    button_level_2.set_main_color((255,255,255))
    button_level_2.set_font_color((150, 0, 0))
    button_level_2.set_font_size(25)

    box = thorpy.Box(elements=[
        button_level_1,
        button_level_2])
    box.set_main_color((255, 255, 255))


    menu = thorpy.Menu(box)
    for element in menu.get_population():
        element.surface = screen

    box.set_center((WIDTH/2, HEIGHT/2+180))
    box.blit()
    box.update()
    return menu, box
"""


class OpeningMenu:

    def __init__(self, screen):
        self.sc = screen


class LevelMenu:

    def __init__(self, screen):
        self.sc = screen
