import pygame
from constants import *


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        self.x = x
        self.y = y
        self.default = True
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.rect = pygame.Rect(self.position.x, self.position.y, 2, 6)

    def draw(self, screen):
        rect = (self.position.x, self.position.y, 2, 2*3)
        pygame.draw.rect(screen, WHITE, rect)
        self.rect.topleft = (self.position.x, self.position.y)

    def update(self, dt):
        self.position.y -= BULLET_SPEED * dt
        self.rect.topleft = (self.position.x, self.position.y)

    def collides_with(self, other):
        return self.rect.colliderect(other.rect)


class AlienBullet(Bullet):
    def __init__(self, x, y):
        if hasattr(self, "containers"):
            super().__init__(x, y)
        else:
            super().__init__(x, y)
        self.default = True
        self.structure = [
            [1, 0, 0],
            [0, 1, 0],
            [0, 0, 1],
            [0, 1, 0],
            [1, 0, 0],
            [0, 1, 0],
            [0, 0, 1]
        ]

        self.structure2 = [
            [0, 0, 1],
            [0, 1, 0],
            [1, 0, 0],
            [0, 1, 0],
            [0, 0, 1],
            [0, 1, 0],
            [1, 0, 0]
        ]
        self.rect = pygame.Rect(self.position.x, self.position.y, 3*2, 7*2)

    def update(self, dt):
        self.position.y += (BULLET_SPEED-10) * dt
        self.default = not self.default
        self.rect.topleft = (self.position.x, self.position.y)

    def draw(self, screen):
        self.rect.topleft = (self.position.x, self.position.y)
        if self.default:
            for i in range(7):
                for j in range(3):
                    if self.structure[i][j]:
                        rect = (self.position.x + (j*2),
                                self.position.y + (i*2),
                                2, 2)
                        pygame.draw.rect(screen, WHITE, rect)
        else:
            for i in range(7):
                for j in range(3):
                    if self.structure2[i][j]:
                        rect = (self.position.x + (j*2),
                                self.position.y + (i*2),
                                2, 2)
                        pygame.draw.rect(screen, WHITE, rect)
