import pygame

from settings import Settings 
from ship import Ship
import game_functions as gf

def run_game():
    pygame.init()
    ai_settings=Settings()
    screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #make a ship
    ship=Ship(ai_settings,screen)

#main game loop
    
    while True: 
        #Watch for keyboard and mouse events
        gf.check_events(ship)
        #redraw the screen on each passthrough
        ship.update()
        gf.update_screen(ai_settings, screen, ship)

run_game()

#store bullets
