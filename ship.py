import pygame
from constants import *
from bullet import *


class Ship(pygame.sprite.Sprite):
    def __init__(self, x, y):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init_()
        self.x = int(x)
        self.y = int(y)
        self.shoot_timer = 0
        self._spacebar_pressed = False
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.ship_structure = [
            [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        ]

    def draw(self, screen):
        for i in range(SHIP_HEIGHT):
            for j in range(SHIP_WIDTH):
                if self.ship_structure[i][j]:
                    rect = (self.position.x+(j*SIZE), self.position.y +
                            (i*SIZE), SIZE, SIZE)
                    pygame.draw.rect(screen, GREEN, rect)

    def update(self, dt):
        self.shoot_timer -= dt
        spacebar_pressed = False
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.move(-dt)
        if keys[pygame.K_d]:
            self.move(dt)
        if keys[pygame.K_SPACE]:
            if not self._spacebar_pressed:
                self.shoot()
                self._spacebar_pressed = True
        else:
            self._spacebar_pressed = False

    def move(self, dt):
        self.position.x += dt*SHIP_SPEED

    def shoot(self):
        if self.shoot_timer > 0:
            return
        self.shoot_timer = SHIP_SHOOT_COOLDOWN
        shot = Bullet(self.position.x+(SHIP_WIDTH*SIZE/2), self.position.y)
        shot.velocity = pygame.Vector2(0, -1) * BULLET_SPEED
