import pygame 

class Ship():
    
    def __init__(self,ai_settings,screen):
        """initialize the ship and set its starting positions"""
        
        self.screen = screen
        self.ai_settings = ai_settings
        
        # load the ship image and get its rect.
        self.image =pygame.image.load('image/ship.bmp')
        self.image = pygame.transform.scale(self.image, (60,40))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        # start each new ship at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
        # store a decimal value for the ship's center.
        self.center = float(self.rect.centerx)
        
        # movement flag
        self.moving_right = False
        self.moving_left = False
        
    def update(self):
        """ update the ship's postion based on the movement flag."""
        
        keys = pygame.key.get_pressed()
        # update the ship's cenetr value, not the rect.
        if keys [pygame.K_RIGHT] and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
            
        # update rect object from self.center.
        self.rect.centerx = self.center   
        
    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image,self.rect)
        
        