# PyGame-Snake
**Python Snake Pygame**

**Goal of Project:**

*Goal:* To be exposed to Python's syntax and logic; as well as to learn how to connect and effectively utilize available libraries on Python.


**Definiton of Done:**

*Definition:* Fully working Snake game using Python. Must abide by basic Snake game parameters and work according to specifications.

**Done**

- *Randomized food spread:* When the player touches food, the food disappears, and new food generates. The solution involves using the Distance formula to calculate the distance between the player's head and the food. Upon collision, the background redraws, and the food's position regenerates randomly.

- *Counter (Points):* The counter changes with each food item eaten by the player. It's calculated by checking when the head is within 15 pixels of the food. If so, 1 is added to the score counter.

- *Movement (According to length):* The snake's head points in the direction of key presses, while remaining segments follow suit. Movement remains constant in one direction, requiring another key press to change direction.

- *Segmentation:* Implement a function that recognizes when the snake eats food, adding a new segment of the same size as the head to follow the head's movement.

**To Do**
- *Endgame conditions:* Define conditions for the game to end, such as the snake touching itself or the game boundaries. A `player_death()` function could be triggered when the distance between the head and body or head and boundaries reaches a certain value.

- *Restart button:* Create a simple restart button that resets the game to its default settings.

-*Refinements*: Head/Body Collision, Food can't spawn inside body, Gridlocked movement

