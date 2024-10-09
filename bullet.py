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
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)

    def draw(self, screen):
        rect = (self.position.x, self.position.y, 2, 2*3)
        pygame.draw.rect(screen, WHITE, rect)

    def update(self, dt):
        self.position.y -= BULLET_SPEED * dt

    def collides_with(self, other):
        return self.position.distance_to(other.position) <= (ALIEN_WIDTH + 6)/2


class AlienBullet(Bullet):
    def update(self, dt):
        self.position.y += BULLET_SPEED * dt
