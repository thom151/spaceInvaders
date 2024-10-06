import pygame
from constants import *
from ship import *
from bullet import *


def main():

    # INITALIZATION
    pygame.init()
    print("Space Invaders!")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    # GROUPINGS
    drawable = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Ship.containers = (updatable, drawable)
    Bullet.containers = (drawable, updatable)

    ship = Ship(SCREEN_WIDTH / 2, SCREEN_HEIGHT-(SCREEN_HEIGHT/3))
    bullet = Bullet(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    # GAME LOOP
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        for obj in updatable:
            obj.update(dt)
        screen.fill("black")
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()

        dt = clock.tick(60)/1000


if __name__ == "__main__":
    main()
