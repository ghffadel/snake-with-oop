from snake import Snake
from cube import Cube
from constants import Constants
from random import randint
import pygame


class Window:
	def __init__(self):
		self.snake = Snake([Constants.WIDTH // 2, Constants.HEIGHT // 2])
		self.fruit = Cube(Constants.COLORS["green"], [randint(10, Constants.WIDTH - 10), randint(10, Constants.HEIGHT - 10)])
		self.window = pygame.display.set_mode((Constants.WIDTH, Constants.HEIGHT))

	def draw_window(self):
		self.window.fill(Constants.COLORS["black"])
		x = y = 0
		for i in range(Constants.ROWS):
			x += Constants.WIDTH // Constants.ROWS
			y += Constants.WIDTH // Constants.ROWS
			pygame.draw.line(self.window, Constants.COLORS["white"], (x, 0), (x, Constants.HEIGHT))
			pygame.draw.line(self.window, Constants.COLORS["white"], (0, y), (Constants.WIDTH, y))

		pygame.display.update()
