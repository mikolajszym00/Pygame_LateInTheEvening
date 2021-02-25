import pygame

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    from main_menu.main_menu import MainMenu
    mainMenu = MainMenu(screen)
    mainMenu.run()
