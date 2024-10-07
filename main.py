import pygame
from constants import *
from ship import *
from bullet import *
from aliens import *


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
    bullets = pygame.sprite.Group()
    aliens = pygame.sprite.Group()

    Ship.containers = (updatable, drawable)
    Bullet.containers = (drawable, updatable)
    Skull.containers = (aliens, drawable, updatable)
    Crab.containers = (aliens, drawable, updatable)
    Squid.containers = (aliens, drawable, updatable)
    Bullet.containers = (bullets, updatable, drawable)

    crabs = [[None for j in range(ALIEN_COLS)]
             for i in range(SKULL_AND_CRAB_ROWS)]

    skulls = [[None for j in range(ALIEN_COLS)]
              for i in range(SKULL_AND_CRAB_ROWS)]
    squids = [None for j in range(ALIEN_COLS)]

    for i in range(ALIEN_ROWS):
        for j in range(ALIEN_COLS):
            if i < 1:
                squids[j] = (Squid(BORDER + (ALIEN_WIDTH*j),
                             SCREEN_HEIGHT/4+(i*ALIEN_WIDTH)))
            elif 1 <= i <= 2:
                crabs[i-1][j-1] = (Crab(BORDER+(ALIEN_WIDTH*j),
                                        SCREEN_HEIGHT/4+(i*ALIEN_WIDTH)))
            else:
                skulls[i-3][j-3] = (Skull(BORDER + (ALIEN_WIDTH*j),
                                          SCREEN_HEIGHT/4+(i*ALIEN_WIDTH)))

    ship = Ship(SCREEN_WIDTH / 2, SCREEN_HEIGHT-(SCREEN_HEIGHT/5))

    # GAME LOOP
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        for obj in updatable:
            obj.update(dt)

        for alien in aliens:
            for bullet in bullets:
                if bullet.collides_with(alien):
                    bullet.kill()
                    alien.kill()

        screen.fill("black")
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()

        dt = clock.tick(60)/1000


if __name__ == "__main__":
    main()
