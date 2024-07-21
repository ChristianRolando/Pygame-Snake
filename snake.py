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
        self.snake_cord = [[self.x_cord, self.y_cord],
                           [208, self.y_cord],
                           [176, self.y_cord]]
        print(f"Snake initialized at position: {self.snake_cord[0]}")
       
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
        self.snake_cord.insert(0, new_head)
        self.snake_cord.pop()
        print(f"Snake updated to position: {self.snake_cord[0]}")
    
    def snake_draw(self):
        """Draw the snake on the screen."""
        for i in self.snake_cord:
            pygame.draw.rect(self.screen.get_screen(), "purple", [(i), (self.screen.get_screen_pixels(), self.screen.get_screen_pixels())])
        print(f"Snake drawn at positions: {self.snake_cord}")
             
    def snake_directional(self):
        """Update the direction of the snake based on the current direction."""
        if self.current_direction == 'd':
            self.update_seg = [self.snake_cord[-1][0] - 32, self.snake_cord[-1][1]]
        elif self.current_direction == 'a':
            self.update_seg = [self.snake_cord[-1][0] + 32, self.snake_cord[-1][1]]
        elif self.current_direction == 'w':
            self.update_seg = [self.snake_cord[-1][0], self.snake_cord[-1][1] - 32]
        elif self.current_direction == 's':
            self.update_seg = [self.snake_cord[-1][0], self.snake_cord[-1][1] + 32]
        print(f"Snake direction updated to: {self.current_direction}, segment: {self.update_seg}")
        return self.update_seg
            
    def check_snake_collide_with_self(self, score):
        """Check if the snake collides with itself."""
        if score > 5:
            head = pygame.Rect(self.snake_cord[0][0], self.snake_cord[0][1], self.screen.get_screen_pixels(), self.screen.get_screen_pixels())
            for segment in self.snake_cord[2:]:
                segment_rect = pygame.Rect(segment[0], segment[1], self.screen.get_screen_pixels(), self.screen.get_screen_pixels())
                if head.colliderect(segment_rect):
                    print("Snake collided with itself!")
                    return False
            print("Snake did not collide with itself!")
        return True