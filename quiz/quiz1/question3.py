import pygame

pygame.display.set_mode((750,750))

# rows i, columns j

# draw circle
for i in range (4, 11, 2):
    for j in range (2, 11, 4):
    #    circle(i, j, 255, 0, 0)

# draw star
for i in range (1, 10, 2):
    for j in range (2, 12, 3):
   #    star(i, j, 0, 0, 255)


pygame.display.update()
pygame.time.delay(5000)