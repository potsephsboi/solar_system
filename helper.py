import math
import pygame
import time

from PIL import Image


pygame.init()
WIDTH = 600
HEIGHT = 600

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

    Planet('mercury', pygame.image.load('../planets_animation/planets/mercury.png'), 5, 15, 0, [WIDTH/2, 150],
        (int(Image.open('../planets_animation/planets/mercury.png').width), int(Image.open('../planets_animation/planets/mercury.png').height))
        )

