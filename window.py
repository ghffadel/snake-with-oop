from snake import Snake
from cube import Cube
from constants import Constants
from random import randint


class Window:
	def __init__(self):
		self.snake = Snake([Constants.WIDTH // 2, Constants.HEIGHT // 2])
		self.fruit = Cube(Constants.COLORS["green"], [randint(10, Constants.WIDTH - 10), randint(10, Constants.HEIGHT - 10)])
		