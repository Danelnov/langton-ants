import numpy as np
import pygame
from ant import Ant


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Size in pixels of each frame
HEIGHT = 10
WIDHT = 10

grid = np.zeros((70, 70)) # Total board size 70x70
ant = Ant([35, 35]) # Place the ant in the center of the board

pygame.init()

screen = pygame.display.set_mode((700, 700))
pygame.display.set_caption("langton's ant")
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break
        
    # Move the ant
    row, column = ant.position # Get the current state of the cell
    ant.move(grid[row, column])
    # Update the cell state
    if grid[row, column] == 0:
        grid[row, column] = 1
    else:
        grid[row, column] = 0
    
    screen.fill(BLACK)
    
    # change color each frame
    for row in range(70):
        for column in range(70):
            if [row, column] == ant.position:
                color = RED
            elif grid[row, column] == 0:
                color = BLACK
            else:
                color = WHITE
            pygame.draw.rect(
                screen, color, 
                (HEIGHT*column, WIDHT*row, HEIGHT, WIDHT))
    
    # Reload
    clock.tick(60)
    pygame.display.flip()

pygame.quit()
