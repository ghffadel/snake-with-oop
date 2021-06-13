import pygame
from cube import Cube
from constants import Constants


class Snake:

	def __init__(self, pos):
		self.cubes = [Cube(Constants.COLORS["green"], pos)]
		self.size = 1

	def move(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()

			keys = pygame.key.get_pressed()

			x, y = self.cubes[-1].pos

			for key in keys:
				if keys[pygame.K_LEFT]:
					self.cubes[-1].direction = (-1, 0)

				elif keys[pygame.K_RIGHT]:
					self.cubes[-1].direction = (1, 0)

				elif keys[pygame.K_UP]:
					self.cubes[-1].direction = (0, -1)

				elif keys[pygame.K_DOWN]:
					self.cubes[-1].direction = (0, 1)

			dx, dy = self.cubes[-1].direction

			self.cubes[-1].pos = (x + dx, y + dy)

			self.cubes.append(Cube(Constants.COLORS["green"], self.cubes[0].pos))

			if len(self.cubes) > self.size:
				del self.cubes[0]

	def check_collision(self, fruit):
		if self.cubes[-1] == fruit.pos:
			self.size += 1

