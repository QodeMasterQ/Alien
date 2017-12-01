import pygame
from pygame.sprite import Group 
from settings import Settings
from game_stats import GameStats
from ship import Ship 
from alien import Alien
import game_functions as gf
from button import Button
from scoreboard import Scoreboard

def run_game():
    # Intialize pygame,settings and create a screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    screen = pygame.display.set_mode((1100, 700))
    pygame.display.set_caption("Alien Invasion")

    # Make the Play button.
    play_button = Button(ai_settings, screen, "Play")

    # Create an instance to store game statistics and create a scoreboard.
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    
    # Make a ship, a group of bullets, and a group of aliens.
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    #Create the fleet of aliens.
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Set background color.
    bg_color = (230, 230, 230)

    # Make an alien.
    alien = Alien(ai_settings, screen)

    # Make the Play button.
    play_button = Button(ai_settings, screen, "Play")

    # Start the main loop for the game.
    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship,
            aliens, bullets)

        if stats.game_active:
       
            ship.update()
            gf.update_bullets(ai_settings, stats, sb, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, sb, screen, ship, aliens, bullets)
        
        # Get rid of bullets that have disappeared.
               # Create a new bullet and add it to the bullets group.

        gf.update_screen(ai_settings, screen, ship, stats, sb, aliens, bullets,
            play_button)
        
        # Watch for the keyboard and the mouse events.

        # Redraw the screen during each pass through the loop.
        #screen.fill(ai_settings.bg_color) 
        #ship.blitme()

        # Make the most recently drawn screen visible.
        pygame.display.flip()
run_game()