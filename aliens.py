import pygame
from constants import *


class Aliens(pygame.sprite.Sprite):
    def __init__(self, x, y):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)


class Skull(Aliens):
    def __init__(self, x, y):
        if hasattr(self, "container"):
            super().__init__(self.container, x, y)
        else:
            super().__init__(x, y)

        self.skull_structure = [
            [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0],
            [0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0],
            [1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1]
        ]

    def update(self, dt, alien_count):
        self.position.x += dt*(ALIEN_SPEED)

    def draw(self, screen):
        for i in range(len(self.skull_structure)):
            for j in range(len(self.skull_structure[i])):
                if self.skull_structure[i][j]:
                    rect = (self.position.x + (j*SIZE),
                            self.position.y + (i*SIZE),
                            SIZE, SIZE)
                    pygame.draw.rect(screen, WHITE, rect)


class Crab(Aliens):
    def __init__(self, x, y):
        if hasattr(self, "container"):
            super().__init__(self.container, x, y)
        else:
            super().__init__(x, y)
        self.crab_structure = [
            [0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
            [0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1],
            [1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1],
            [0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0]

        ]

    def draw(self, screen):
        for i in range(len(self.crab_structure)):
            for j in range(len(self.crab_structure[i])):
                if self.crab_structure[i][j]:
                    rect = (self.position.x + (j*SIZE),
                            self.position.y + (i*SIZE),
                            SIZE, SIZE)
                    pygame.draw.rect(screen, WHITE, rect)


class Squid(Aliens):
    def __init__(self, x, y):
        if hasattr(self, "container"):
            super().__init__(self.container, x, y)
        else:
            super().__init__(x, y)
        self.squid_structure = [
            [0, 0, 0, 1, 1, 0, 0, 0],
            [0, 0, 1, 1, 1, 1, 0, 0],
            [0, 1, 1, 1, 1, 1, 1, 0],
            [1, 1, 0, 1, 1, 0, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [0, 0, 1, 0, 0, 1, 0, 0],
            [0, 1, 0, 1, 1, 0, 1, 0],
            [1, 0, 1, 0, 0, 1, 0, 1]

        ]

    def draw(self, screen):
        for i in range(len(self.squid_structure)):
            for j in range(len(self.squid_structure[i])):
                if self.squid_structure[i][j]:
                    rect = (self.position.x + (j*SIZE),
                            self.position.y + (i*SIZE),
                            SIZE, SIZE)
                    pygame.draw.rect(screen, WHITE, rect)
