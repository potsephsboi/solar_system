import math
import pygame
import time

from PIL import Image


pygame.init()
WIDTH = 1000
HEIGHT = 1000
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FPS = 35

class Planet:
    Planets = []
    def __init__(self, name, icon, ang_vel, vx, vy, pos, size) -> None:
        self.name = name
        self.icon = icon 
        self.ang_vel = ang_vel
        self.vx = vx
        self.vy = vy
        self.vmax = vx
        self.pos = pos
        self.size = size
        Planet.Planets.append(self)


    def __repr__(self) -> str:
        return f'[PLANET] {self.name} || [POSITION] {self.pos} || [VELOCITY] {math.sqrt(self.vx**2 + self.vy**2)}'


def init_planets():
    Planet('sun', pygame.image.load('../planets_animation/planets/sun.png'), 0, 0, 0, [WIDTH/2, HEIGHT/2],
        (int(Image.open('../planets_animation/planets/sun.png').width), int(Image.open('../planets_animation/planets/sun.png').height))
        )

    Planet('mercury', pygame.image.load('../planets_animation/planets/mercury.png'), 8, 25, 0, [WIDTH/2, 400],
        (int(Image.open('../planets_animation/planets/mercury.png').width), int(Image.open('../planets_animation/planets/mercury.png').height))
        )

    Planet('venus', pygame.image.load('../planets_animation/planets/venus.png'), 6, 23, 0, [WIDTH/2, 340],
        (int(Image.open('../planets_animation/planets/venus.png').width), int(Image.open('../planets_animation/planets/venus.png').height))
        )

    Planet('earth', pygame.image.load('../planets_animation/planets/earth.png'), 3.5, 22, 0, [WIDTH/2, 270],
        (int(Image.open('../planets_animation/planets/earth.png').width), int(Image.open('../planets_animation/planets/earth.png').height))
        )

    Planet('mars', pygame.image.load('../planets_animation/planets/mars.png'), 3, 20, 0, [WIDTH/2, 210],
        (int(Image.open('../planets_animation/planets/mars.png').width), int(Image.open('../planets_animation/planets/mars.png').height))
        )

    

