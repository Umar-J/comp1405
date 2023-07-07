# Umar Jan 101270578
import pygame
#userinput
userpic = input("Enter the file you would like to import\n> ")
#load image
pic = pygame.image.load(userpic)
#get size
x,y = pic.get_size()
#window using the above variables
screen = pygame.display.set_mode((x,y))
#blit image to the screen
screen.blit(pic,(0,0))
pygame.display.update()

# Functions to ensure that there will not be any x,y coordinates that are out of bounds
def xval(a,col,x):
    if a-50+col < x:
        return abs((a-50+col)) 
    else:
        return x-2

def yval(b,row,y):
    if b-50+row < y:
        return abs((b-50+row))
    else:
        return y-2

exit_flag = False
while not exit_flag:
    pygame.event.get()
    if pygame.mouse.get_pressed()[0]:
        for row in range (100): #all possible pixels
            for col in range (100):
                #get mouse position
                a,b = pygame.mouse.get_pos()
                xv = xval(a,col,x)
                yv = yval(b,row,y)
                (r,g,b,_) = pic.get_at((xv,yv))

                #apply negation of each pixel abs(c-255) (set at)
                r=abs(r-255)
                g=abs(g-255)
                b=abs(b-255)
                pygame.Surface.set_at(screen,(xv,yv),(r,g,b))
                pygame.display.update()
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit_flag = True
