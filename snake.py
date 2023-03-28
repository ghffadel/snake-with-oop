import pygame
from cube import Cube
from constants import Constants


class Snake:
    def __init__(self, color, pos):
        self.color = color
        self.head = Cube(Constants.COLORS[color], pos)
        self.head_direction = (0, 0)
        self.cubes = []
        self.size = 1

    def move(self, bot=False, fruit=(0, 0)):
        if bot:
            x, y = self.head.pos

            if x > fruit[0]:
                self.head_direction = (-1, 0)

            elif x < fruit[0]:
                self.head_direction = (1, 0)

            elif y > fruit[1]:
                self.head_direction = (0, -1)

            else:
                self.head_direction = (0, 1)

        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

                keys = pygame.key.get_pressed()

                if keys[pygame.K_LEFT]:
                    self.head_direction = (-1, 0)

                elif keys[pygame.K_RIGHT]:
                    self.head_direction = (1, 0)

                elif keys[pygame.K_UP]:
                    self.head_direction = (0, -1)

                elif keys[pygame.K_DOWN]:
                    self.head_direction = (0, 1)

        self.update_position()

    def update_position(self):
        x, y = self.head.pos
        dx, dy = self.head_direction

        limit_x = Constants.ROWS
        limit_y = Constants.ROWS - 5

        if not (0 <= x < limit_x and 0 <= y < limit_y):

            if self.head.pos[0] > limit_x:
                x = -1
                y = self.head.pos[1]

            elif self.head.pos[0] < 0:
                x = limit_x
                y = self.head.pos[1]

            elif self.head.pos[1] > limit_y:
                x = self.head.pos[0]
                y = -1

            elif self.head.pos[1] < 0:
                x = self.head.pos[0]
                y = limit_y

        self.head.pos = (x + dx, y + dy)

        self.cubes.append(Cube(self.color, self.head.pos))

        if len(self.cubes) > self.size:
            del self.cubes[0]

    def check_collision(self, fruit):
        if self.cubes[-1].pos == fruit.pos:
            self.size += 1
            return True

        return False
