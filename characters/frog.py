import pygame
from .enemies import Enemies

images_run_right = []
images_run_left = []
for i in range(1, 7):
    frog = pygame.image.load('game assets/frog/frog_run0{}.xcf'.format(i))
    frog = pygame.transform.scale(frog, (24 * 2, 26 * 2))
    images_run_right.append(frog)
    """image will be reversed in order to simulate running left"""
    frog = pygame.transform.flip(frog, True, False)
    images_run_left.append(frog)


class Frog(Enemies):
    def __init__(self):
        super().__init__()
        self.images_list = {-1: images_run_right, 1: images_run_left}
        self.images = self.images_list[self.side]

        self.max_speed_x = 1
        self.max_speed_y = 1

        self.speed_x = self.speed_x()
        self.speed_y = self.speed_y()

        self.max_lives = 48
        self.lives = self.max_lives
        self.corr_x = 0
        self.corr_y = -5

        self.kill_bonus = (abs(self.speed_x) * abs(self.speed_y)) * 20
