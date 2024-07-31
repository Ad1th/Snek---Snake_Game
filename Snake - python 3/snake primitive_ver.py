import pygame
import random

width = 1600
height = 700

# Initialize pygame and create window
pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Initialize snake and food coordinates
snake_body = [[width/2-20,height/2],[width/2-40,height/2],[width/2-60,height/2],[width/2-80,height/2]]
food_x = width/2-20
food_y = height/2
snake_speed = 0.5
snake_direction = "right"

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and snake_direction != "right":
                snake_direction = "left"
            elif event.key == pygame.K_RIGHT and snake_direction != "left":
                snake_direction = "right"
            elif event.key == pygame.K_UP and snake_direction != "down":
                snake_direction = "up"
            elif event.key == pygame.K_DOWN and snake_direction != "up":
                snake_direction = "down"

    # Move the snake and check if it's out of bounds
    for i in range(len(snake_body) - 1, 0, -1):
        snake_body[i][0] = snake_body[i-1][0]
        snake_body[i][1] = snake_body[i-1][1]
    if snake_direction == "right":
        snake_body[0][0] += snake_speed
    elif snake_direction == "left":
        snake_body[0][0] -= snake_speed
    elif snake_direction == "up":
        snake_body[0][1] -= snake_speed
    elif snake_direction == "down":
        snake_body[0][1] += snake_speed
    if snake_body[0][0] > width-20 or snake_body[0][0] < 0 or snake_body[0][1] > height-20 or snake_body[0][1] < 0:
        running = False

    # Draw the snake and food
    screen.fill((0, 0, 0))
    for i in range(len(snake_body)):
        pygame.draw.rect(screen, (255, 0, 0), (snake_body[i][0], snake_body[i][1], 20, 20))
    pygame.draw.rect(screen, (0, 255, 0), (food_x, food_y, 20, 20))

    # Check if snake and food overlap
    if snake_body[0][0] == food_x and snake_body[0][1] == food_y:
        food_x = random.randint(0, width-20)
        food_y = random.randint(0, height-20)
        snake_speed += 0.1
        snake_body.append([snake_body[-1][0],snake_body[-1][1]])
    pygame.display.update()

# Quit pygame and exit program
pygame.quit()
