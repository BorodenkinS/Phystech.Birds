import pymunk as pm
import pygame as pg
from birds import *
from pigs import *
from obstructions import *


class Level:
    

    def __init__(self, space, screen):
        self.birds = []
        self.pigs = []
        self.obstructions = []
        self.number_of_birds = 0
        self.mouse_is_up = True
        self.pigs_to_remove = []
        self.birds_to_remove = []
        self.beams_to_remove = []
        self.score = 0
        self.sc = screen
        self.space = space
        self.levels = [self.level1, self.level2, self.level3, self.level4, self.level5]
        self.sling = Sling(self.sc)
        self.sling.position = (120, 510)


    def level1(self):
        # проработать механизм удаления прошлых объектов.
        # просто заносить в список на удаление, наверное, недостаточно, ибо функция удаления сработает позже
        # создания новых объектов
        background_surf = pygame.image.load('Sprites\\bg 1 1200x600.png')
        ground_surf = pygame.image.load('Sprites\\grass.png')
        self.sc.blit(background_surf, background_surf.get_rect(bottomright=(1200,600)))
        self.sc.blit(ground_surf, ground_surf.get_rect(bottomright=(1200, 600)))

        self.obstructions = [WoodBeam(1050, 475, False, self.space, self.sc),
                             WoodBeam(1000, 475, False, self.space, self.sc),
                             WoodBeam(1025, 420, True, self.space, self.sc),
                             WoodBeam(920, 475, False, self.space, self.sc),
                             WoodBeam(870, 475, False, self.space, self.sc),
                             WoodBeam(895, 420, True, self.space, self.sc),
                             WoodBeam(720, 475, False, self.space, self.sc),
                             WoodBeam(670, 475, False, self.space, self.sc),
                             WoodBeam(695, 420, True, self.space, self.sc)]
        for beam in self.obstructions:
            beam.draw()

        self.pigs = [DefaultPig(1025, 400, self.space, self.sc),
                     DefaultPig(895, 400, self.space, self.sc),
                     DefaultPig(695, 400, self.space, self.sc)]


        self.birds = [RedBird(100, 510, self.space, self.sc),
                      RedBird(75, 510, self.space, self.sc),
                      RedBird(50, 510, self.space, self.sc),
                      RedBird(25, 510, self.space, self.sc)]
        self.number_of_birds = 4


    def level2(self):
        background_surf = pygame.image.load('Sprites\\bg 2 1200x600.png')
        ground_surf = pygame.image.load('Sprites\\grass.png')
        self.sc.blit(background_surf, background_surf.get_rect(bottomright=(1200, 600)))
        self.sc.blit(ground_surf, ground_surf.get_rect(bottomright=(1200, 600)))

        self.obstructions = [WoodBeam(905, 475, False, self.space, self.sc),
                             WoodBeam(995, 475, False, self.space, self.sc),
                             WoodBeam(950, 420, True, self.space, self.sc),
                             WoodBeam(905, 365, False, self.space, self.sc),
                             WoodBeam(995, 365, False, self.space, self.sc),
                             WoodBeam(950, 310, True, self.space, self.sc),
                             GlassBeam(890, 475, False, self.space, self.sc),
                             GlassBeam(800, 475, False, self.space, self.sc),
                             GlassBeam(845, 420, True, self.space, self.sc)]

        self.pigs = [DefaultPig(950, 400, self.space, self.sc),
                     DefaultPig(845, 510, self.space, self.sc),
                     KingPig(950, 495, self.space, self.sc)]


        self.birds = [TriangleBird(100, 511, self.space, self.sc),
                      TriangleBird(75, 511, self.space, self.sc),
                      RedBird(25, 510, self.space, self.sc),
                      RedBird(25, 510, self.space, self.sc)]
        self.number_of_birds = 4

    def level3(self):
        background_surf = pygame.image.load('Sprites\\bg 3 1200x600.png')
        ground_surf = pygame.image.load('Sprites\\grass.png')
        self.sc.blit(background_surf, background_surf.get_rect(bottomright=(1200, 600)))
        self.sc.blit(ground_surf, ground_surf.get_rect(bottomright=(1200, 600)))

        self.obstructions = [WoodBeam(905, 475, False, self.space, self.sc),
                             WoodBeam(995, 475, False, self.space, self.sc),
                             GlassBeam(950, 420, True, self.space, self.sc),
                             WoodBeam(890, 475, False, self.space, self.sc),
                             WoodBeam(800, 475, False, self.space, self.sc),
                             GlassBeam(845, 420, True, self.space, self.sc),
                             WoodBeam(1010, 475, False, self.space, self.sc),
                             WoodBeam(1100, 475, False, self.space, self.sc),
                             GlassBeam(1055, 420, True, self.space, self.sc),
                             WoodBeam(960, 365, False, self.space, self.sc),
                             WoodBeam(1050, 365, False, self.space, self.sc),
                             GlassBeam(1005, 310, True, self.space, self.sc),
                             WoodBeam(850, 365, False, self.space, self.sc),
                             WoodBeam(940, 365, False, self.space, self.sc),
                             GlassBeam(890, 310, True, self.space, self.sc),
                             WoodBeam(910, 255, False, self.space, self.sc),
                             WoodBeam(1000, 255, False, self.space, self.sc),
                             GlassBeam(955, 200, True, self.space, self.sc)
                             ]


        self.pigs = [DefaultPig(845, 510, self.space, self.sc),
                     DeafultPig(950, 510, self.space, self.sc),
                     DefaultPig(1050, 510, self.space, self.sc),
                     DefaultPig(1000, 400, self.space, self.sc),
                     DefaultPig(890, 400, self.space, self.sc),
                     DefaultPig(950, 290, self.space, self.sc)]


        self.birds = [BigBird(100, 495, self.space, self.sc),
                      BigBird(65, 495, self.space, self.sc),
                      RedBird(20, 510, self.space, self.sc)]
        self.number_of_birds = 3


    def level4(self):
        background_surf = pygame.image.load('Sprites\\bg 4 1200x600.png')
        ground_surf = pygame.image.load('Sprites\\grass.png')
        self.sc.blit(background_surf, background_surf.get_rect(bottomright=(1200, 600)))
        self.sc.blit(ground_surf, ground_surf.get_rect(bottomright=(1200, 600)))

        self.obstructions = [WoodBeam(905, 475, False, self.space, self.sc),
                             WoodBeam(995, 475, False, self.space, self.sc),
                             WoodBeam(950, 420, True, self.space, self.sc),
                             GlassBeam(980, 475, False, self.space, self.sc),
                             GalssBeam(920, 475, False, self.space, self.sc),
                             WoodBeam(905, 365, False, self.space, self.sc),
                             WoodBeam(995, 365, False, self.space, self.sc),
                             WoodBeam(950, 310, True, self.space, self.sc),
                             GlassBeam(980, 365, False, self.space, self.sc),
                             GalssBeam(920, 365, False, self.space, self.sc),
                             WoodBeam(1020, 475, False, self.space, self.sc),
                             WoodBeam(1110, 475, False, self.space, self.sc),
                             WoodBeam(1065, 420, True, self.space, self.sc),
                             GlassBeam(1095, 475, False, self.space, self.sc),
                             GalssBeam(1035, 475, False, self.space, self.sc),
                             WoodBeam(1020, 365, False, self.space, self.sc),
                             WoodBeam(1110, 365, False, self.space, self.sc),
                             WoodBeam(1065, 310, True, self.space, self.sc),
                             GlassBeam(1095, 365, False, self.space, self.sc),
                             GalssBeam(1035, 365, False, self.space, self.sc),
                             ]

        self.pigs = [DefaultPig(950, 400, self.space, self.sc),
                     DefaultPig(950, 510, self.space, self.sc),
                     DefaultPig(1065, 400, self.space, self.sc),
                     DefaultPig(1065, 510, self.space, self.sc)]


        self.birds = [BigBird(100, 495, self.space, self.sc),
                      BigBird(65, 495, self.space, self.sc),
                      TriangleBird(20, 510, self.space, self.sc)]
        self.number_of_birds = 3

    def level5(self):
        background_surf = pygame.image.load('Sprites\\bg 5 1200x600.png')
        ground_surf = pygame.image.load('Sprites\\grass.png')
        self.sc.blit(background_surf, background_surf.get_rect(bottomright=(1200, 600)))
        self.sc.blit(ground_surf, ground_surf.get_rect(bottomright=(1200, 600)))

        self.obstructions = [WoodBeam(905, 475, False, self.space, self.sc),
                             WoodBeam(995, 475, False, self.space, self.sc),
                             WoodBeam(950, 420, True, self.space, self.sc),
                             GlassBeam(980, 475, False, self.space, self.sc),
                             GalssBeam(920, 475, False, self.space, self.sc),
                             WoodBeam(905, 365, False, self.space, self.sc),
                             WoodBeam(995, 365, False, self.space, self.sc),
                             WoodBeam(950, 310, True, self.space, self.sc),
                             GlassBeam(980, 365, False, self.space, self.sc),
                             GalssBeam(920, 365, False, self.space, self.sc),
                             WoodBeam(905, 255, False, self.space, self.sc),
                             WoodBeam(995, 255, False, self.space, self.sc),
                             GlassBeam(950, 200, True, self.space, self.sc),
                             ]

        self.pigs = [DefaultPig(950, 400, self.space, self.sc),
                     DefaultPig(950, 510, self.space, self.sc),
                     DefaultPig(950, 290, self.space, self.sc),
                     DefaultPig(1050, 510, self.space, self.sc),
                     DefaultPig(1090, 510, self.space, self.sc),
                     KingPig(1120, 495, self.space, self.sc)]



        self.birds = [BigBird(100, 495, self.space, self.sc),
                      TriangleBird(60, 510, self.space, self.sc),
                      RedBird(20, 510, self.space, self.sc)]
        self.number_of_birds = 3
