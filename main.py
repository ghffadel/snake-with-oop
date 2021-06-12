from window import Window
from constants import Constants
from snake import Snake
from cube import Cube
import pygame


def main():
    window = Window()
    clock = pygame.time.Clock()
    s = Snake((Constants.ROWS // 2, Constants.ROWS // 3))

    flag = True

    while flag:
        pygame.time.delay(Constants.FRAMERATE)
        clock.tick(10)
        window.draw_window()
        for cube in s.cubes:
            window.draw_cube(cube)

        window.draw_cube(window.fruit)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()


main()
