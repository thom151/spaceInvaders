import pygame
from constants import *
from ship import *
from bullet import *
from aliens import *
import math
import random


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
    AlienBullet.containers = (drawable, updatable)
    Skull.containers = (aliens, drawable)
    Crab.containers = (aliens, drawable)
    Squid.containers = (aliens, drawable)
    Bullet.containers = (bullets, updatable, drawable)

    aliens_struct = [[None for j in range(ALIEN_COLS)]
                     for i in range(ALIEN_ROWS)]

    for i in range(ALIEN_ROWS):
        for j in range(ALIEN_COLS):
            if i < 1:
                aliens_struct[i][j] = (Squid(BORDER + (ALIEN_WIDTH*j),
                                             SCREEN_HEIGHT/4+(i*ALIEN_WIDTH)))
            elif 1 <= i <= 2:
                aliens_struct[i][j] = (Crab(BORDER+(ALIEN_WIDTH*j),
                                            SCREEN_HEIGHT/4+(i*ALIEN_WIDTH)))
            else:
                aliens_struct[i][j] = (Skull(BORDER + (ALIEN_WIDTH*j),
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
        bootommost = None
        greatest_y = float("-inf")

        for alien in aliens:
            if alien.position.x > greatest_x:
                greatest_x = alien.position.x
                rightmost = alien
            if alien.position.x < least_x:
                least_x = alien.position.x
                leftmost = alien
            if alien.position.y > greatest_y:
                greatest_y = alien.position.y
                bottommost = alien

        if bottommost.position.y >= ship.position.y:
            print("haha")
            return

        if curr_time - last_move_time > len(aliens)*10:

            bottom_list = get_lowest_list(aliens_struct)
            alien_to_shoot = random.choice(bottom_list)
            if alien_to_shoot is not None:
                alien_to_shoot.shoot()

            for alien in aliens:
                if not to_left:
                    alien.update(dt, len(aliens))
                else:
                    alien.update(-dt, len(aliens))
            last_move_time = curr_time

            if rightmost.position.x >= SCREEN_WIDTH-50:
                for alien in aliens:
                    alien.position.y += 20
                    to_left = True
            if leftmost.position.x <= 0:
                for alien in aliens:
                    alien.position.y += 20
                    to_left = False

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


def get_lowest_list(aliens):
    list = []

    for j in range(ALIEN_COLS):
        greatest_alien = None
        greatest_y = float("-inf")
        for i in range(ALIEN_ROWS):
            if aliens[i][j].position.y > greatest_y and aliens[i][j].alive():
                greatest_y = aliens[i][j].position.y
                greatest_alien = aliens[i][j]
        list.append(greatest_alien)
    return list


if __name__ == "__main__":
    main()
