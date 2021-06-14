from snake import Snake
from cube import Cube
from constants import Constants
from random import randint
import pygame


class Window:
    def __init__(self):
        self.snake = Snake("green", (2, 2))
        self.bot = Snake("blue", (Constants.ROWS - 2, Constants.ROWS - 8))
        # Randint do fruit de (0, 19) em X e (0, 14) em Y
        self.fruit = Cube(Constants.COLORS["red"], self.generate_position())
        self.window = pygame.display.set_mode(
            (Constants.WIDTH, Constants.HEIGHT)
        )

    def generate_position(self):
        while True:
            pos = (
                randint(0, Constants.ROWS - 1),
                randint(0, Constants.ROWS - 6),
            )
            if pos not in [
                cube.pos for cube in self.snake.cubes
            ] and pos not in [cube.pos for cube in self.bot.cubes]:
                return pos

    def draw_window(self):
        self.window.fill(Constants.COLORS["black"])
        x = y = 0
        for i in range(Constants.ROWS):
            x += Constants.WIDTH // Constants.ROWS
            y += Constants.WIDTH // Constants.ROWS
            pygame.draw.line(
                self.window,
                Constants.COLORS["white"],
                (x, 0),
                (x, Constants.HEIGHT),
            )
            pygame.draw.line(
                self.window,
                Constants.COLORS["white"],
                (0, y),
                (Constants.WIDTH, y),
            )

    def draw_cube(self, cube):
        distance = Constants.WIDTH // Constants.ROWS
        x, y = cube.pos
        pygame.draw.rect(
            self.window,
            cube.color,
            (x * distance + 1, y * distance + 1, distance - 2, distance - 2),
        )
