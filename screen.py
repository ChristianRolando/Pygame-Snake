from typing import Any
import pygame
from singleton import Singleton

class Screen(metaclass = Singleton):
    def __init__(self):
        self.screen_width = 640
        self.screen_height = 640
        self.screen_pixels = 32
        self.squares = int(self.screen_width / self.screen_pixels)
        self.BG1_rgb = (173, 216, 230)  # Light Blue
        self.BG2_rgb = (0, 0, 139) 
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height)) 
        self.BG1 = self.hex_to_rgb("#F8C00")
        self.BG2 = self.hex_to_rgb("#FFD700")
    
    def hex_to_rgb(self, hex_color):
        return tuple(int(hex_color[i+1:i+3], 16) for i in (0, 2, 4))
    
    def get_screen_width(self):
        return self.screen_width 
    
    def get_screen_height(self):
        return self.screen_height
    
    def get_screen(self):
        return self.screen 
    
    def get_screen_pixels(self):
        return self.screen_pixels
    
    def get_squares(self):
        return self.squares
    
    def get_BG1(self):
        return self.BG1
    
    def get_BG2(self):
        return self.BG2
    
    def update(self, food):
        pygame.display.update(food)
        
    def filp():
        pygame.display.flip()