import pygame
import random
from .characters import Characters


class Enemies(Characters):
    def __init__(self):
        start, self.side = self.start()
        super().__init__(start, random.randrange(0, 600))

        """for draw()"""
        self.animation_count = 0
        self.images = None

        """for speed()"""
        self.max_speed_x = 0
        self.max_speed_y = 0

        """for hp_bar()"""
        self.max_lives = 0
        self.lives = self.max_lives
        self.corr_x = 0
        self.corr_y = 0

        self.to_close = False

    @staticmethod
    def start():
        which_side = random.randrange(-1, 2, 2)  # -1 or 1
        start = {-1: random.randrange(-100, 0), 1: random.randrange(800, 900)}
        return start[which_side], which_side

    def speed_x(self):
        if self.side == -1:
            return random.randrange(-self.max_speed_x, 0)
        else:
            return random.randrange(1, self.max_speed_x+1)

    def speed_y(self):
        return random.randrange(-self.max_speed_y, self.max_speed_y+1)

    def draw(self, screen):
        animation_speed = (self.max_speed_x + self.max_speed_y)/20
        self.draw_sprite(screen, self.images, animation_speed)
        self.hp_bar(screen)

    def update(self):
        self.move()
        self.hero_to_close()

    def move(self):
        self.x -= self.speed_x
        self.y -= self.speed_y

    def hp_bar(self, screen):
        for i in range(self.max_lives):
            rect_w = 48/self.max_lives
            if i < self.lives:
                colour = (4, 160, 34)
            else:
                colour = (180, 20, 34)
            pygame.draw.rect(screen, colour, pygame.Rect(self.x + i*rect_w + self.corr_x,
                                                         self.y + self.corr_y,
                                                         rect_w, 4))

    def hero_to_close(self):
        if self.to_close:
            pass

    def out_of_screen(self):
        if self.x <= -110 or self.x >= 910 or self.y <= -110 or self.y >= 710:
            return False
        return True

    def __str__(self):
        return self.__class__.__name__
