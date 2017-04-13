##Environment Construction and Dimensions File

import pygame,sys
from pygame.locals import *

def wall_up(lenght, width):
    item = pygame.Surface(length,width),flags = SRCALPHA, depth = 32)
    item.fill((0,0,0))
    
    return item

def column(length,width):
    item = wall_up(length,width)

    return item

def wall_jut(length,width):
    item = wall_up

    return item

def wall_down(length,width):
    item = pygame.Surface(length,width),flags = SRCALPHA, depth = 32)
    item.fill((0,0,0))

    return item

def wall_left(length,width):
    item = pygame.Surface(length,width),flags = SRCALPHA, depth = 32)
    item.fill((0,0,0))

    return item

def wall_right(length,width):
    item = pygame.Surface(length,width),flags = SRCALPHA, depth = 32)
    item.fill((0,0,0))

    return item
