import sys
import pygame
from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf
from pygame.sprite import Group

def run_game():
    #Initialize pygame, settings and  screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    #set the bg color.
    
    # make s ship, group of bullets , and a group of aliens.
    ship = Ship(ai_settings,screen)
    bullets = Group()
    aliens = Group()
    
    # create the fleet of an aliens.
    gf.create_fleet(ai_settings,screen,aliens)
    
    
    
    
    #Start the main loop for the game. 
    while True:
        gf.check_events(ai_settings,screen,ship,bullets)
        ship.update()
        
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings,screen,ship,aliens,bullets)
        
        #watch for keybord and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        # redraw the screen during each pass through the loop.
        screen.fill(ai_settings.bg_color)
        ship.blitme()
                
        # make the most recently drawn screen visible.
        pygame.display.flip()
        bullets.update()
        gf.update_screen(ai_settings,screen,ship,aliens,bullets)

run_game()