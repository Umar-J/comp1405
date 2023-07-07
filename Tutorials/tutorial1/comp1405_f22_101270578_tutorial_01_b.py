# Umar Jan 101270578

import pygame

screen = pygame.display.set_mode((300, 300))
screen.fill((255, 255, 255))

# body
pygame.draw.polygon(screen, (0, 0, 0), [(115, 164), (173-12, 65+20), (241-16, 80+25), (182, 180)])
#pygame.draw.polygon(screen, (0, 0, 0), [(115, 164), (173, 65+20), (241, 80), (182, 180)])
# head
pygame.draw.circle(screen, (0, 0, 0), (220, 39), 25)
# left leg
pygame.draw.arc(screen, (0, 0, 0), (65, 150, 120, 80), 3.14 / 2, 3.14, width=5)
# right leg
pygame.draw.arc(screen, (0, 0, 0), (154, 163, 60, 80), -1, 3.14/2, width=5)
# right arm
pygame.draw.arc(screen, (0, 0, 0), (177, 84, 60, 80), -1, 3.14/2, width=5)
# left arm
pygame.draw.arc(screen, (0, 0, 0), (120, 20, 100, 80), 3.14, 3*3.14/2, width=5)
#left foot
pygame.draw.polygon(screen, (0, 0, 0), [(38,188), (67,188), (67,190), (38,190)])
#right foot
pygame.draw.polygon(screen, (0, 0, 0), [(200, 233), (217, 249), (215, 251), (198, 235)])
#donut
pygame.draw.circle(screen, (185,122,87), (105,47), 17)
# donut hole
pygame.draw.circle(screen, (255,255,255), (105,47), 5)
#left hand
pygame.draw.circle(screen, (0, 0, 0), (123, 60), 10)
# right hand
pygame.draw.circle(screen, (0, 0, 0), (223, 154), 10)
#eye
pygame.draw.circle(screen, (255,255,255), (212, 29), 4)
#smile
pygame.draw.arc(screen, (255,255,255), (192, 6, 50, 40), 3.14, 3*3.14/2, width=2)
#neck curve
pygame.draw.arc(screen, (0,0,0), (160, 65, 68, 60), -0.5, 3, width=100)


pygame.display.update()
pygame.time.delay(3000)
