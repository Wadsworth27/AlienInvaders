import pygame
import sys 
from settings import Settings 
from ship import Ship

def run_game():
    pygame.init()
    ai_settings=Settings()
    screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #make a ship
    ship=Ship(screen)

#main game loop
    
    while True: 
        #Watch for keyboard and mouse events
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
        #redraw the screen on each passthrough
        screen.fill(ai_settings.bg_color)
        ship.blitme()
        #most recent scren visible
        pygame.display.flip()
run_game()
<<<<<<< HEAD

=======
>>>>>>> parent of 8dd99e5 (Revert "Added ship image and starting position")
