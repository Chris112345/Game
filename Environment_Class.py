##Environment Class
import pygame, sys
from pygame.locals import *
pygame.init()

class Environment():

    def __init__(self,image,width,length,coord):
        picture = pygame.Surface((length,width),flags=SRCALPHA, depth=32)
        picture = pygame.image.load(image).convert_alpha()
        picture = pygame.transform.scale(picture,(width,length))
        self.image = picture
        self.width = width
        self.length = length
        self.coord = [0,0]

    def get_coord(self):
        return self.coord

    def left_coord(self,speed):
        self.coord[0] += speed

    def right_coord(self,speed):
        self.coord[0] -= speed

    def up_coord(self,speed):
        self.coord[1] += speed

    def down_coord(self,speed):
        self.coord[1] -= speed

    def get_background(self):
        return self.image

    def get_width(self):
        return self.width

    def get_length(self):
        return self.length
