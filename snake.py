from cube import Cube
from constants import Constants


class Snake:
	def __init__(self, pos):
		self.cubes = [Cube(Constants.COLORS["green"], pos)]

