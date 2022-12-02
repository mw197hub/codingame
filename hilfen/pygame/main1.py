import sys, math, pygame



clock = pygame.time.Clock()
pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
# Set up the drawing window
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

# Run until the user asks to quit
running = True
f0,f1,f2,size = 0,0,0,75
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            # Was it the Escape key? If so, stop the loop.
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_SPACE:
                print("Spieler hat Leertaste gedrückt")
            elif event.key == pygame.K_a:
                f0+=10
            elif event.key == pygame.K_s:
                f1+=10
            elif event.key == pygame.K_d:
                f2+=10
        elif event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print(pygame.mouse.get_pressed())
            print(pygame.mouse.get_pos())
            print(pygame.time.get_ticks())
            print(pygame.mouse.get_rel())
            #pygame.mouse.set_visible(False)
            pygame.mouse.set_pos([1,1])
        print(pygame.mouse.get_pos())

    # Fill the background with white
    screen.fill((255, 255, 255))

    # Draw a solid blue circle in the center
    pygame.draw.circle(screen, (f0, f1, f2), (250, 250), size)
    if size > 0:
        size-=1
    else:
        size=75
    # Flip the display
    pygame.display.flip()
    clock.tick(60)   # xx fps (frames per second)
# Done! Time to quit.
pygame.quit()
