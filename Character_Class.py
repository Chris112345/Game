import pygame, sys
from pygame.locals import *

pygame.init()

##Character Class
class Character():
    
    def __init__(self,image,length,width,speed):
        self.xcoord = 0
        self.ycoord = 0
        self.length = length
        self.orientation = 'right'
        self.speed = speed
        self.width = width
        picture = pygame.Surface((length,width),flags=SRCALPHA, depth=32)
        picture = pygame.image.load(image).convert_alpha()
        picture = pygame.transform.scale(picture,(width,length))
        self.image = picture
        
    

    def get_length(self):
        return self.length

    def get_width(self):
        return self.width
        
    def up(self):
        self.ycoord -= self.speed
        
    def down(self):
        self.ycoord += self.speed
        
    def change(self,new_im):
        self.image = new_im

    def turn(self):
        self.image = pygame.transform.flip(self.image,True,False)

    def left(self):
        self.xcoord -= self.speed
        if self.orientation == 'right':
            self.turn()
            self.orientation = 'left'

         
    def right(self):
        self.xcoord += self.speed
        if self.orientation == 'left':
            self.turn()
            self.orientation = 'right'
        
    def get_coord(self):
        return (self.xcoord,self.ycoord)
        
