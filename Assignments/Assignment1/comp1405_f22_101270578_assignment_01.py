# Umar Jan 101270578

import pygame

screen = pygame.display.set_mode((480, 640))

# this will fill the window with a background color of white
screen.fill((255, 255, 255))

# polygons
pygame.draw.polygon(screen, (93, 70, 50), [(0, 320), (0, 543), (79, 640), (159, 640), (159, 532)])
pygame.draw.polygon(screen, (131, 117, 175), [(160, 533), (320, 533), (320, 426), (400, 426), (400, 534), (321, 640), (160, 640)])

# Update display
pygame.display.update()

# pause to see picture
pygame.time.delay(3000)

# saving image
pygame.image.save(screen, "assigned_image_for_101270578.png")
