import pygame 
from singleton import Singleton
from screen import Screen


class ScoreBoard(metaclass = Singleton):
    
    def __init__(self):
        self.score = 0
        self.x_cord = 240
        self.y_cord = 0
        self.screen = Screen()
        self.draw_scoreboard(self.screen.get_screen())
        
    
    
    def draw_scoreboard(self, screen):
        font = pygame.font.Font("freesansbold.ttf", 32)
        score = font.render("Score: " + str(self.score), True, (255, 255, 255))
        screen.blit(score, (self.x_cord, self.y_cord))
        
        
        
        
    