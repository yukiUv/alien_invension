class GameStats():
    """Track statistics for alien incasion"""
    
    def __init__(self,ai_settings):
        """Initialize statistics."""
        self.ai_settings = ai_settings
        self.reset_stats()
        # start game in an inactive state
        self.game_active = False
        
        # load saved high score
        
        try:
            with open("high_score.txt","r") as file:
                self.high_score = int(file.read())
        except (FileNotFoundError,ValueError):
            self.high_score = 0
            
        self.reset_stats()
        
    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        # start level
        self.level = 1
    
    def save_high_score(self):
        """save the high score"""
        
        with open("high_score.txt","w") as file:
            file.write(str(self.high_score))
        
    