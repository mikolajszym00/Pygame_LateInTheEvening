import pygame


class Tree:
    def __init__(self, pos):
        self.img = pygame.image.load('game assets/bg/bg_arm2.xcf')
        self.pos = pos
        self.rectangle = None

    def draw(self, screen):
        screen.blit(self.img, self.pos)

    def draw_under_bg(self, screen):
        self.rectangle = pygame.draw.rect(screen, (255, 255, 255), (self.pos[0] + 10, self.pos[1], 25, 30))
