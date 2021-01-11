import sys
import pygame
def check_keydown_events(event,ship):
    #Response to key presses
    if event.key == pygame.K_RIGHT:
        ship.moving_right=True
    elif event.key == pygame.K_LEFT:
        ship.moving_left=True

def check_keyup_events(event,ship):
    #handles key releases
    if event.key == pygame.K_RIGHT:
        ship.moving_right=False      
    elif event.key == pygame.K_LEFT:
        ship.moving_left=False  


def check_events(ship):
    # Respond to events like keypresses or mouseclicks
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        elif event.type== pygame.KEYDOWN:
            check_keydown_events(event,ship)
        elif event.type== pygame.KEYUP:
            check_keyup_events(event,ship)


def update_screen(ai_settings, screen, ship):
        screen.fill(ai_settings.bg_color)
        ship.blitme()
        
        #most recent scren visible
        pygame.display.flip()
