import math
import pygame
import random

from food import Food
from snake import Snake
from screen import Screen
from scoreboard import ScoreBoard
from singleton import Singleton

class Controller(metaclass = Singleton):
    
    def __init__(self):
        print("Initializing Controller")
        self.dt = 0
        pygame.init()
        self.food = Food()
        self.screen = Screen()
        self.run_status = True
        self.snake = Snake(self.screen)
        self.clock = pygame.time.Clock()
        self.scoreboard = ScoreBoard()
        self.ate = False
        print(f"dt: {self.dt}, run_status: {self.run_status}, clock: {self.clock}")
    
    def set_run_status(self, status):
        print(f"Setting run status to {status}")
        self.run_status = status
        
    def get_run_status(self):
        return self.run_status
    
    def get_dt(self):
        print("Getting dt")
        return self.dt
    
    def set_name(self, name):
        print(f"Setting name to {name}")
        self.model.set_name(name)

    def get_screen(self):
        print("Getting screen")
        return self.screen.get_screen()
    
    def draw_background(self):
        print("Drawing background")
        self.screen.get_screen().fill(self.screen.BG1)
        counter = 0  
        for row in range(self.screen.get_squares()):
            for col in range(self.screen.get_squares()):
                if counter % 2 == 0:
                    pygame.draw.rect(self.screen.get_screen(), self.screen.get_BG2(), (col * self.screen.get_screen_pixels(), row * self.screen.get_screen_pixels(), self.screen.get_screen_pixels(), self.screen.get_screen_pixels()))
                counter += 1
            counter += 1
    
    #Player Movement
    def track_player_movement(self):
        print("Tracking player movement")
        keys = pygame.key.get_pressed()
        print("--------\nself.dt: ", self.dt)
        if keys[pygame.K_w] and self.snake.current_direction != "s":
            self.snake.player_vel_x = 0
            self.snake.player_vel_y = - self.snake.movement_speed * self.dt
            self.snake.current_direction = "w"
        if keys[pygame.K_s] and self.snake.current_direction != "w":
            self.snake.player_vel_x = 0
            self.snake.player_vel_y = self.snake.movement_speed * self.dt
            self.snake.current_direction = "s"
        if keys[pygame.K_a] and self.snake.current_direction != "d":
            self.snake.player_vel_y = 0
            self.snake.player_vel_x = - self.snake.movement_speed * self.dt
            self.snake.current_direction = "a"
        if keys[pygame.K_d] and self.snake.current_direction != "a":
            self.snake.player_vel_y = 0
            self.snake.player_vel_x = self.snake.movement_speed * self.dt
            self.snake.current_direction = "d"
        print(f"player_vel_x: {self.snake.player_vel_x}, player_vel_y: {self.snake.player_vel_y}, current_direction: {self.snake.current_direction}")
        
        self.snake.set_x_cord(self.snake.get_x_cord() + self.snake.player_vel_x)
        self.snake.set_y_cord(self.snake.get_y_cord() + self.snake.player_vel_y )

    def update_player_pos(self):
        print("Updating player position")
        self.x_cord += self.player_vel_x 
        self.y_cord += self.player_vel_y
        
    def check_boundries(self):
        print("Checking boundaries")
        if self.snake.x_cord <= (- self.screen.get_screen_pixels() / 2): #Left x coord
            pygame.quit()
        elif self.snake.x_cord >= self.screen.get_screen_width() - (self.screen.get_screen_pixels() / 2):
            pygame.quit()
        if self.snake.y_cord <= (-self.screen.get_screen_pixels() / 2): #Top y coord
            pygame.quit()
        elif self.snake.y_cord >= self.screen.get_screen_height() - (self.screen.get_screen_pixels() / 2): #Bottom y coord
            pygame.quit()
            
    def get_distance(self):
        print("Getting distance")
        distance = math.sqrt(pow(self.food.x_cord - self.snake.x_cord, 2) + pow(self.food.y_cord - self.snake.y_cord, 2))
        return distance
    
    def spawn_food(self):
        print("Spawning food")
        pygame.draw.rect(self.screen.get_screen(), "red", [(self.food.x_cord, self.food.y_cord), (self.screen.get_screen_pixels(), self.screen.get_screen_pixels())])
        self.ate = False

    def check_food(self):
        print("Checking food")
        distance = self.get_distance()
        if distance < self.screen.get_screen_pixels():
            print("Food eaten")
            self.scoreboard.score += 1
            self.snake.movement_speed += 10
            self.snake.snake_cord.append(self.snake.snake_directional())
            #Update the food rectangle
            self.screen.update(self.food._shape)
            
            #Respawn the food
            self.food.x_cord = random.randrange(0, self.screen.get_screen_width() - self.screen.get_screen_pixels(), 32)
            self.food.y_cord = random.randrange(0, self.screen.get_screen_height() - self.screen.get_screen_pixels(), 32)
            #Draw food again
            self.ate = True
            self.spawn_food()    
        print(f"distance: {distance}, score: {self.scoreboard.score}, movement_speed: {self.snake.movement_speed}")