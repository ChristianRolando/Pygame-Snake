import pygame
import math
import random

class Snake:
    def __init__(self, name):
        self.player_vel_x = 0
        self.player_vel_y = 0
        self.current_direction = "d"
        self.movement_speed = 250
        self.player_pos_x = 240
        self.player_pos_y = 240
        self.snake_body = [[self.player_pos_x, self.player_pos_y],
                           [208, self.player_pos_y],
                           [176, self.player_pos_y]]
        self.name=name
        
    def snake_update(self):
        new_head = [self.player_pos_x, self.player_pos_y]
        self.snake_body.insert(0, new_head)
        self.snake_body.pop()
    
    def snake_draw(self, PIXELS, screen):
        for i in self.snake_body:
            pygame.draw.rect(screen, "purple", [(i), (PIXELS, PIXELS)])
             
    def snake_directional(self):
        if self.current_direction == 'd':
            self.update_seg = [self.snake_body[-1][0] - 32, self.snake_body[-1][1]]
        if self.current_direction == 'a':
            self.update_seg = [self.snake_body[-1][0] + 32, self.snake_body[-1][1]]
        if self.current_direction == 'w':
            self.update_seg = [self.snake_body[-1][0], self.snake_body[-1][1] - 32]
        if self.current_direction == 's':
            self.update_seg = [self.snake_body[-1][0], self.snake_body[-1][1] + 32]
        return self.update_seg