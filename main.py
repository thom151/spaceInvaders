import pygame
from constants import *
from ship import *
from bullet import *
from aliens import *
import math


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
    Skull.containers = (aliens, drawable)
    Crab.containers = (aliens, drawable)
    Squid.containers = (aliens, drawable)
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
    to_left = False
    last_move_time = pygame.time.get_ticks()
    # GAME LOOP
    while True:
        curr_time = pygame.time.get_ticks()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        for obj in updatable:
            obj.update(dt)

        greatest_x = float("-inf")
        least_x = float("inf")
        rightmost = None
        leftmost = None

        for alien in aliens:
            if alien.position.x > greatest_x:
                greatest_x = alien.position.x
                rightmost = alien
            if alien.position.x < least_x:
                least_x = alien.position.x
                leftmost = alien

        if rightmost.position.x >= SCREEN_WIDTH:
            for alien in aliens:
                alien.position.y += ALIEN_WIDTH
            to_left = True
        if leftmost.position.x <= BORDER - 50:
            for alien in aliens:
                alien.position.y += ALIEN_WIDTH
            to_left = False

        for alien in aliens:
            if not to_left:
                alien.update(dt, len(aliens))
            else:
                alien.update(-dt, len(aliens))

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
