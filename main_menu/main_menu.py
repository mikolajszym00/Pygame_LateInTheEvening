import pygame
import sys
from game import Game


class MainMenu:
    def __init__(self, screen):
        self.screen = screen

        self.animation_count = 0
        self.path = 'game assets/bg/bg_intro00.xcf'

    def run(self):
        while True:
            self.handle_events()

            self.screen.blit(pygame.image.load(self.path), (0, 0))
            pygame.display.set_caption('Late In The Evening')

            self.to_screen(60, 'Late In The Evening', (400, 200), False)
            self.to_screen(40, 'Play', (400, 280), True)
            self.to_screen(40, 'Leaderboard', (400, 340), True)

            pygame.display.update()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.to_screen(40, 'Play', (400, 280), True).collidepoint(pygame.mouse.get_pos()):
                    self.intro(1)
                    game = Game(self.screen)
                    score = game.run()
                    self.score_saver(score)
                    self.end_game(score)
                    self.intro(-1)
                if self.to_screen(40, 'Leaderboard', (400, 340), True).collidepoint(pygame.mouse.get_pos()):
                    self.leaderboard()
                if self.to_screen(40, 'OK', (400, 500), True).collidepoint(pygame.mouse.get_pos()):
                    return True

    def leaderboard(self):
        while not self.handle_events():
            self.screen.blit(pygame.image.load(self.path), (0, 0))

            self.to_screen(60, 'Highest scores:', (400, 150), False)
            self.to_screen(40, 'OK', (400, 500), True)

            with open('main_menu/LB.txt') as file:
                for index, i in enumerate(file.read().split(',')):
                    self.to_screen(40, '{}. {}'.format(index + 1, int(i)), (400, index * 50 + 220), False)

            pygame.display.update()

    def end_game(self, score):
        while not self.handle_events():
            self.screen.blit(pygame.image.load('game assets/bg/bg_intro06.xcf'), (0, 0))

            self.to_screen(60, 'Your score:', (400, 150), False)
            self.to_screen(60, '{}'.format(score), (400, 270), False)
            self.to_screen(40, 'OK', (400, 500), True)

            pygame.display.update()

    @staticmethod
    def score_saver(score):
        with open('main_menu/LB.txt', 'r') as file:
            scores_list = file.read().split(',')
            for index, number in enumerate(scores_list):
                if score >= int(number):
                    scores_list.insert(index, str(score))
                    scores_list.pop()
                    break
            scores = ','.join(scores_list)
        with open('main_menu/LB.txt', 'w') as file:
            file.write(scores)

    def to_screen(self, size, text, pos, change_colour):
        a_text = pygame.font.SysFont("monospace", size).render(text, True, (255, 255, 255))
        a_rect = a_text.get_rect(center=pos)
        if change_colour and a_rect.collidepoint(pygame.mouse.get_pos()):
            a_text = pygame.font.SysFont("monospace", size).render(text, True, (0, 0, 0))
        self.screen.blit(a_text, a_rect)
        return a_rect

    def intro(self, outro):
        while True:
            self.animation_count += outro * 0.05
            if self.animation_count >= 7:
                self.animation_count = 7
                break
            if self.animation_count < 0:
                self.animation_count = 0
                break

            self.screen.blit(pygame.image.load('game assets/bg/bg_intro0{}.xcf'.format(int(self.animation_count))),
                             (0, 0))

            pygame.display.update()
