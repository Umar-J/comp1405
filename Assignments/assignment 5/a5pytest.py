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

def points (r,g,b):
    rlist = [r // 8, g // 8, b // 8]
    colorlist = [(255,0,0),(0, 255, 0),(0, 0, 255)]
    for i in (0,1,2):
        while rlist[i]>=0:
            rlist[i] -= 1
            if i == 0: dcolor = colorlist[0]
            elif i == 1:dcolor = colorlist[1]
            elif i ==2 :dcolor = colorlist[2]
            xEnlarged = x*5 + random.randint(0,5-1) 
            yEnlarged = y*5 + random.randint(0,5-1) 
            pygame.draw.rect(screen, (dcolor), (xEnlarged, yEnlarged,1,1))
            pygame.display.update()

for y in range (hei):
    for x in range (wid):
        (r,g,b,_) = image.get_at((x, y))
        points(r,g,b)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
