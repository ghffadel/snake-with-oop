import pygame
from cube import Cube
from constants import Constants


class Snake:

	body = []

	def __init__(self, pos):
		self.cubes = [Cube(Constants.COLORS["green"], pos)]
		self.body.append(self.cubes)

	def move(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()

			keys = pygame.key.get_pressed()

			for key in keys:
				if keys[pygame.K_LEFT]:
					# self.dirnx = -1
					# self.dirny = 0
					print("esquerda")
					print(len(self.body))

				elif keys[pygame.K_RIGHT]:
					# self.dirnx = 1
					# self.dirny = 0
					print("direita")
					print(len(self.body))

				elif keys[pygame.K_UP]:
					# self.dirnx = 0
					# self.dirny = -1
					print("cima")
					print(len(self.body))

				elif keys[pygame.K_DOWN]:
					# self.dirnx = 0
					# self.dirny = 1
					print("baixo")
					print(len(self.body))
