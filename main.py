import pygame
from controller import Controller 
from scoreboard import ScoreBoard


# inilize controller object
controller = Controller()


screen = controller.get_screen()

# starting game loop
while controller.get_run_status:  
    print("game is running ..")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_status = False
    controller.draw_background()
    controller.scoreboard.draw_scoreboard(screen)
    controller.spawn_food()
    controller.snake.snake_draw()
    controller.set_run_status(controller.snake.check_snake_collide_with_self(controller.scoreboard.get_score()))
    print("run_status: ..", controller.get_run_status())
    controller.scoreboard.update_highscore()  
    controller.check_boundries()
    controller.track_player_movement()
    controller.check_boundries()
    controller.snake.snake_update()
    controller.check_food()
    controller.scoreboard.update_highscore()
    pygame.display.flip()
    controller.dt = controller.clock.tick(35) / 1000

pygame.quit()