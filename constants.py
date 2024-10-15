import pygame

# Use the dummy audio driver to bypass sound initialization

pygame.mixer.init()
pygame.font.init()


SCREEN_WIDTH = 672
SCREEN_HEIGHT = 768
SIZE = 3
SOUND_INDEX = 0

SKULL_AND_CRAB_ROWS = 2
ALIEN_ROWS = 5
SQUID_ROWS = 1
ALIEN_COLS = 11
ALIEN_WIDTH = 45
ALIEN_SPEED = 300
ALIEN_DELAY = 500
SPACESHIP_SPEED = 160
UFO_SIZE = 4

BORDER = 100
COL_SPACING = 9


SHIP_HEIGHT = 8
SHIP_WIDTH = 13
SHIP_SPEED = 150
SHIP_SHOOT_COOLDOWN = 0.3

BULLET_HEIGHT = 2
BULLET_WIDTH = 1
BULLET_SPEED = 500

RED = (255, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

shoot_sfx = pygame.mixer.Sound("sounds/sample0.wav")
die_sfx = pygame.mixer.Sound("sounds/sample1.wav")
move1 = pygame.mixer.Sound("sounds/fastinvader1.wav")
move2 = pygame.mixer.Sound("sounds/fastinvader2.wav")
move3 = pygame.mixer.Sound("sounds/fastinvader3.wav")
move4 = pygame.mixer.Sound("sounds/fastinvader4.wav")

move_sounds = [move1, move2, move3, move4]
ufo_sound = pygame.mixer.Sound("sounds/ufo_lowpitch.wav")
ship_explosion = pygame.mixer.Sound("sounds/explosion.wav")

font = pygame.font.Font('fonts/font.ttf')
