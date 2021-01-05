import pygame
import sys 

def run_game():
    pygame.init()
    screen=pygame.display.set_mode((1200,800))
    pygame.display.set_caption("Alien Invasion")

    # Set background color
    bg_color=(230,230,230)

#main game loop
    while True: 
        #Watch for keyboard and mouse events
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
        #redraw the screen on each passthrough
        screen.fill(bg_color)
        #most recent scren visible
        pygame.display.flip()
run_game()