# Umar Jan 101270578

import pygame

pi = 3.141592653589793238

screen = pygame.display.set_mode((300, 300))

pygame.draw.rect(screen, (177, 62, 41), [0, 0, 300, 300])
# outermost right
pygame.draw.arc(screen, (85, 134, 177), [70, 70, 163, 163], 3*pi/2, pi/2, width = 100 )
#middle right
pygame.draw.arc(screen, (224, 180, 85), [95, 95, 112, 112], 3*pi/2, pi/2, width = 100)
# innermost right
pygame.draw.arc(screen, (220, 153, 136), [121, 121, 60, 60], 3*pi/2, pi/2, width = 100)
#outer left
pygame.draw.arc(screen, (215, 205, 195), [70, 70, 163, 163], pi/2, 3*pi/2, width = 100 )
#inner left
pygame.draw.arc(screen, (29, 29, 29), [95, 95, 112, 112], pi/2, 3*pi/2, width = 100)

pygame.display.update()
pygame.time.delay(3000)
