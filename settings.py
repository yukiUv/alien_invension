class Settings():
    """a class to store all settings  for game"""
    
    def __init__(self):
        """Initialize the game's settings"""
        # screen settings
        self.screen_width =1200
        self.screen_height =720
        self.bg_color =(230,230,230)
        
        #ship settings
        self.ship_speed_factor = 2.5
        self.ship_limit = 3
        
        # bullet settings
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60,60,60
        self.bullets_allowed = 4
        #Alien Settings
        self.alien_speed_factor = 3
        self.drop_fleet_speed = 10
        # fleet_direction of  1 represent right; -1 represent left .
        self.fleet_direction = 1