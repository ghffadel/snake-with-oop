import pygame
from cube import Cube
from constants import Constants


class Snake:

	def __init__(self, pos):
		self.head = Cube(Constants.COLORS["green"], pos)
		self.head_direction = (0, 0)
		self.cubes = []
		self.size = 1

	def move(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()

			keys = pygame.key.get_pressed()

			for key in keys:
				if keys[pygame.K_LEFT]:
					self.head_direction = (-1, 0)

				elif keys[pygame.K_RIGHT]:
					self.head_direction = (1, 0)

				elif keys[pygame.K_UP]:
					self.head_direction = (0, -1)

				elif keys[pygame.K_DOWN]:
					self.head_direction = (0, 1)
		
		x, y = self.head.pos
		dx, dy = self.head_direction

		# if not (0 <= x < Constants.ROWS - 1 and 0 <= y < Constants.ROWS - 6):
		# 	self.head.pos = 

		self.head.pos = (x + dx, y + dy)

		self.cubes.append(Cube(Constants.COLORS["green"], self.head.pos))

		if len(self.cubes) > self.size:
			del self.cubes[0]

	def check_collision(self, fruit):
		if self.cubes[-1].pos == fruit.pos:
			self.size += 1
			return True

		return False