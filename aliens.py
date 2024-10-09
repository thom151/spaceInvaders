import pygame
from constants import *
from bullet import *


class Aliens(pygame.sprite.Sprite):
    def __init__(self, x, y):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.default = True
        self.shoot_timer = 0

    def update(self, dt, alien_count):
        self.position.x += dt*(ALIEN_SPEED)
        self.default = not self.default

    def shoot(self):
        if self.shoot_timer > 0:
            return
        self.shoot_timer = SHIP_SHOOT_COOLDOWN
        shot = AlienBullet(self.position.x+(ALIEN_WIDTH*SIZE/2),
                           self.position.y + 50)
        shot.velocity = pygame.Vector2(0, -1) * BULLET_SPEED


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

        self.skull_structure2 = [
            [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0],
            [0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0],
            [0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0]
        ]

    def draw(self, screen):
        if self.default:
            for i in range(len(self.skull_structure)):
                for j in range(len(self.skull_structure[i])):
                    if self.skull_structure[i][j]:
                        rect = (self.position.x + (j*SIZE),
                                self.position.y + (i*SIZE),
                                SIZE, SIZE)
                        pygame.draw.rect(screen, WHITE, rect)
        else:
            for i in range(len(self.skull_structure)):
                for j in range(len(self.skull_structure[i])):
                    if self.skull_structure2[i][j]:
                        rect = (self.position.x + (j*SIZE),
                                self.position.y + (i*SIZE),
                                SIZE, SIZE)
                        pygame.draw.rect(screen, WHITE, rect)

    def __repr__(self):
        return "Skull"


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

        self.crab_structure2 = [
            [0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
            [1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
            [1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1],
            [1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0]

        ]

    def draw(self, screen):
        if self.default:
            for i in range(len(self.crab_structure)):
                for j in range(len(self.crab_structure[i])):
                    if self.crab_structure[i][j]:
                        rect = (self.position.x + (j*SIZE),
                                self.position.y + (i*SIZE),
                                SIZE, SIZE)
                        pygame.draw.rect(screen, WHITE, rect)
        else:
            for i in range(len(self.crab_structure)):
                for j in range(len(self.crab_structure[i])):
                    if self.crab_structure2[i][j]:
                        rect = (self.position.x + (j*SIZE),
                                self.position.y + (i*SIZE),
                                SIZE, SIZE)
                        pygame.draw.rect(screen, WHITE, rect)

    def __repr__(self):
        return "Crab"


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

        self.squid_structure2 = [
            [0, 0, 0, 1, 1, 0, 0, 0],
            [0, 0, 1, 1, 1, 1, 0, 0],
            [0, 1, 1, 1, 1, 1, 1, 0],
            [1, 1, 0, 1, 1, 0, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [0, 1, 0, 1, 1, 0, 1, 0],
            [1, 0, 0, 0, 0, 0, 0, 1],
            [0, 1, 0, 0, 0, 0, 1, 0]

        ]

    def draw(self, screen):
        if self.default:
            for i in range(len(self.squid_structure)):
                for j in range(len(self.squid_structure[i])):
                    if self.squid_structure[i][j]:
                        rect = (self.position.x + (j*SIZE),
                                self.position.y + (i*SIZE),
                                SIZE, SIZE)
                        pygame.draw.rect(screen, WHITE, rect)
        else:
            for i in range(len(self.squid_structure)):
                for j in range(len(self.squid_structure[i])):
                    if self.squid_structure2[i][j]:
                        rect = (self.position.x + (j*SIZE),
                                self.position.y + (i*SIZE),
                                SIZE, SIZE)
                        pygame.draw.rect(screen, WHITE, rect)

    def __repr__(self):
        return "Squid"
