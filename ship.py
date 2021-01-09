import pygame

class Ship():

    def __init__(self, ai_settings, screen):
        #initilize the ship and set starting condition
        self.screen=screen
        self.ai_settings=ai_settings
        #load the image and get its rect
        self.image= pygame.image.load('images/ship.bmp')
        self.rect =self.image.get_rect()
        self.screen_rect=screen.get_rect()

        #start each new ship at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # sore a deimal for ship's center
        self.center=float(self.rect.centerx)
        #Movement Flag
        self.moving_right = False
        self.moving_left = False


    def blitme(self):
        '''draw the ship at its current location'''
        self.screen.blit(self.image, self.rect)
    def update(self):
        if self.moving_right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left:
            self.center -= self.ai_settings.ship_speed_factor
        #update rect object form self.center
        self.rect.centerx = self.center
        
    