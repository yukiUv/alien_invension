import sys
import pygame
from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button    
from scoreboard import Scoreboard



def run_game():
    #Initialize pygame, settings and  screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    # load the bg image.
    
    ai_settings.bg_image = pygame.image.load('image/background.bmp')
    ai_settings.bg_image = pygame.transform.scale(
        ai_settings.bg_image , (ai_settings.screen_width, ai_settings.screen_height)
    )
    
    """ Set up the sound system the same way : load everything once here
    and store it on ai_settings so fire_bullet() and the collision
    code can just call .play() on it.
    """
    
    ai_settings.fire_sound = pygame.mixer.Sound('sound/fire.wav')
    ai_settings.fire_sound.set_volume(0.4)
    ai_settings.explosion_sound = pygame.mixer.Sound('sound/explosion.wav')
    ai_settings.explosion_sound.set_volume(0.5)
    
    pygame.mixer.music.load('sound/background_music.wav')
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(-1) # -1 loops the track forever1
    
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
    sb =Scoreboard(ai_settings,screen,stats)
    
    #Start the main loop for the game. 
    while True:
        gf.check_events(ai_settings, screen,stats,sb,play_button, ship,aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets)
            gf.update_aliens(ai_settings,screen,stats,sb,ship,aliens,bullets)
            # Draw everything ONCE per frame — update_screen handles
            # screen.fill, bullets, ship.blitme(), aliens.draw(), and flip().
        gf.update_screen(ai_settings,screen,stats,sb, ship, aliens, bullets,play_button)
        
        
        clock.tick(90)
        

run_game()