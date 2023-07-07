# Umar Jan 101278520
from sys import argv
import pygame
import random

#get image
#userImage = argv[1]
userImage = "c:/Users/umara/pythonprojects/Assignments/assignment 5/abu_antar.jpg" #just a string that has name
image = pygame.image.load(userImage) #actually imports the image from the string
#get dimensions of image
(wid,hei) = image.get_size()
screen = pygame.display.set_mode((wid*5, hei*5)) #expand by factor of 5 (each pixel will now be 5x5 big)

for y in range (hei):
    for x in range (wid):
        (r, g, b, _) = image.get_at((x, y))
        #number of points to draw total
        red, green, blue = r // 8, g // 8, b // 8
        #iterate for each color and corresponding # of shapes for each
        while red > 0:
            red -=1
            xEnlarged = x*5 + random.randint(0,5-1) # x*5 is the bottom and adds random number 0-5 to it
            yEnlarged = y*5 + random.randint(0,5-1) # ex if x is 10 then its 10*5 + 0-5 so range is 500-505
            pygame.draw.rect(screen, ((255, 0, 0)), (xEnlarged, yEnlarged,1,1))
        while green > 0:
            xEnlarged = x*5 + random.randint(0,5-1) 
            yEnlarged = y*5 + random.randint(0,5-1) 
            pygame.draw.rect(screen, ((0, 255, 0)), (xEnlarged, yEnlarged,1,1))
            green -=1
        while blue > 0:
            blue -= 1
            xEnlarged = x*5 + random.randint(0,5-1) 
            yEnlarged = y*5 + random.randint(0,5-1) 
            pygame.draw.rect(screen, ((0, 0, 255)), (xEnlarged, yEnlarged,1,1))
    pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
