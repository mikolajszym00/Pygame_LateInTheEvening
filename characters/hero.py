import pygame
from .characters import Characters

images_run_right = []
images_run_left = []
for i in range(6):
    hero = pygame.image.load('game assets/hero/hero_run0{}.xcf'.format(i))
    hero = pygame.transform.scale(hero, (17 * 2, 20 * 2))
    images_run_right.append(hero)
    """image will be reversed in order to simulate running left"""
    hero = pygame.transform.flip(hero, True, False)
    images_run_left.append(hero)

images_idle = []
for i in range(4):
    hero = pygame.image.load('game assets/hero/hero_idle0{}.xcf'.format(i))
    hero = pygame.transform.scale(hero, (17 * 2, 20 * 2))
    images_idle.append(hero)


class Hero(Characters):
    def __init__(self):
        super().__init__(400, 300)

        self.images_run_r = images_run_right
        self.images_run_l = images_run_left
        self.images_idle = images_idle

        self.anim = 'idle'
        # self.animation_count = 0
        self.animation_speed = 0.2

    def draw(self, screen):
        dict_anim = {'idle': images_idle, 'run_right': self.images_run_r, 'run_left': self.images_run_l}
        images = dict_anim[self.anim]
        self.draw_sprite(screen, images, self.animation_speed)

    def update(self):
        self.move()
        self.screen_constrain()

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.x -= 2
        if keys[pygame.K_d]:
            self.x += 2
        if keys[pygame.K_w]:
            self.y -= 2
        if keys[pygame.K_s]:
            self.y += 2
        if (keys[pygame.K_d] or keys[pygame.K_s]) and not keys[pygame.K_a]:
            self.anim = 'run_right'
        elif keys[pygame.K_a] or keys[pygame.K_w]:
            self.anim = 'run_left'
        else:
            self.anim = 'idle'

    def screen_constrain(self):
        """
        Checking if hero touch the border of the screen
        :return: None
        """
        if self.x >= 800-40:
            self.x = 800-40
        if self.x <= 0:
            self.x = 0
        if self.y >= 600-40:
            self.y = 600-40
        if self.y <= 0:
            self.y = 0
