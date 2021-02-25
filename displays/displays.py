import pygame
import random
import time
from characters.boomerang import boom_pic


class Displays:
    def __init__(self):
        self.boom_pic = boom_pic
        self.rectangle = None

        self.time_left = None
        self.life_time = 6
        self.timer = time.time()
        self.is_collected = True
        self.random_loc = -100, -100

    def draw(self, screen, boom_number):
        self.lives(screen, boom_number)
        self.extra_life(screen)

    @staticmethod
    def lives(screen, boom_number):
        for i in range(boom_number):
            screen.blit(boom_pic, (10 + i * 30, 10))

    @staticmethod
    def score(screen, score):
        a_text = pygame.font.SysFont("monospace", 30).render('Score: {}'.format(score), True, (255, 255, 255))
        a_rect = a_text.get_rect(center=(650, 20))
        screen.blit(a_text, a_rect)

    def extra_life(self, screen):
        if time.time() - self.timer > random.randrange(20, 30):
            self.timer = time.time()
            self.is_collected = False
            self.random_loc = random.randrange(200, 500), random.randrange(200, 400)

        self.time_left = self.life_time + self.timer - time.time()
        if self.time_left > 0 and not self.is_collected:
            self.rectangle = self.boom_pic.get_rect(center=self.random_loc)
            self.extra_boom_level(screen, self.random_loc, self.life_time, int(self.time_left))
            screen.blit(self.boom_pic, self.random_loc)
        else:
            self.is_collected = True

    @staticmethod
    def extra_boom_level(screen, pos, hp_max, hp):
        for i in range(1, hp_max + 1):
            rect_w = 24/hp_max
            if i <= hp:
                colour = (4, 160, 34)
            else:
                colour = (180, 20, 34)
            pygame.draw.rect(screen, colour, pygame.Rect(pos[0] - 5 + i*rect_w, pos[1] - 8, rect_w, 3))
