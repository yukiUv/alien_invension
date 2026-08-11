import sys

import pygame

from settings import Settings

def run_game():
    #Initialize pygame, settings and  screen object.
    pygame.init()
    ai_settings = Settings()
    
    screen = pygame.display.set_mode(
        (ai_settings.screen_width
    ))
    pygame.display.set_caption("Alien Invasion")
    
    #set the bg color.
    bg_color =(230,230,230)
    
    #Start the main loop for the game. 
    while True:
        
        #watch for keybord and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        # redraw the screen during each pass through the loop.
        screen.fill(bg_color)
                
        # make the most recently drawn screen visible.
        pygame.display.flip()

run_game()