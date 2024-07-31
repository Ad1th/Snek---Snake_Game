import pygame
import pygame.locals
import random
pygame.init()

# Window size
window_x = 780
window_y = 620

#Defining colours
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)


win = pygame.display.set_mode((window_x,window_y))
pygame.display.set_caption("pYtHoN")

x = 50
y = 50
width = 20
height = 20
vel = 15 

# defining snake default position and direction
snake_position = [100, 50]
direction = 'RIGHT'
change_to = direction

# defining first 4 blocks of snake body
snake_body = [  [100, 50],
                [90, 50],
                [80, 50],
                [70, 50]
             ]
snake_spawn = True

# fruit position
fruit_position = [random.randrange(1, (window_x//10)) * 10,
                  random.randrange(1, (window_y//10)) * 10]
fruitposition = [90,90]
fruit_spawn = True
fruitcolour = green
 
# setting default snake direction
# towards right
direction = 'RIGHT'
change_to = direction


font = pygame.font.Font('freesansbold.ttf', 32)
 
# defining colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
snakecolour = red
snakecolour2 = green
def game_over():
    text2 = font.render('GAME OVER', True, red, blue)
    textRect2 = text2.get_rect()
    textRect2.center = (fruit_position[0],fruit_position[1])
    win.blit(text2, textRect2)

run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_ESCAPE]:
           run = False
           
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        x-=vel
        if direction != 'Right':
            direction = 'Left'
            snake_position[0] -= 10


    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        x += vel
        if direction != 'LEFT':
            direction = 'RIGHT'
            snake_position[0] += 10

    if keys[pygame.K_UP] or keys[pygame.K_w]:
        y -= vel
        if direction != 'DOWN':
            direction = 'UP'
            snake_position[1] -= 10

    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        y += vel
        if (direction != 'UP'):
            direction = 'DOWN'
            snake_position[1] += 10

    #Snake body growing mechanism
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
        #score += 10
        fruit_spawn = False
    else:
        snake_body.pop()

    #Snake Movement
    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'RIGHT':
        snake_position[0] += 10

    
     # Game Over conditions
    if (snake_position[0] < 0 or snake_position[0] > window_x-10):
        game_over()
    if (snake_position[1] < 0 or snake_position[1] > window_y-10):
        game_over()
    win.fill(black)
	
    #for pos in snake_body:
     #   pygame.draw.rect(win, green,pygame.rect(pos[0], pos[1], 10, 10))
    
    #fruit_position[0], fruit_position[1], 10, 10))

# Touching the snake body
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()
        
    text2 = font.render('Mode 2', True, green, blue)
    textRect2 = text2.get_rect()
    textRect2.center = (fruit_position[0],fruit_position[1])
                        
    win.fill((0,0,0))
    pygame.draw.rect(win, snakecolour2, (x, y, width, height))  
    if snake_spawn == True:
        pygame.draw.rect(win, snakecolour,(snake_body[0][0],snake_body[0][1],  width, height))
        pygame.draw.rect(win, snakecolour,(snake_body[1][0],snake_body[1][1],  width, height))
        pygame.draw.rect(win, snakecolour,(snake_body[2][0],snake_body[2][1],  width, height))
        pygame.draw.rect(win, snakecolour,(snake_body[3][0],snake_body[3][1],  width, height))
    
    fruit_spawn = True
    if fruit_spawn == True:
        pygame.draw.rect(win, fruitcolour,(fruit_position[0], fruit_position[1], 10,10))
        #pygame.draw.rect(win, (255, 255, 0), (food_x, food_y, 20, 20))
    #fruit_position = [random.randrange(1, (window_x//10)) * 10,
                  #random.randrange(1, (window_y//10)) * 10]
    pygame.display.update()
    
pygame.quit()
quit()
