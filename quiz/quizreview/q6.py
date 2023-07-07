import pygame
pygame.display.set_mode([750, 750])

# row i, column j,

# row
for x in range (3, 10, 3):
    # column
    for y in range (3, 13, 3):
        print("umbrella at", x,y)
      #  umbrella(x, y, 0, 255, 0)

# row
for w in range (4, 13, 4):
    #column
    for z in range (1, 10, 4):
        print("star at", w,z)
        #star(w, z, 0, 0, 255)

pygame.display.update()
pygame.time.delay(5000)
