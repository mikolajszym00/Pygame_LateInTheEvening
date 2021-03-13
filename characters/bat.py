import pygame
from .enemies import Enemies

#powinno być w metodzie w klasie
images = []
for i in range(1, 7):
    bat = pygame.image.load('game assets/bat/bat_flying0{}.xcf'.format(i))
    # if 1 < i < 6:
    #     images.append(bat)
    images.append(bat)
for i in range(6, 0, -1):
    bat = pygame.image.load('game assets/bat/bat_flying0{}.xcf'.format(i))
    images.append(bat)


class Bat(Enemies):
    def __init__(self):
        super().__init__()
        self.images = images

        self.max_speed_x = 4
        self.max_speed_y = 3

        self.speed_x = self.speed_x()
        self.speed_y = self.speed_y()

        self.max_lives = 12
        self.lives = self.max_lives
        self.corr_x = -10
        self.corr_y = -6

        self.kill_bonus = (abs(self.speed_x) * abs(self.speed_y)) * 20
