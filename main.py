import pygame
from constants import *
from ship import *
from bullet import *
from aliens import *
import math
import random
from borders import *


def main():

    # INITALIZATION
    pygame.init()
    pygame.mixer.init()
    print("Space Invaders!")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    next_alien_time = pygame.time.get_ticks()
    alien_spawn_interval = 80

    font = pygame.font.Font('fonts/font.ttf', 32)
    text = font.render("SCORE", True, WHITE)
    textRect = text.get_rect()
    textRect.center = (SCREEN_WIDTH//2, 30)

    # GROUPINGS
    drawable = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    aliens = pygame.sprite.Group()
    alien_bullets = pygame.sprite.Group()
    borders = pygame.sprite.Group()
    alien_explosion = pygame.sprite.Group()
    spaceship = pygame.sprite.Group()

    SpaceShip.containers = (updatable)
    Ship.containers = (updatable, drawable)
    Bullet.containers = (drawable, updatable)
    AlienBullet.containers = (drawable, updatable)
    Skull.containers = (aliens)
    Crab.containers = (aliens)
    Squid.containers = (aliens)
    Bullet.containers = (bullets, updatable, drawable)
    AlienBullet.containers = (drawable, updatable, alien_bullets)
    Border.containers = (borders, drawable)
    Explosion.containers = (alien_explosion)

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
    ufo_time_appearance = last_move_time + random.randint(5000, 15000)
    print("Time: ", ufo_time_appearance/1000)
    adjustment = 25
    shield = Border(75 + adjustment, 520)
    shield2 = Border(197 + adjustment, 520)
    shield3 = Border(319 + adjustment, 520)
    shield4 = Border(441 + adjustment, 520)
    ufo = None

    pre_game_alien_rendering(
        screen, drawable, aliens_struct, alien_spawn_interval)

    while ship.lives > 0:

        curr_time = pygame.time.get_ticks()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        for obj in updatable:
            obj.update(dt)

        score = font.render(str(ship.score), True, WHITE)
        scoreRect = score.get_rect()
        scoreRect.center = (SCREEN_WIDTH//2, 70)
        lives = font.render(f"LIVES: {str(ship.lives)}", True, WHITE)
        livesRect = lives.get_rect()
        livesRect.center = (100, SCREEN_HEIGHT-50)

        if alien_bullets_to_ship(alien_bullets, ship, screen):
            ship.lives -= 1
            if ship.lives == 0:
                return
            else:
                ship.position.x = SCREEN_WIDTH / 2
                ship.position.y = SCREEN_HEIGHT-(SCREEN_HEIGHT/5)
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

        for bullet in bullets:
            if ufo is not None:
                if bullet.collides_with(ufo):
                    ufo.kill()
                    bullet.kill()
                    ship.score += ufo.points
            for alien in aliens:
                if bullet.collides_with(alien):
                    bullet.kill()
                    alien.kill()
                    explosion_sprite = Explosion(
                        alien.position.x, alien.position.y)
                    drawable.add(explosion_sprite)
                    ship.score += alien.points
            for alien_bullet in alien_bullets:
                if bullet.collides_with(alien_bullet):
                    alien_bullet.kill()
                    bullet.kill()

        border_to_bullets(borders, bullets, alien_bullets, screen)
        if curr_time >= ufo_time_appearance:
            ufo = SpaceShip(0, 100)
            drawable.add(ufo)
            ufo_time_appearance = pygame.time.get_ticks() + random.randint(20000, 35000)

        screen.fill("black")
        screen.blit(text, textRect)
        screen.blit(score, scoreRect)
        screen.blit(lives, livesRect)
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()

        dt = clock.tick(60)/1000


def bullet_to_alien(bullets, aliens, alien_bullets, screen, ship):
    for bullet in bullets:
        for alien in aliens:
            if bullet.collides_with(alien):
                bullet.kill()
                alien.animate_kill(screen)
                alien.kill()
        for alien_bullet in alien_bullets:
            if bullet.collides_with(alien_bullet):
                alien_bullet.kill()
                bullet.kill()


def alien_bullets_to_ship(alien_bullets, ship, screen):
    for alien_bullet in alien_bullets:
        if alien_bullet.collides_with(ship):
            alien_bullet.kill()
            return True
    return False


def border_to_bullets(borders, bullets, alien_bullets, screen):
    for border in borders:
        for bullet in bullets:
            coordinates = border.check_border_collision2(bullet)
            if coordinates is not None:
                print(coordinates)
                border.damage2(coordinates[0], coordinates[1])
                bullet.kill()
        for alien_bullet in alien_bullets:
            coordinate_alien = border.check_border_collision2(alien_bullet)
            if coordinate_alien is not None:
                print("alien", coordinate_alien)
                border.damage2(coordinate_alien[0], coordinate_alien[1])
                alien_bullet.kill()


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


def pre_game_alien_rendering(screen, drawable, aliens_struct, alien_spawn_interval):
    curr_time = pygame.time.get_ticks()
    next_alien_time = curr_time
    alien_spawn_index = 0

    while alien_spawn_index < ALIEN_ROWS * ALIEN_COLS:
        curr_time = pygame.time.get_ticks()

        if curr_time >= next_alien_time:
            i = alien_spawn_index // ALIEN_COLS
            j = alien_spawn_index % ALIEN_COLS

            alien_to_show = aliens_struct[i][j]
            drawable.add(alien_to_show)

            alien_spawn_index += 1
            next_alien_time = curr_time + alien_spawn_interval  # Set next alien time

        screen.fill("black")
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()

        pygame.time.Clock().tick(60)

    return


if __name__ == "__main__":
    main()
