import pygame
from constants import *


class Border(pygame.sprite.Sprite):
    def __init__(self, x, y):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init()
        self.position = pygame.Vector2(x, y)
        self.image = pygame.Surface((140, 100), pygame.SRCALPHA)
        self.image.fill(GREEN)
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(
            topleft=(self.position.x, self.position.y))
        self.structure = [


            [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
            [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
            [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0,
                0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
                0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0,
                0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0,
                0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0,
                0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
        ]
        self.width = len(self.structure[0])
        self.height = len(self.structure)

    def damage(self, rel_x, rel_y, radius=6):
        for dx in range(-radius, radius):
            for dy in range(-radius, radius):
                dist = (dx**2 + dy**2)**0.5
                if dist <= radius:
                    pixel_x = rel_x + dx
                    pixel_y = rel_y + dy

                    if 0 <= pixel_x < self.image.get_width() and 0 <= pixel_y < self.image.get_height():
                        self.image.set_at((pixel_x, pixel_y), (0, 0, 0, 0))
                        self.mask = pygame.mask.from_surface(self.image)

    def check_border_collision(self, bullet):
        if bullet.rect.colliderect(self.rect):
            rel_x = bullet.rect.x - self.rect.x
            rel_y = bullet.rect.y - self.rect.y
            if 0 <= rel_x < self.image.get_width() and 0 <= rel_y < self.image.get_height():
                if self.mask.get_at((rel_x, rel_y)):
                    return (rel_x, rel_y)
        return None

    def check_border_collision2(self, bullet, block_size=SIZE):
        rel_x = bullet.rect.x - self.rect.x
        rel_y = bullet.rect.y - self.rect.y

        grid_x = rel_x // block_size  # Find which column in the grid the bullet hits
        grid_y = rel_y // block_size  # Find which row in the grid the bullet hits

        if 0 <= grid_x < self.width and 0 <= grid_y < self.height:
            if self.structure[grid_y][grid_x] == 1:
                return grid_x, grid_y  # Return the exact grid coordinates of the hit
        return None  # No collision or already destroyed

    def damage2(self, grid_x, grid_y, radius=2):
        for dx in range(-radius, radius+1):
            for dy in range(-radius, radius+1):
                # Calculate distance from the impact point
                dist = (dx**2 + dy**2)**0.5
                if dist <= radius:  # If within the damage radius
                    pixel_x = grid_x + dx
                    pixel_y = grid_y + dy
                    if 0 <= pixel_x < self.width and 0 <= pixel_y < self.height:
                        self.structure[pixel_y][pixel_x] = 0

    def draw(self, screen):
        block_size = SIZE
        for y in range(self.height):
            for x in range(self.width):
                if self.structure[y][x] == 1:  # Only draw intact blocks
                    pygame.draw.rect(screen, (0, 255, 0), (self.rect.x + x * block_size,
                                     self.rect.y + y * block_size, block_size, block_size))
