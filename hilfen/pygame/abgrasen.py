import sys, math, pygame,random


def getPos(w):
    return (w*10)+4

clock = pygame.time.Clock()
pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
# Set up the drawing window
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

# Run until the user asks to quit
running = True
f0,f1,f2,size = 0,0,0,75
posList=[]
anzahlFelder=0
for y in range(1,79):
    xLine=[]
    for x in range(1,79):
        if random.randint(0,9) == 1:
            xLine.append([(y*10)+4,(x*10)+4,9])
        else:
            xLine.append([(y*10)+4,(x*10)+4,1])
            anzahlFelder+=1
    posList.append(xLine[:])
print(anzahlFelder,file=sys.stderr)


botList=[[1,1]]        
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))
    for xLine in posList:
        for p in xLine:
            if p[2] == 1:
                pygame.draw.circle(screen, (255,10,10), (p[0], p[1]), 3)
            elif p[2] == 0:
                pygame.draw.circle(screen, (50,205,50), (p[0], p[1]), 3)
            else:
                pygame.draw.rect(screen,(0,0,0),pygame.Rect(p[0]-4, p[1]-4, 10, 10))
    for bot in botList:
        pygame.draw.circle(screen, (0,255,0), (getPos(bot[0]), getPos(bot[1])), 4)
        pos = posList[bot[0]-1][bot[1]-1]
        posList[bot[0]-1][bot[1]-1] = [pos[0],pos[1],0]
        bot[0] +=1;bot[1] = bot[1]
    # Flip the display
    pygame.display.flip()
    clock.tick(60)   # xx fps (frames per second)
# Done! Time to quit.
pygame.quit()