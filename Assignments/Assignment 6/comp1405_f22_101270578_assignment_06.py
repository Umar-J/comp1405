# Umar Jan 101270578
# Features: 1. If player lands on another they are sent to start 2. Numbered tiles
import pygame
import random

dimensions = [1300, 900]
display = pygame.display.set_mode((dimensions[0], dimensions[1])) #initialize suraface 
bColor = [(100,100,100),(255,255,255)] #board color
cellsize = 100 #x,y
bsize = [7,6]
pygame.init() #fonts
bfont = pygame.font.SysFont('Arial', 14)#font for tiles
tfont = pygame.font.SysFont('Arial', 32)#font for tiles
#players initialization: Name, Position, color
p1 = ["Player 1", 0 , (255,0,0)]
p2 = ["Player 2", 0 , (0,255,0)]
tcounter = 0 # turn counter

#set up the game
def board():
    counter = 1 # counter for square number
    for r in range (bsize[0]): # rows
        for c in range (bsize[1]): #columns
            xCell = abs(cellsize*5*((r % 2)) - c*cellsize)
            pygame.draw.rect(display,bColor[(c)%2],(xCell,r*cellsize,cellsize,cellsize))
            
            #number the tiles
            display.blit(bfont.render(str(counter), True, (100,200,0)),(xCell +5 ,r*cellsize+5))
            counter+=1
            pygame.display.update() 
            
            #draw players
            #player 1
            if p1[1] <=5:
                pygame.draw.circle(display,p1[2],((p1[1]*cellsize)+50,(cellsize-25)),100/6)
            if p1[1] >5 and p1[1]<=11:
                pygame.draw.circle(display,p1[2],(5*cellsize + 50 - ((p1[1]-6)*cellsize),(2*cellsize-25)),100/6)
            if p1[1] >11 and p1[1]<=17:
                pygame.draw.circle(display,p1[2],(((p1[1]-12)*cellsize)+50,(3*cellsize-25)),100/6)
            if p1[1] >17 and p1[1]<=23:
                pygame.draw.circle(display,p1[2],(5*cellsize + 50 - ((p1[1]-18)*cellsize),(4*cellsize-25)),100/6)
            if p1[1] >23 and p1[1]<=29:
                pygame.draw.circle(display,p1[2],(((p1[1]-24)*cellsize)+50,(5*cellsize-25)),100/6)
            if p1[1] >29 and p1[1]<=35:
                pygame.draw.circle(display,p1[2],(5*cellsize + 50 - ((p1[1]-30)*cellsize),(6*cellsize-25)),100/6)
            if p1[1] >35 and p1[1]<=40:
                pygame.draw.circle(display,p1[2],(((p1[1]-35)*cellsize)+50,(7*cellsize-25)),100/6)
            
            #player 2
            if p2[1] <=5:
                pygame.draw.circle(display,p2[2],((p2[1]*cellsize)+50,(cellsize-75)),100/6)
            if p2[1] >5 and p2[1]<=11:
                pygame.draw.circle(display,p2[2],(5*cellsize + 50 - ((p2[1]-6)*cellsize),(2*cellsize-75)),100/6)
            if p2[1] >11 and p2[1]<=17:
                pygame.draw.circle(display,p2[2],(((p2[1]-12)*cellsize)+50,(3*cellsize-75)),100/6)
            if p2[1] >17 and p2[1]<=23:
                pygame.draw.circle(display,p2[2],(5*cellsize + 50 - ((p2[1]-18)*cellsize),(4*cellsize-75)),100/6)
            if p2[1] >23 and p2[1]<=29:
                pygame.draw.circle(display,p2[2],(((p2[1]-24)*cellsize)+50,(5*cellsize-75)),100/6)
            if p2[1] >29 and p2[1]<=35:
                pygame.draw.circle(display,p2[2],(5*cellsize + 50 - ((p2[1]-30)*cellsize),(6*cellsize-75)),100/6)
            if p2[1] >35 and p2[1]<=40:
                pygame.draw.circle(display,p2[2],(((p2[1]-35)*cellsize)+50,(7*cellsize-75)),100/6)


#dice
def dice(player):
    roll = random.randint(1,6)
    pygame.draw.rect(display, (0,0,0), (980,199,101,400)) #clr old stuff 
    if player == 1:
        p1[1] += roll
        #checking if same square as other player
        if p1[1] == p2[1]:
            p1[1] =0
    elif player == 2:
        p2[1] += roll
        #checking if same square as other player
        if p2[1] == p1[1]:
            p2[1] =0
    display.blit(tfont.render('Dice Result:', True, (100,200,0)),(1000,300))
    display.blit(tfont.render(str(roll), True, (100,200,0)),(1000,340))
    board()
    pygame.display.update()
    return roll

def plabel(player):
    pygame.draw.rect(display, (0,0,0), (980,49,200,400)) #clr old stuff
    display.blit(tfont.render('Current Turn:', True, (100,200,0,)),(1000,50))
    if player == 1:
        display.blit(tfont.render(p1[0], True, (100,200,0)),(1000,100))
    elif player == 2:
        display.blit(tfont.render(p2[0], True, (100,200,0)),(1000,100))
    pygame.display.update() 

#turn selection
def turn(count):
    if count % 2 == 0:
        return 1
    else:
        return 2


def main():
    board()
    z = 0
    while True:
        z += 1
        pygame.time.delay(1000)
        plabel(turn(z))
        dice(turn(z))
        if p1[1] > 40:
            print("player 1 wins")
            display.blit(tfont.render('Player 1 wins!', True, (100,200,0)),(800, 600))
            pygame.display.update()
            break
        elif p2[1] > 40:
            print("player 2 wins!")
            display.blit(tfont.render('Player 2 wins!', True, (100,200,0)),(800, 600))
            pygame.display.update()
            break

main()


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.display.quit()
pygame.quit()
exit()