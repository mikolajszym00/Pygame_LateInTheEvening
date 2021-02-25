import pygame
import math
from .characters import Characters

images = []
for i in range(1, 4):
    boom = pygame.image.load('game assets/boomerang/boomerang{}.png'.format(i))
    boom = pygame.transform.scale(boom, (20, 20))
    images.append(boom)

boom_pic = images[0]


class Boomerang(Characters):
    def __init__(self, boom_pos, mouse_pos):
        super().__init__(boom_pos[0], boom_pos[1])
        self.images = images

        self.animation_count = 0

        self.mouse_pos = mouse_pos
        self.boom_pos = boom_pos

        self.switch_there = 'ON'
        self.switch_back = 'OFF'
        self.speed = 4

    def draw(self, screen):
        """
        Draws the boom on the screen, using images
        :param screen: surface
        :return: None
        """
        if self.switch_there == 'ON' or self.switch_back == 'ON':
            self.draw_sprite(screen, self.images, 0.125)
        else:
            self.rectangle = self.get_rect((self.x, self.y))
            screen.blit(self.img, (self.x, self.y))
        self.fall_point(screen)

    def update(self, hero_pos):
        self.there(hero_pos)
        self.back()

    def fall_point(self, screen):
        if self.switch_back == "ON":
            pygame.draw.circle(screen, (230, 23, 32), (self.boom_pos[0]+self.img.get_width()/2,
                                                       self.boom_pos[1]+self.img.get_height()/2), 5, 0)

    def add_points(self):
        return int(math.sqrt((self.boom_pos[0] - self.x) ** 2 + (self.boom_pos[1] - self.y) ** 2)/80)

    def there(self, hero_pos_future):
        """
        Depends on the quarter hero
        :param hero_pos_future: position which is used to return the boomerang
        :return: None
        """
        if self.switch_there == 'OFF':
            pass
        # 1 quarter
        elif self.boom_pos[0] <= self.mouse_pos[0] and self.boom_pos[1] > self.mouse_pos[1]:
            if self.y - self.mouse_pos[1] > 0:
                self.y -= self.speed
            elif self.mouse_pos[0] - self.x > 0:
                self.x += self.speed
            else:
                self.switch_there = 'OFF'
                self.switch_back = 'ON'
                self.boom_pos = hero_pos_future

        # 2 quarter
        elif self.boom_pos[0] < self.mouse_pos[0] and self.mouse_pos[1] >= self.boom_pos[1]:
            if self.mouse_pos[0] - self.x > 0:
                self.x += self.speed
            elif self.mouse_pos[1] - self.y > 0:
                self.y += self.speed
            else:
                self.switch_there = 'OFF'
                self.switch_back = 'ON'
                self.boom_pos = hero_pos_future

        # 3 quarter
        elif self.mouse_pos[0] <= self.boom_pos[0] and self.mouse_pos[1] > self.boom_pos[1]:
            if self.mouse_pos[1] - self.y > 0:
                self.y += self.speed
            elif self.x - self.mouse_pos[0] > 0:
                self.x -= self.speed
            else:
                self.switch_there = 'OFF'
                self.switch_back = 'ON'
                self.boom_pos = hero_pos_future

        # 4 quarter
        elif self.mouse_pos[0] < self.boom_pos[0] and self.boom_pos[1] >= self.mouse_pos[1]:
            if self.x - self.mouse_pos[0] > 0:
                self.x -= self.speed
            elif self.y - self.mouse_pos[1] > 0:
                self.y -= self.speed
            else:
                self.switch_there = 'OFF'
                self.switch_back = 'ON'
                self.boom_pos = hero_pos_future

    def back(self):
        if self.switch_back == 'OFF':
            pass
        # 1 quarter
        elif self.boom_pos[0] >= self.mouse_pos[0] and self.boom_pos[1] < self.mouse_pos[1]:
            if self.y - self.boom_pos[1] > 0:
                self.y -= self.speed
            elif self.boom_pos[0] - self.x > 0:
                self.x += self.speed
            else:
                self.switch_back = 'OFF'

        # 2 quarter
        elif self.boom_pos[0] > self.mouse_pos[0] and self.mouse_pos[1] <= self.boom_pos[1]:
            if self.boom_pos[0] - self.x > 0:
                self.x += self.speed
            elif self.boom_pos[1] - self.y > 0:
                self.y += self.speed
            else:
                self.switch_back = 'OFF'

        # 3 quarter
        elif self.mouse_pos[0] >= self.boom_pos[0] and self.mouse_pos[1] < self.boom_pos[1]:
            if self.boom_pos[1] - self.y > 0:
                self.y += self.speed
            elif self.x - self.boom_pos[0] > 0:
                self.x -= self.speed
            else:
                self.switch_back = 'OFF'

        # 4 quarter
        elif self.mouse_pos[0] > self.boom_pos[0] and self.boom_pos[1] <= self.mouse_pos[1]:
            if self.x - self.boom_pos[0] > 0:
                self.x -= self.speed
            elif self.y - self.boom_pos[1] > 0:
                self.y -= self.speed
            else:
                self.switch_back = 'OFF'
