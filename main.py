from window import Window
from constants import Constants
from snake import Snake
from cube import Cube
import pygame

def draw_snake (cubes):
    for cube in cubes:
        window.draw_cube(cube)

def draw_elements ():
    window.draw_window()

    draw_snake(window.snake.cubes)
    draw_snake(window.bot.cubes)

    window.draw_cube(window.fruit)

def handle_movement ():
    window.snake.move()
    window.bot.move(True, window.fruit.pos)

def handle_collisions ():
    player_positions = [cube.pos for cube in window.snake.cubes]
    bot_positions = [cube.pos for cube in window.bot.cubes]

    for position in player_positions:
        if player_positions.count(position) > 1 or position in bot_positions:
            exit()

    if window.snake.check_collision(window.fruit) or window.bot.check_collision(window.fruit):
        window.fruit.pos = window.generate_position()

def main ():
    global window

    window = Window()
    clock = pygame.time.Clock()

    while True:
        pygame.time.delay(Constants.FRAMERATE)
        clock.tick(10)

        draw_elements()

        pygame.display.update()

        handle_movement()
        
        handle_collisions()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

if __name__ == "__main__":
    main()