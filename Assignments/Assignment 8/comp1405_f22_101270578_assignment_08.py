# Umar Jan 101270578

import pygame

def draw_eyes():
    #draw eyes with centre at 150,250, black and white and outline black
    # Colours
    white = (255, 255, 255)
    black = (0, 0, 0)
    brown = (139,69,19)
        
    #right eye
    pygame.draw.circle(win_sfc, white, (150+30, 250-30), 30)
    pygame.draw.circle(win_sfc, black, (150+30, 250-30), 30, 5)
    
    #left eye
    pygame.draw.circle(win_sfc, white, (150-30, 250-30), 30)
    pygame.draw.circle(win_sfc, black, (150-30, 250-30), 30, 5)

    # iris
    pygame.draw.circle(win_sfc, brown, (150+30, 250-30), 10)
    pygame.draw.circle(win_sfc, brown, (150-30, 250-30), 10)

def draw_hat():
    #draw hat at centre 250,350, 3 colors 
    #colors
    black = (0, 0, 0)
    green = (0, 200, 0)
    red = (255, 0, 0)
    #code for drawing parts of hat
    pygame.draw.arc(win_sfc, red, (140, 240, 190, 150), 0, 3.141592, 200)#top part
    pygame.draw.arc(win_sfc, black, (140, 240, 190, 150), 0, 3.141592, 5) #outline
    pygame.draw.rect(win_sfc, green, (140, 280, 190, 40))#main bottom part
    pygame.draw.rect(win_sfc, black, (140, 280, 190, 40), 5)#outline
    return "christmas toque"
    
def draw_mouth(x,y):
    #inner mouth (two circles, one for inner throat)
    pygame.draw.circle(win_sfc, (150, 40, 10), (x, y+40), 20) #offset based on arguments
    pygame.draw.circle(win_sfc, (60, 20, 20), (x, y+45), 10)
    #outline
    pygame.draw.circle(win_sfc, (0, 0, 0), (x, y+40), 20, 5)   