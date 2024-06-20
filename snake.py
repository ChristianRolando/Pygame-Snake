import pygame
from screen import Screen
from singleton import Singleton

class Snake(metaclass = Singleton):
    """A class representing a snake in a game."""

    def __init__(self, screen: Screen):
        """Initialize the snake with its attributes."""
        self.screen = screen
        self.player_vel_x = 0
        self.player_vel_y = 0
        self.current_direction = "d"
        self.movement_speed = 280
        self.x_cord = 240
        self.y_cord = 240
        self.snake_body = [[self.x_cord, self.y_cord],
                           [208, self.y_cord],
                           [176, self.y_cord]]
        print(f"Snake initialized at position: {self.snake_body[0]}")
  
    def get_x_cord(self):
        return self.x_cord
    
    def set_x_cord(self, x):
        self.x_cord = x
    
    def get_y_cord(self):
        return self.y_cord
    
    def set_y_cord(self, y):
        self.y_cord = y
        
    def snake_update(self):
        """Update the position of the snake."""
        new_head = [self.x_cord, self.y_cord]
        self.snake_body.insert(0, new_head)
        self.snake_body.pop()
        print(f"Snake updated to position: {self.snake_body[0]}")
    
    def snake_draw(self):
        """Draw the snake on the screen."""
        for i in self.snake_body:
            pygame.draw.rect(self.screen.get_screen(), "purple", [(i), (self.screen.get_screen_pixels(), self.screen.get_screen_pixels())])
        print(f"Snake drawn at positions: {self.snake_body}")
             
    def snake_directional(self):
        """Update the direction of the snake based on the current direction."""
        if self.current_direction == 'd':
            self.update_seg = [self.snake_body[-1][0] - 32, self.snake_body[-1][1]]
        elif self.current_direction == 'a':
            self.update_seg = [self.snake_body[-1][0] + 32, self.snake_body[-1][1]]
        elif self.current_direction == 'w':
            self.update_seg = [self.snake_body[-1][0], self.snake_body[-1][1] - 32]
        elif self.current_direction == 's':
            self.update_seg = [self.snake_body[-1][0], self.snake_body[-1][1] + 32]
        print(f"Snake direction updated to: {self.current_direction}, segment: {self.update_seg}")
        return self.update_seg