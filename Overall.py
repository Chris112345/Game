import pygame, sys
from pygame.locals import *
from Character_Class import *
from Environment_Class import *
pygame.init()

Game_Display = (500,500)
Display_Surf = pygame.display.set_mode(Game_Display)

Display_Surf.fill((255,255,255))
speed = 4
Character = Character("cthulu.png",100,100,speed)

Environment = Environment("back1.png",1000,1000,(0,0))

cooldown_const = 25
cooldown = 0
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    keys = pygame.key.get_pressed()
    if cooldown <= 0:
        if keys[pygame.K_RIGHT] and Character.get_coord()[0] < (500-Character.get_width()):
            if -499 < Environment.get_coord()[0] <= 499:
                Environment.right_coord(speed)
            else:
                Character.right()
            cooldown += cooldown_const
        if keys[pygame.K_LEFT] and Character.get_coord()[0] > 0:
            if -499 < Environment.get_coord()[0] <= 499:
                Environment.left_coord(speed)
            else:
                Character.left()
            cooldown += cooldown_const
        if keys[pygame.K_DOWN] and Character.get_coord()[1] < (500-Character.get_length()):
            if -499 < Environment.get_coord()[1] <= 499:
                Environment.down_coord(speed)
            else:
                Character.down()
            cooldown += cooldown_const
        if keys[pygame.K_UP] and Character.get_coord()[1] > 0:
            if -499 < Environment.get_coord()[1] <= 499:
                Environment.up_coord(speed)
            else:
                Character.up()
            cooldown += cooldown_const
    if cooldown > 0:
        cooldown -= 1
    Display_Surf.fill((255,255,255))
    Display_Surf.blit(Environment.get_background(), Environment.get_coord())
    Display_Surf.blit(Character.image,Character.get_coord())
    pygame.display.update()
    
