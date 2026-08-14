import pygame as pyg

class Ship():
    
    def __init__(self,screen):
        """initialize the ship and set its starting positions"""
        
        self.screen = screen
        
        # load the ship image and get its rect.
        self.image =pyg.image.load('image/ship.bmp')
        self.image = pyg.transform.scale(self.image, (60,40))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        # start each new ship at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
        
    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image,self.rect)
        
        