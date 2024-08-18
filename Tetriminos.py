from Colors import *
from Screen import *

def ORANGE_RICKY(screen,x,y,square_size):
    pygame.draw.rect(screen, ORANGE, (x, y, square_size, square_size))
    pygame.draw.rect(screen, ORANGE, (x + square_size, y, square_size, square_size))
    pygame.draw.rect(screen, ORANGE, (x + 2 * square_size, y, square_size, square_size))
    pygame.draw.rect(screen, ORANGE, (x + 2 * square_size, y - square_size, square_size, square_size))


def BLUE_RICKY(screen,x,y, square_size):
    pygame.draw.rect(screen, BLAU, (x, y, square_size, square_size))
    pygame.draw.rect(screen, BLAU, (x, y - square_size, square_size, square_size))
    pygame.draw.rect(screen, BLAU, (x + square_size, y, square_size, square_size))
    pygame.draw.rect(screen, BLAU, (x + 2 * square_size, y, square_size, square_size))

def CLEVELAND_Z(screen, x, y, square_size):
    pygame.draw.rect(screen, LILA, (x, y, square_size, square_size))
    pygame.draw.rect(screen, LILA, (x + square_size, y, square_size, square_size))
    pygame.draw.rect(screen, LILA, (x + square_size, y + square_size, square_size, square_size))
    pygame.draw.rect(screen, LILA, (x + 2 * square_size, y + square_size, square_size, square_size))

def RHODE_ISLAND_Z(screen, x, y, square_size):
    pygame.draw.rect(screen, HELLBLAU, (x, y, square_size, square_size))
    pygame.draw.rect(screen, HELLBLAU, (x + square_size, y, square_size, square_size))
    pygame.draw.rect(screen, HELLBLAU, (x + square_size, y - square_size, square_size, square_size))
    pygame.draw.rect(screen, HELLBLAU, (x + 2 * square_size, y - square_size, square_size, square_size))

def HERO(screen, x, y, square_size):
    pygame.draw.rect(screen, ROT, (x + square_size, y, square_size, square_size))
    pygame.draw.rect(screen, ROT, (x + square_size, y + square_size, square_size, square_size))
    pygame.draw.rect(screen, ROT, (x + square_size, y + 2 * square_size, square_size, square_size))
    pygame.draw.rect(screen, ROT, (x + square_size, y - square_size, square_size, square_size))

def TEEWEE(screen, x, y, square_size):
    pygame.draw.rect(screen, GELB, (x, y, square_size, square_size))
    pygame.draw.rect(screen, GELB, (x + square_size, y, square_size, square_size))
    pygame.draw.rect(screen, GELB, (x + square_size, y - square_size, square_size, square_size))
    pygame.draw.rect(screen, GELB, (x + 2 * square_size, y, square_size, square_size))

def SMASHBOY(screen, x, y, square_size):
    pygame.draw.rect(screen, GRUEN, (x, y, square_size, square_size))
    pygame.draw.rect(screen, GRUEN, (x + square_size, y, square_size, square_size))
    pygame.draw.rect(screen, GRUEN, (x, y - square_size, square_size, square_size))
    pygame.draw.rect(screen, GRUEN, (x + square_size, y - square_size, square_size, square_size))


