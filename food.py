import pygame
import random
from singleton import Singleton
from screen import Screen

class Food(metaclass = Singleton):
    
    def __init__(self):
        #Cordinates
        self.screen = Screen()
        self.x_cord = int(random.randrange(0,  630, 32))
        self.y_cord = int(random.randrange(0, 630, 32))
        
        #shape of food
        self._shape = pygame.draw.rect(self.screen.get_screen(), "red", [(self.x_cord, self.y_cord), (32, 32)])

    # Getter for x_cord
    
    def get_x_cord(self):
        return self.x_cord

    # Setter for x_cord
    def set_x_cord(self, x):
        self.x_cord = x

    def get_y_cord(self):
        return self.y_cord

    # Setter for y_cord
    def set_y_cord(self, y):
        self.y_cord = y

    # Getter for shape
    @property
    def shape(self):
        return self._shape

    # Setter for shape
    @shape.setter
    def shape(self, value):
        self._shape = value

 