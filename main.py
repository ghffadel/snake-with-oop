from window import Window
from constants import Constants
import pygame


def main():
    window = Window()
    clock = pygame.time.Clock()

    flag = True
    while flag:
        pygame.time.delay(Constants.FRAMERATE)
        clock.tick(10)
        window.draw_window()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()


main()
