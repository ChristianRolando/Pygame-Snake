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
player_vel_x = 0
player_vel_y = 0
player_pos_x = 240
player_pos_y = 240
movement_speed = 400
current_direction = " "
snake_body = [[player_pos_x, player_pos_y],[208, player_pos_y], [176, player_pos_y]]
update_seg = 0

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
    
def snake_update(snake_body, player_pos_x, player_pos_y):
    new_head = [player_pos_x, player_pos_y]
    
    snake_body.insert(0, new_head)
    snake_body.pop()
    
def snake_draw(snake_body):
    for i in snake_body:
        pygame.draw.rect(screen, "purple", [(i), (PIXELS, PIXELS)])
        
def snake_directional(current_direction, snake_body):
    if current_direction == 'd':
        update_seg = [snake_body[-1][0] - 32, snake_body[-1][1]]
    if current_direction == 'a':
        update_seg = [snake_body[-1][0] + 32, snake_body[-1][1]]
    if current_direction == 'w':
        update_seg = [snake_body[-1][0], snake_body[-1][1] - 32]
    if current_direction == 's':
        update_seg = [snake_body[-1][0], snake_body[-1][1] + 32]
    return update_seg
    
# Game Program Loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    #Draw the background     
    draw_background(screen)
    
    #Head of snake drawn
    # pygame.draw.rect(screen, "purple", [(player_pos_x, player_pos_y), (PIXELS, PIXELS)])
    snake_draw(snake_body)
    
    #Player Movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and current_direction != "s":
        player_vel_x = 0
        player_vel_y = -movement_speed * dt
        current_direction = "w"
    if keys[pygame.K_s] and current_direction != "w":
        player_vel_x = 0
        player_vel_y = movement_speed * dt
        current_direction = "s"
    if keys[pygame.K_a] and current_direction != "d":
        player_vel_y = 0
        player_vel_x = -movement_speed * dt
        current_direction = "a"
    if keys[pygame.K_d] and current_direction != "a":
        player_vel_y = 0
        player_vel_x = movement_speed * dt
        current_direction = "d"
        
    player_pos_x += player_vel_x 
    player_pos_y += player_vel_y 
    
    snake_update(snake_body, player_pos_x, player_pos_y)
    
    # for i in range(len(snake_body)):
    #     print("snake: , ith: ", i, snake_body[i])   
    # print(snake_body)

    #Boundaries
    if player_pos_x <= 0:
        player_pos_x = 0
    elif player_pos_x >= WIDTH - PIXELS:
        player_pos_x = WIDTH - PIXELS

    if player_pos_y <= 0:
        player_pos_y = 0
    elif player_pos_y >= HEIGHT - PIXELS:
        player_pos_y = HEIGHT - PIXELS
        
    #Food Handling
    spawn_food(screen, food_pos_x, food_pos_y)   
    distance_head_food = math.sqrt(pow(food_pos_x - player_pos_x, 2) + pow(food_pos_y - player_pos_y, 2))
    if distance_head_food < PIXELS:
        score_value += 1
        snake_body.append(snake_directional(current_direction, snake_body))
        draw_background(screen)
        food_pos_x = random.randrange(0, WIDTH - PIXELS, 32)
        food_pos_y = random.randrange(0, HEIGHT - PIXELS, 32)
        spawn_food(screen, food_pos_x, food_pos_y)

    draw_scoreboard(screen, score_value, scoreboard_x_coord, scoreboard_y_coord)

    pygame.display.flip()
    
    dt = clock.tick(30) / 1000
    
    #blah blah

pygame.quit()