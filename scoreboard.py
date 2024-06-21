import pygame 
from singleton import Singleton
from screen import Screen
import pandas as pd


class ScoreBoard(metaclass = Singleton):
    
    def __init__(self):
        self.score = 0
        self.x_cord = 0
        self.y_cord = 0
        self.screen = Screen()
        self.draw_scoreboard(self.screen.get_screen())
        # self.highscore = pd.to_numeric(pd.read_csv("highscores.csv")["highscore"], errors='coerce').max()
        
        print()
    def draw_scoreboard(self, screen):
        font = pygame.font.Font("freesansbold.ttf", 32)
        score = font.render("Score: " + str(self.score), True, (255, 255, 255))
        highscore = font.render("High Score: " + str(self.get_highscore()), True, (255, 255, 255))

        # Get the screen dimensions
        screen_width, screen_height = pygame.display.get_surface().get_size()
        top_bar_height = 40  # Set the height of the top bar

        # Create a rectangle that covers the top bar of the screen
        score_rect = pygame.Rect(self.x_cord, self.y_cord, screen_width, top_bar_height)

        # Draw the rectangle
        pygame.draw.rect(screen, (0, 0, 0), score_rect)

        # Position the score in the middle of the top bar
        score_x = (screen_width - score.get_width()) // 4
        score_y = (top_bar_height - score.get_height()) // 2
        screen.blit(score, (score_x, score_y))

        # Position the high score to the right of the score
        highscore_x = score_x + score.get_width() + 10
        highscore_y = score_y
        screen.blit(highscore, (highscore_x, highscore_y))
        
    def update_highscore(self):
        score_data = pd.read_csv("highscores.csv")
        highscore = self.get_highscore()
        
        if self.score > highscore:
            score_data["highscore"] = self.score
            score_data.to_csv("highscores.csv", index = False)
            print("new highscore")
            

        
    def get_highscore(self):
        score_data = pd.read_csv("highscores.csv")
        score_data["highscore"] = int(pd.to_numeric(score_data["highscore"], errors='coerce'))
        
        highscore = score_data["highscore"].max()
        return highscore    
        
        
    def get_score(self):
        return self.score
    