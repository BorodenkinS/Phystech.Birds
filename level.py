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
        self.sling.position = (120, 500)

    def level1(self):
        # проработать механизм удаления прошлых объектов.
        # просто заносить в список на удаление, наверное, недостаточно, ибо функция удаления сработает позже
        # создания новых объектов
        self.background_surf = pg.image.load('Sprites\\bg 1 1200x600.png')
        self.ground_surf = pg.image.load('Sprites\\grass.png')
        self.ground_body = pm.Body(1, 1, pm.Body.KINEMATIC)
        self.ground_body.position = pm.Vec2d(600, 585)
        self.ground_shape = pm.Poly.create_box(self.ground_body, (1200, 30))
        self.space.add(self.ground_body, self.ground_shape)
        self.ground_shape.friction = 3
        self.ground_shape.elasticity = 0.3
        self.ground_shape.collision_type = 3

        self.beams = [WoodBeam(1050, 520, False, self.space, self.sc),
                             WoodBeam(1000, 520, False, self.space, self.sc),
                             WoodBeam(1025, 465, True, self.space, self.sc),
                             WoodBeam(920, 520, False, self.space, self.sc),
                             WoodBeam(870, 520, False, self.space, self.sc),
                             WoodBeam(895, 465, True, self.space, self.sc),
                             WoodBeam(720, 520, False, self.space, self.sc),
                             WoodBeam(670, 520, False, self.space, self.sc),
                             WoodBeam(695, 465, True, self.space, self.sc)]

        self.pigs = [DefaultPig(1025, 445, self.space, self.sc),
                     DefaultPig(895, 445, self.space, self.sc),
                     DefaultPig(695, 445, self.space, self.sc)]

        self.birds = [RedBird(100, 555, self.space, self.sc),
                      RedBird(75, 555, self.space, self.sc),
                      RedBird(50, 555, self.space, self.sc),
                      RedBird(25, 555, self.space, self.sc)]
        self.number_of_birds = 4
        self.number_of_birds = 4

    def level2(self):
        self.background_surf = pg.image.load('Sprites\\bg 2 1200x600.png')
        self.ground_surf = pg.image.load('Sprites\\grass.png')
        self.ground_body = pm.Body(1, 1, pm.Body.KINEMATIC)
        self.ground_body.position = pm.Vec2d(600, 585)
        self.ground_shape = pm.Poly.create_box(self.ground_body, (1200, 30))
        self.space.add(self.ground_body, self.ground_shape)
        self.ground_shape.friction = 3
        self.ground_shape.elasticity = 0.3
        self.ground_shape.collision_type = 3

        self.beams = [WoodBeam(905, 520, False, self.space, self.sc),
                             WoodBeam(995, 520, False, self.space, self.sc),
                             WoodBeam(950, 465, True, self.space, self.sc),
                             WoodBeam(905, 410, False, self.space, self.sc),
                             WoodBeam(995, 410, False, self.space, self.sc),
                             WoodBeam(950, 355, True, self.space, self.sc),
                             GlassBeam(890, 520, False, self.space, self.sc),
                             GlassBeam(800, 520, False, self.space, self.sc),
                             GlassBeam(845, 465, True, self.space, self.sc)]

        self.pigs = [DefaultPig(950, 445, self.space, self.sc),
                     DefaultPig(845, 555, self.space, self.sc),
                     KingPig(950, 540, self.space, self.sc)]

        self.birds = [TriangleBird(100, 550, self.space, self.sc),
                      TriangleBird(75, 550, self.space, self.sc),
                      RedBird(25, 555, self.space, self.sc),
                      RedBird(25, 555, self.space, self.sc)]
        self.number_of_birds = 4

    def level3(self):
        self.background_surf = pg.image.load('Sprites\\bg 3 1200x600.png')
        self.ground_surf = pg.image.load('Sprites\\grass.png')
        self.ground_shape = pm.Segment(self.space.static_body, (0, 578), (1200, 578), 44)
        self.space.add(self.ground_shape)
        self.ground_shape.friction = 3
        self.ground_shape.elasticity = 0.3
        self.ground_shape.collision_type = 3

        self.beams = [WoodBeam(905, 520, False, self.space, self.sc),
                             WoodBeam(995, 520, False, self.space, self.sc),
                             GlassBeam(950, 465, True, self.space, self.sc),
                             WoodBeam(890, 520, False, self.space, self.sc),
                             WoodBeam(800, 520, False, self.space, self.sc),
                             GlassBeam(845, 465, True, self.space, self.sc),
                             WoodBeam(1010, 520, False, self.space, self.sc),
                             WoodBeam(1100, 520, False, self.space, self.sc),
                             GlassBeam(1055, 465, True, self.space, self.sc),
                             WoodBeam(960, 410, False, self.space, self.sc),
                             WoodBeam(1050, 410, False, self.space, self.sc),
                             GlassBeam(1005, 355, True, self.space, self.sc),
                             WoodBeam(850, 410, False, self.space, self.sc),
                             WoodBeam(940, 410, False, self.space, self.sc),
                             GlassBeam(890, 355, True, self.space, self.sc),
                             WoodBeam(910, 300, False, self.space, self.sc),
                             WoodBeam(1000, 300, False, self.space, self.sc),
                             GlassBeam(955, 245, True, self.space, self.sc)
                             ]

        self.pigs = [DefaultPig(845, 555, self.space, self.sc),
                     DefaultPig(950, 555, self.space, self.sc),
                     DefaultPig(1050, 555, self.space, self.sc),
                     DefaultPig(1000, 445, self.space, self.sc),
                     DefaultPig(890, 445, self.space, self.sc),
                     DefaultPig(950, 335, self.space, self.sc)]

        self.birds = [BigBird(100, 545, self.space, self.sc),
                      BigBird(65, 545, self.space, self.sc),
                      RedBird(20, 550, self.space, self.sc)]
        self.number_of_birds = 3

    def level4(self):
        self.background_surf = pg.image.load('Sprites\\bg 4 1200x600.png')
        self.ground_surf = pg.image.load('Sprites\\grass.png')
        self.ground_body = pm.Body(1, 1, pm.Body.KINEMATIC)
        self.ground_body.position = pm.Vec2d(600, 585)
        self.ground_shape = pm.Poly.create_box(self.ground_body, (1200, 30))
        self.space.add(self.ground_body, self.ground_shape)
        self.ground_shape.friction = 3
        self.ground_shape.elasticity = 0.3
        self.ground_shape.collision_type = 3
        self.beams = [WoodBeam(905, 520, False, self.space, self.sc),
                             WoodBeam(995, 520, False, self.space, self.sc),
                             WoodBeam(950, 465, True, self.space, self.sc),
                             GlassBeam(980, 520, False, self.space, self.sc),
                             GlassBeam(920, 520, False, self.space, self.sc),
                             WoodBeam(905, 410, False, self.space, self.sc),
                             WoodBeam(995, 410, False, self.space, self.sc),
                             WoodBeam(950, 355, True, self.space, self.sc),
                             GlassBeam(980, 410, False, self.space, self.sc),
                             GlassBeam(920, 410, False, self.space, self.sc),
                             WoodBeam(1020, 520, False, self.space, self.sc),
                             WoodBeam(1110, 520, False, self.space, self.sc),
                             WoodBeam(1065, 465, True, self.space, self.sc),
                             GlassBeam(1095, 520, False, self.space, self.sc),
                             GlassBeam(1035, 520, False, self.space, self.sc),
                             WoodBeam(1020, 410, False, self.space, self.sc),
                             WoodBeam(1110, 410, False, self.space, self.sc),
                             WoodBeam(1065, 355, True, self.space, self.sc),
                             GlassBeam(1095, 410, False, self.space, self.sc),
                             GlassBeam(1035, 410, False, self.space, self.sc),
                             ]

        self.pigs = [DefaultPig(950, 445, self.space, self.sc),
                     DefaultPig(950, 555, self.space, self.sc),
                     DefaultPig(1065, 445, self.space, self.sc),
                     DefaultPig(1065, 555, self.space, self.sc)]

        self.birds = [BigBird(100, 550, self.space, self.sc),
                      BigBird(65, 550, self.space, self.sc),
                      TriangleBird(20, 550, self.space, self.sc)]
        self.number_of_birds = 3

    def level5(self):
        self.background_surf = pg.image.load('Sprites\\bg 5 1200x600.png')
        self.ground_surf = pg.image.load('Sprites\\grass.png')
        self.ground_body = pm.Body(1, 1, pm.Body.KINEMATIC)
        self.ground_body.position = pm.Vec2d(600, 585)
        self.ground_shape = pm.Poly.create_box(self.ground_body, (1200, 30))
        self.space.add(self.ground_body, self.ground_shape)
        self.ground_shape.friction = 3
        self.ground_shape.elasticity = 0.3
        self.ground_shape.collision_type = 3

        self.beams = [WoodBeam(905, 520, False, self.space, self.sc),
                             WoodBeam(995, 520, False, self.space, self.sc),
                             WoodBeam(950, 465, True, self.space, self.sc),
                             GlassBeam(980, 520, False, self.space, self.sc),
                             GlassBeam(920, 520, False, self.space, self.sc),
                             WoodBeam(905, 410, False, self.space, self.sc),
                             WoodBeam(995, 410, False, self.space, self.sc),
                             WoodBeam(950, 355, True, self.space, self.sc),
                             GlassBeam(980, 410, False, self.space, self.sc),
                             GlassBeam(920, 410, False, self.space, self.sc),
                             WoodBeam(905, 300, False, self.space, self.sc),
                             WoodBeam(995, 300, False, self.space, self.sc),
                             GlassBeam(950, 245, True, self.space, self.sc),
                             ]
        self.pigs = [DefaultPig(950, 445, self.space, self.sc),
                     DefaultPig(950, 555, self.space, self.sc),
                     DefaultPig(950, 335, self.space, self.sc),
                     DefaultPig(1050, 555, self.space, self.sc),
                     DefaultPig(1090, 555, self.space, self.sc),
                     KingPig(1120, 540, self.space, self.sc)]

        self.birds = [BigBird(100, 545, self.space, self.sc),
                      TriangleBird(60, 550, self.space, self.sc),
                      RedBird(20, 555, self.space, self.sc)]
        self.number_of_birds = 3
