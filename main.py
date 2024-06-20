import pygame
from controller import Controller  # assuming controller.py is in the same directory
# game utils class
from scoreboard import ScoreBoard


#  init controller
controller = Controller()

#get Screen
screen = controller.get_screen()

    
# Game Program Loop
# while controller.run_status:
while controller.run_status:  
    print("game is running ..")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_status = False
    
    #Draw the background     
    controller.draw_background()
    controller.spawn_food()
    
    
    #Head of snake drawn
    controller.snake.snake_draw()
    
    #Player Movement
    controller.track_player_movement()
 
    # update snake body
    controller.snake.snake_update()
    
    #Boundaries      
    controller.check_boundries()
        
    # Spawnss
    controller.check_food()
         
    # Update the display
    # pygame.display.update()
    
    pygame.display.flip()
    
    controller.dt = controller.clock.tick(35) / 1000

pygame.quit()