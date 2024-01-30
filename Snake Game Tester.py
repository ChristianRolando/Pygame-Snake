#function to update the head of the snake and update the rest of the snake to the coordinates of the previous snake preceeding them
update_x = 4
update_y = 3
snake = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5]]

def update_snake(snake, update_x, update_y):
    
    head = snake[0].copy()
    print("head:", head)

    snake[0][0] += update_x
    snake[0][1] += update_y
    
    snake[1] = head

    print("snake after head update:", snake)

    for i in range(len(snake)-1, 0, -1):
        snake[i] = snake[i-1]

    print("new snake:               ", snake)

update_snake(snake, update_x, update_y)
