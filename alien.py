import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """ a class to represent a single alien in the fleet"""
    
    def __init__(self,ai_settings,screen):
        """ Intialize the alien ship and set its starting positions"""
        super().__init__()
        self.screen =screen
        self.ai_settings = ai_settings
        
        # Load the alien ship image and set its rect attributes.
        
        self.image = pygame.image.load('image/alien.bmp')
        self.image = pygame.transform.scale(self.image(60,40))
        self.rect = self.image.get_rect()
        
        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        #store the alien's exact position.
        self.x =float(self.rect.x)
        
    def blitme(self):
        """Draw the alien at its current loaction.""" 
        self.screen.blit(self.image,self.rect)   