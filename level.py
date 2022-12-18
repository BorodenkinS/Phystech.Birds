import pymunk as pm
import pygame as pg
from birds import *
from pigs import *
from obstructions import *


class Level:
    # убрать атрибуты, которые заполняются в level_i
    def __init__(self, space, screen):
        self.birds = []
        self.pigs = []
        self.beams = []
        self.obstructions = []
        self.number_of_birds = 0
        self.mouse_is_up = True
        self.pigs_to_remove = []
        self.birds_to_remove = []
        self.beams_to_remove = []
        self.flying_bird = None
        self.score = 0
        self.sc = screen
        self.space = space
        self.levels = [self.level1, self.level2, self.level3, self.level4, self.level5]
        self.sling = Sling(self.sc)
        self.sling.position = (120, 400)

    def level1(self):
        # проработать механизм удаления прошлых объектов.
        # просто заносить в список на удаление, наверное, недостаточно, ибо функция удаления сработает позже
        # создания новых объектов
        self.background_surf = pg.image.load('Sprites\\bg 1 1200x600.png')
        self.ground_surf = pg.image.load('Sprites\\grass.png')
        self.ground_shape = pm.Segment(self.space.static_body, (0,578), (1200, 578), 44)
        self.space.add(self.ground_shape)
        self.ground_shape.friction = 1
        self.ground_shape.elasticity = 1
        self.ground_shape.collision_type = 3

        self.obstructions = [WoodBeam(1050, 535, False, self.space, self.sc),
                             WoodBeam(1000, 535, False, self.space, self.sc),
                             WoodBeam(1025, 480, True, self.space, self.sc),
                             WoodBeam(920, 535, False, self.space, self.sc),
                             WoodBeam(870, 535, False, self.space, self.sc),
                             WoodBeam(895, 480, True, self.space, self.sc),
                             WoodBeam(720, 535, False, self.space, self.sc),
                             WoodBeam(670, 535, False, self.space, self.sc),
                             WoodBeam(695, 480, True, self.space, self.sc)]

        self.pigs = [DefaultPig(1025, 460, self.space, self.sc),
                     DefaultPig(895, 460, self.space, self.sc),
                     DefaultPig(695, 460, self.space, self.sc)]

        self.birds = [RedBird(100, 550, self.space, self.sc),
                      RedBird(75, 550, self.space, self.sc),
                      RedBird(50, 550, self.space, self.sc),
                      RedBird(25, 550, self.space, self.sc)]
        self.number_of_birds = 4

    def level2(self):
        self.background_surf = pg.image.load('Sprites\\bg 2 1200x600.png')
        self.ground_surf = pg.image.load('Sprites\\grass.png')
        self.ground_shape = pm.Segment(self.space.static_body, (0, 578), (1200, 578), 44)
        self.space.add(self.ground_shape)
        self.ground_shape.friction = 1
        self.ground_shape.elasticity = 1
        self.ground_shape.collision_type = 3

        self.obstructions = [WoodBeam(905, 535, False, self.space, self.sc),
                             WoodBeam(995, 535, False, self.space, self.sc),
                             WoodBeam(950, 480, True, self.space, self.sc),
                             WoodBeam(905, 425, False, self.space, self.sc),
                             WoodBeam(995, 425, False, self.space, self.sc),
                             WoodBeam(950, 370, True, self.space, self.sc),
                             GlassBeam(890, 535, False, self.space, self.sc),
                             GlassBeam(800, 535, False, self.space, self.sc),
                             GlassBeam(845, 480, True, self.space, self.sc)]

        self.pigs = [DefaultPig(950, 460, self.space, self.sc),
                     DefaultPig(845, 570, self.space, self.sc),
                     KingPig(950, 555, self.space, self.sc)]

        self.birds = [TriangleBird(100, 550, self.space, self.sc),
                      TriangleBird(75, 550, self.space, self.sc),
                      RedBird(25, 550, self.space, self.sc),
                      RedBird(25, 550, self.space, self.sc)]
        self.number_of_birds = 4

    def level3(self):
        self.background_surf = pg.image.load('Sprites\\bg 3 1200x600.jpg')
        self.ground_surf = pg.image.load('Sprites\\grass.png')
        self.ground_shape = pm.Segment(self.space.static_body, (0, 578), (1200, 578), 44)
        self.space.add(self.ground_shape)
        self.ground_shape.friction = 1
        self.ground_shape.elasticity = 1
        self.ground_shape.collision_type = 3

        self.obstructions = [WoodBeam(905, 535, False, self.space, self.sc),
                             WoodBeam(995, 535, False, self.space, self.sc),
                             GlassBeam(950, 480, True, self.space, self.sc),
                             WoodBeam(890, 535, False, self.space, self.sc),
                             WoodBeam(800, 535, False, self.space, self.sc),
                             GlassBeam(845, 480, True, self.space, self.sc),
                             WoodBeam(1010, 535, False, self.space, self.sc),
                             WoodBeam(1100, 535, False, self.space, self.sc),
                             GlassBeam(1055, 480, True, self.space, self.sc),
                             WoodBeam(960, 425, False, self.space, self.sc),
                             WoodBeam(1050, 425, False, self.space, self.sc),
                             GlassBeam(1005, 370, True, self.space, self.sc),
                             WoodBeam(850, 425, False, self.space, self.sc),
                             WoodBeam(940, 425, False, self.space, self.sc),
                             GlassBeam(890, 370, True, self.space, self.sc),
                             WoodBeam(910, 315, False, self.space, self.sc),
                             WoodBeam(1000, 315, False, self.space, self.sc),
                             GlassBeam(955, 260, True, self.space, self.sc)
                             ]

        self.pigs = [DefaultPig(845, 570, self.space, self.sc),
                     DefaultPig(950, 570, self.space, self.sc),
                     DefaultPig(1050, 570, self.space, self.sc),
                     DefaultPig(1000, 460, self.space, self.sc),
                     DefaultPig(890, 460, self.space, self.sc),
                     DefaultPig(950, 350, self.space, self.sc)]

        self.birds = [BigBird(100, 545, self.space, self.sc),
                      BigBird(65, 545, self.space, self.sc),
                      RedBird(20, 550, self.space, self.sc)]
        self.number_of_birds = 3

    def level4(self):
        self.background_surf = pg.image.load('Sprites\\bg 4 1200x600.jpg')
        self.ground_surf = pg.image.load('Sprites\\grass.png')
        self.ground_shape = pm.Segment(self.space.static_body, (0, 578), (1200, 578), 44)
        self.space.add(self.ground_shape)
        self.ground_shape.friction = 1
        self.ground_shape.elasticity = 1
        self.ground_shape.collision_type = 3
        self.obstructions = [WoodBeam(905, 535, False, self.space, self.sc),
                             WoodBeam(995, 535, False, self.space, self.sc),
                             WoodBeam(950, 480, True, self.space, self.sc),
                             GlassBeam(980, 535, False, self.space, self.sc),
                             GlassBeam(920, 535, False, self.space, self.sc),
                             WoodBeam(905, 425, False, self.space, self.sc),
                             WoodBeam(995, 425, False, self.space, self.sc),
                             WoodBeam(950, 370, True, self.space, self.sc),
                             GlassBeam(980, 425, False, self.space, self.sc),
                             GlassBeam(920, 425, False, self.space, self.sc),
                             WoodBeam(1020, 535, False, self.space, self.sc),
                             WoodBeam(1110, 535, False, self.space, self.sc),
                             WoodBeam(1065, 480, True, self.space, self.sc),
                             GlassBeam(1095, 535, False, self.space, self.sc),
                             GlassBeam(1035, 535, False, self.space, self.sc),
                             WoodBeam(1020, 425, False, self.space, self.sc),
                             WoodBeam(1110, 425, False, self.space, self.sc),
                             WoodBeam(1065, 370, True, self.space, self.sc),
                             GlassBeam(1095, 425, False, self.space, self.sc),
                             GlassBeam(1035, 425, False, self.space, self.sc),
                             ]

        self.pigs = [DefaultPig(950, 460, self.space, self.sc),
                     DefaultPig(950, 570, self.space, self.sc),
                     DefaultPig(1065, 460, self.space, self.sc),
                     DefaultPig(1065, 570, self.space, self.sc)]

        self.birds = [BigBird(100, 550, self.space, self.sc),
                      BigBird(65, 550, self.space, self.sc),
                      TriangleBird(20, 550, self.space, self.sc)]
        self.number_of_birds = 3

    def level5(self):
        self.background_surf = pg.image.load('Sprites\\bg 5 1200x600.jpg')
        self.ground_surf = pg.image.load('Sprites\\grass.png')
        self.ground_shape = pm.Segment(self.space.static_body, (0, 578), (1200, 578), 44)
        self.space.add(self.ground_shape)
        self.ground_shape.friction = 1
        self.ground_shape.elasticity = 1
        self.ground_shape.collision_type = 3

        self.obstructions = [WoodBeam(905, 535, False, self.space, self.sc),
                             WoodBeam(995, 535, False, self.space, self.sc),
                             WoodBeam(950, 480, True, self.space, self.sc),
                             GlassBeam(980, 535, False, self.space, self.sc),
                             GlassBeam(920, 535, False, self.space, self.sc),
                             WoodBeam(905, 425, False, self.space, self.sc),
                             WoodBeam(995, 425, False, self.space, self.sc),
                             WoodBeam(950, 370, True, self.space, self.sc),
                             GlassBeam(980, 425, False, self.space, self.sc),
                             GlassBeam(920, 425, False, self.space, self.sc),
                             WoodBeam(905, 315, False, self.space, self.sc),
                             WoodBeam(995, 315, False, self.space, self.sc),
                             GlassBeam(950, 260, True, self.space, self.sc),
                             ]
        self.pigs = [DefaultPig(950, 460, self.space, self.sc),
                     DefaultPig(950, 570, self.space, self.sc),
                     DefaultPig(950, 350, self.space, self.sc),
                     DefaultPig(1050, 570, self.space, self.sc),
                     DefaultPig(1090, 570, self.space, self.sc),
                     KingPig(1120, 555, self.space, self.sc)]

        self.birds = [BigBird(100, 545, self.space, self.sc),
                      TriangleBird(60, 550, self.space, self.sc),
                      RedBird(20, 550, self.space, self.sc)]
        self.number_of_birds = 3
