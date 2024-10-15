import pygame
from constants import *
from bullet import *
import random


class Explosion(pygame.sprite.Sprite):
    def __init__(self, x, y):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        self.explode_struct = [
            [0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0],
            [0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
            [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
            [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0],
            [0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0]
        ]
        self.position = pygame.Vector2(x, y)
        self.frame_counter = 0
        self.explode_duration = 15

    def draw(self, screen):
        die_sfx.play()
        for i in range(len(self.explode_struct)):
            for j in range(len(self.explode_struct[0])):
                if self.explode_struct[i][j]:
                    rect = pygame.Rect(self.position.x + (j * SIZE),
                                       self.position.y + (i * SIZE),
                                       SIZE, SIZE)
                    pygame.draw.rect(screen, WHITE, rect)
        self.frame_counter += 1
        if self.frame_counter >= self.explode_duration:
            self.kill()


class SpaceShipExplosion(Explosion):
    def __init__(self, x, y):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()


class Aliens(pygame.sprite.Sprite):
    def __init__(self, x, y):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.rect = pygame.Rect(x, y, 39, 24)
        self.default = True
        self.sound_index = 0
        self.shoot_timer = 0

    def update(self, dt, alien_count):
        self.position.x += dt*(ALIEN_SPEED)
        self.default = not self.default
        self.rect.topleft = (self.position.x, self.position.y)
        move_sounds[self.sound_index].play()
        self.sound_index = (self.sound_index + 1) % 4

    def shoot(self):
        if self.shoot_timer > 0:
            return
        self.shoot_timer = SHIP_SHOOT_COOLDOWN
        shot = AlienBullet(self.position.x+(ALIEN_WIDTH*SIZE/2),
                           self.position.y + 50)
        shot.velocity = pygame.Vector2(0, -1) * BULLET_SPEED


class Skull(Aliens):
    def __init__(self, x, y):
        if hasattr(self, "containers"):
            super().__init__(x, y)
        else:
            super().__init__(x, y)
        self.points = 10
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
        if hasattr(self, "containers"):
            super().__init__(x, y)
        else:
            super().__init__(x, y)
        self.points = 20
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
        if hasattr(self, "containers"):
            super().__init__(x, y)
        else:
            super().__init__(x, y)
        self.points = 30
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


class SpaceShip(Aliens):  # 9:41
    def __init__(self, x, y):
        if hasattr(self, "containers"):
            super().__init__(x, y)
        else:
            super().__init__(x, y)
        self.points = random.randint(100, 150)
        self.spaceship_struct = [
            [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
            [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
            [0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        ]
        self.rect = pygame.Rect(x, y, 64, 24)

    def draw(self, screen):
        for i in range(len(self.spaceship_struct)):
            for j in range(len(self.spaceship_struct[i])):
                if self.spaceship_struct[i][j]:
                    rect = (self.position.x + (j*UFO_SIZE),
                            self.position.y + (i*UFO_SIZE),
                            UFO_SIZE, UFO_SIZE)
                    pygame.draw.rect(screen, RED, rect)

    def update(self, dt):
        self.position.x += dt*SPACESHIP_SPEED
        self.rect.topleft = (self.position.x, self.position.y)
        if self.position.x >= SCREEN_WIDTH:
            self.kill()
