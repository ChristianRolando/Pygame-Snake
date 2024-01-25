import pygame
import random
import math

# Constants
WIDTH = 640
HEIGHT = 640
PIXELS = 32
SQUARES = int(WIDTH / PIXELS)
BG1 = (156, 210, 54)
BG2 = (147, 203, 57)

# Player
player_vel_x = 1
player_vel_y = 0 
movement_speed = 250
snake_segments = [(240, 240), (208, 240), (176, 240)]   #head is pos at (240, 240), body starts at (208,240)

# Food
food_pos_x = random.randrange(0, WIDTH - PIXELS, 32)
food_pos_y = random.randrange(0, HEIGHT - PIXELS, 32)

# Pygame Setup
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True
dt = 0
score_value = 0
scoreboard_x_coord = 240
scoreboard_y_coord = 5

# Functions
def draw_background(screen):
    screen.fill(BG1)
    counter = 0
    for row in range(SQUARES):
        for col in range(SQUARES):
            if counter % 2 == 0:
                pygame.draw.rect(screen, BG2, (col * PIXELS, row * PIXELS, PIXELS, PIXELS))
            if col == SQUARES - 1:
                continue
            counter += 1

def draw_scoreboard(screen, score_value, x, y):
    font = pygame.font.Font("freesansbold.ttf", 32)
    score = font.render("Score: " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def spawn_food(screen, x, y):
    pygame.draw.rect(screen, "red", [(x, y), (PIXELS, PIXELS)])
    

# Game Program Loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    draw_background(screen)
    
    #Updaste snake head position
    head = snake_segments[0]
    new_head = (head[0] + player_vel_x * 32, head[1] + player_vel_y * 32)
    snake_segments = [new_head] + snake_segments[:-1]
    
    for i in range(1, len(snake_segments)):
        snake_segments[i] = snake_segments[i - 1]
    
    pygame.draw.rect(screen, "purple", [(head), (PIXELS, PIXELS)])
    pygame.draw.rect(screen, "red", [(new_head), (PIXELS, PIXELS)])
    
   # Player Movement
keys = pygame.key.get_pressed()
if keys[pygame.K_w]:
    player_vel_x = 0
    player_vel_y = -movement_speed * dt
if keys[pygame.K_s]:
    player_vel_x = 0
    player_vel_y = movement_speed * dt
if keys[pygame.K_a]:
    player_vel_y = 0
    player_vel_x = -movement_speed * dt
if keys[pygame.K_d]:
    player_vel_y = 0
    player_vel_x = movement_speed * dt

# Update snake head position
head = snake_segments[0]
new_head = (head[0] + player_vel_x * PIXELS, head[1] + player_vel_y * PIXELS)
snake_segments = [new_head] + snake_segments[:-1]

# Boundaries
if new_head[0] <= 0:
    new_head = (0, new_head[1])
elif new_head[0] >= WIDTH - PIXELS:
    new_head = (WIDTH - PIXELS, new_head[1])

if new_head[1] <= 0:
    new_head = (new_head[0], 0)
elif new_head[1] >= HEIGHT - PIXELS:
    new_head = (new_head[0], HEIGHT - PIXELS)

# Rest of the code remains the same...

        
    #Food Handling
    spawn_food(screen, food_pos_x, food_pos_y)   
    distance_head_food = math.sqrt(pow(food_pos_x - player_pos_x, 2) + pow(food_pos_y - player_pos_y, 2))
    if distance_head_food < PIXELS:
        score_value += 1
        draw_background(screen)
        food_pos_x = random.randrange(0, WIDTH - PIXELS, 32)
        food_pos_y = random.randrange(0, HEIGHT - PIXELS, 32)
        spawn_food(screen, food_pos_x, food_pos_y)

    draw_scoreboard(screen, score_value, scoreboard_x_coord, scoreboard_y_coord)

    pygame.display.flip()
    
    dt = clock.tick(60) / 1000

pygame.quit()
