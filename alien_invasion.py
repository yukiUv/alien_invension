import sys
import pygame
from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button

def run_game():
    #Initialize pygame, settings and  screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    #make the play button
    play_button = Button(ai_settings,screen,"Play")
    #create clock object
    clock =pygame.time.Clock()
    
    
    # make s ship, group of bullets , and a group of aliens.
    ship = Ship(ai_settings,screen)
    bullets = Group()
    aliens = Group()
    
    # Create the fleet of aliens ONCE, before the loop starts.
    gf.create_fleet(ai_settings,screen,ship,aliens)
    
    #Create a instance to store game statistics.
    stats = GameStats(ai_settings)
    
    #Start the main loop for the game. 
    while True:
        gf.check_events(ai_settings, screen,stats,play_button, ship, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings,screen,ship,aliens,bullets)
            gf.update_aliens(ai_settings,stats,screen,ship,aliens,bullets)
            # Draw everything ONCE per frame — update_screen handles
            # screen.fill, bullets, ship.blitme(), aliens.draw(), and flip().
        gf.update_screen(ai_settings,screen,stats, ship, aliens, bullets,play_button)
        
        
        clock.tick(90)
        

run_game()