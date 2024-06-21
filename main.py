import pygame
from controller import Controller 
from scoreboard import ScoreBoard


# inilize controller object
controller = Controller()


screen = controller.get_screen()

    
# Game Program Loop
# while controller.run_status:
while controller.get_run_status:  
    print("game is running ..")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_status = False
   
    #Draw the background     
    controller.draw_background()
    
    
    #draw scoreboard
    controller.scoreboard.draw_scoreboard(screen)
    
    #
    controller.spawn_food()
    
    
    #Head of snake drawn
    controller.snake.snake_draw()
    
    controller.set_run_status(controller.snake.check_snake_collide_with_self(controller.scoreboard.get_score()))
    print("run_status: ..", controller.get_run_status())
    
    controller.scoreboard.update_highscore()  
    controller.check_boundries()
     
    
    #Player Movement
    controller.track_player_movement()
    controller.check_boundries()
    # update snake body
    controller.snake.snake_update()
    
    #Boundaries 
       
    
        
    # Spawnss
    controller.check_food()
         
    # Update the display
    # pygame.display.update
    # ()
    
    controller.scoreboard.update_highscore()
    pygame.display.flip()
    
    controller.dt = controller.clock.tick(35) / 1000

pygame.quit()