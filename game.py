import pygame
import time
import math
from characters.bat import Bat
from characters.frog import Frog
from characters.hero import Hero
from characters.tree import Tree
from characters.boomerang import Boomerang
from displays.displays import Displays


class Game:
    def __init__(self, screen):
        self.width = 800
        self.height = 600
        self.screen = screen
        self.enemies = []
        self.hero = Hero()
        self.boom = None
        self.dis = Displays()
        self.trees = [Tree((435, 175)),
                      Tree((707, 89)),
                      Tree((144, 386)),
                      Tree((586, 492)),
                      Tree((501, 541))]

        """for enemy_spawner() and timer()"""
        self.start_time = time.time()
        self.bat_timer = time.time()
        self.frog_timer = time.time()

        self.score = 0
        self.boom_number = 5

        self.bg = pygame.image.load("game assets/bg/bg_meadow.xcf")
        self.bg = pygame.transform.scale(self.bg, (self.width, self.height))

        self.bg_tree_top = pygame.image.load("game assets/bg/bg_tree_top.xcf")

        self.animation_count = 0

    def run(self):
        run = True
        clock = pygame.time.Clock()

        """ main game loop"""
        while run:
            clock.tick(60)
            if self.boom_number == -1:
                return self.score

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return self.score
                if event.type == pygame.MOUSEBUTTONDOWN and self.boom is None and self.boom_number > 0:
                    self.boom = Boomerang((self.hero.x, self.hero.y), pygame.mouse.get_pos())

                    self.boom_number -= 1
                # if event.type == pygame.MOUSEBUTTONDOWN:
                #     pos = pygame.mouse.get_pos()
                #     self.clicks.append(pos)
                #     print(self.clicks)
                # for p in self.clicks:
                #     pygame.draw.circle(self.screen, (0, 0, 0), (p[0], p[1]), 5, 0)

            for en in self.enemies:
                if not en.out_of_screen():
                    self.enemies.remove(en)

                """enemy is too close to hero"""
                if self.dist(en.rectangle) < 100:
                    en.to_close = True
                else:
                    en.to_close = False

                """enemy interrupts hero"""
                if en.rectangle.colliderect(self.hero.rectangle):
                    self.enemies.remove(en)

                    self.boom_number -= 1

                """enemy interrupts flying boomerang"""
                if self.boom and \
                        self.boom.rectangle and \
                        en.rectangle.colliderect(self.boom.rectangle) and \
                        (self.boom.switch_there == 'ON' or self.boom.switch_back == 'ON'):
                    en.lives -= 1
                    if en.lives == 0:
                        self.score += en.kill_bonus + self.boom.add_points()
                        self.enemies.remove(en)
                    else:
                        if en.speed_y != 0:
                            self.score += self.boom.add_points() * abs(en.speed_y)
                        else:
                            self.score += self.boom.add_points()

                """enemy interrupts lying boomerang"""
                if self.boom and \
                        self.boom.rectangle and \
                        en.rectangle.colliderect(self.boom.rectangle) and \
                        (self.boom.switch_there == 'OFF' and self.boom.switch_back == 'OFF'):
                    self.boom = None

                """enemy interrupts extra boomerang"""
                if not self.dis.is_collected and self.dis.rectangle.colliderect(en.rectangle):
                    self.dis.is_collected = True

                """enemy interrupts root"""
                for tree in self.trees:
                    if str(en) == 'Frog' and tree.rectangle.colliderect(en.rectangle):
                        pass
                        """może teleportować zabe w losowe miejsce na srodku planszy"""

                en.update()

            """hero interrupts lying boomerang"""
            if self.boom:
                self.boom.update((self.hero.x, self.hero.y))
                if self.boom.rectangle and \
                        self.boom.rectangle.colliderect(self.hero.rectangle) and \
                        self.boom.switch_there == 'OFF' and \
                        self.boom.switch_back == 'OFF':
                    self.boom = None

                    self.boom_number += 1

            """hero interrupts extra boomerang"""
            if not self.dis.is_collected and self.dis.rectangle.colliderect(self.hero.rectangle):
                self.dis.is_collected = True

                self.boom_number += 1

            """hero interrupts root"""
            for tree in self.trees:
                if self.hero.rectangle:
                    if tree.rectangle.top < self.hero.rectangle.bottom < tree.rectangle.bottom:
                        if tree.rectangle.left <= self.hero.rectangle.right <= tree.rectangle.left + 5:
                            self.hero.x = tree.rectangle.left - 34
                        if tree.rectangle.right - 5 <= self.hero.rectangle.left <= tree.rectangle.right:
                            self.hero.x = tree.rectangle.right

                    if tree.rectangle.left - 17 < self.hero.rectangle.midtop[0] < tree.rectangle.right + 17:
                        if tree.rectangle.top - 2 <= self.hero.rectangle.bottom <= tree.rectangle.top + 3:
                            self.hero.y = tree.rectangle.top - 42
                        if tree.rectangle.bottom - 5 <= self.hero.rectangle.bottom <= tree.rectangle.bottom + 5:
                            self.hero.y = tree.rectangle.bottom - 35

            self.hero.update()

            self.enemy_spawner()
            self.draw()

    def draw(self):
        for tree in self.trees:
            tree.draw_under_bg(self.screen)
        self.screen.blit(self.bg, (0, 0))
        for tree in self.trees:
            tree.draw(self.screen)
        if self.boom:
            self.boom.draw(self.screen)

        for en in self.enemies:
            en.draw(self.screen)
        self.hero.draw(self.screen)

        self.dis.draw(self.screen, self.boom_number)

        self.screen.blit(self.bg_tree_top, (0, 0))
        self.dis.score(self.screen, self.score)

        pygame.display.update()

    def enemy_spawner(self):
        if time.time() - self.bat_timer > self.timer():
            self.bat_timer = time.time()
            self.enemies.append(Bat())
        if time.time() - self.frog_timer > self.timer() + 0.5:
            self.frog_timer = time.time()
            self.enemies.append(Frog())

    def dist(self, en_pos):
        return int(math.sqrt((self.hero.rectangle[0] - en_pos[0]) ** 2 + (self.hero.rectangle[1] - en_pos[1]) ** 2))

    def timer(self):
        """delta/seconds"""
        enemy_frequency = 1.6 / (5 * 60)
        increase = round(enemy_frequency * (time.time() - self.start_time), 3)
        if increase >= 1.6:
            return 0.4
        return 2 - increase
