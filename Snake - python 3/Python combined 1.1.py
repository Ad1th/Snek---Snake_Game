import pygame
import random



#First part of the game
# Game Menu and settings
pygame.init()
pygame.display.set_caption("Snake game")




#Defining colours
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
yellow = pygame.Color(255,255,0)

bgcolour = black
X = 1366
Y = 700
display_surface = pygame.display.set_mode((X, Y))

font = pygame.font.Font('freesansbold.ttf', 32)

def optionwindow():
    Mainheading= font.render('Game Menu', True, red, blue)
    MainheadingRect = Mainheading.get_rect()
    MainheadingRect.center = (550,50)

    texta = font.render('Choose Game Mode:', True, green, blue)
    textRecta = texta.get_rect()
    textRecta.center = (180,200)
    
    text1 = font.render('1:Normal', True, green, blue)
    textRect1 = text1.get_rect()
    textRect1.center = (110,240)

    text2 = font.render('2: Peace Mode', True, green, blue)
    textRect2 = text2.get_rect()
    textRect2.center = (155,280)

    text3 = font.render('3: Obstacle mode', True, green, blue)
    textRect3 = text3.get_rect()
    textRect3.center = (180,320)

    text4 = font.render('Choose B nd colour:', True, green, blue)
    textRect4 = text4.get_rect()
    textRect4.center = (1000,200)

    text5 = font.render('g-Green', True, green, blue)
    textRect5 = text5.get_rect()
    textRect5.center = (1000,240)

    text6 = font.render('b-Black', True, green, blue)
    textRect6 = text6.get_rect()
    textRect6.center = (1000,280)

    text7 = font.render('w-White', True, green, blue)
    textRect7 = text7.get_rect()
    textRect7.center = (1000,320)

    text8 = font.render('r-Red', True, green, blue)
    textRect8 = text8.get_rect()
    textRect8.center = (1000,360)

    strttxt = font.render("Press spacebar to Start", True, (255,255,0), blue)
    strttxtrect =  strttxt.get_rect()
    strttxtrect.center = (650,600)

    display_surface.fill(blue)
    display_surface.blit(Mainheading,MainheadingRect)
    display_surface.blit(texta, textRecta)
    display_surface.blit(text1, textRect1)
    display_surface.blit(text2, textRect2)
    display_surface.blit(text3, textRect3)
    display_surface.blit(text4,textRect4)
    display_surface.blit(text5,textRect5)
    display_surface.blit(text6,textRect6)
    display_surface.blit(text7,textRect7)
    display_surface.blit(text8,textRect8)
    display_surface.blit(strttxt, strttxtrect)

optionwindow()

running = True
while running:
    # iterate over the list of Event objects
    # that was returned by pygame.event.get() method.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        pygame.display.update()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_1]:
            mode = 'normal'
            optionwindow()
            arrow = font.render('<---', True, red, blue)
            arrowrect= arrow.get_rect()
            arrowrect.center = (380,240)
            display_surface.blit(arrow, arrowrect)

    elif keys[pygame.K_2]:
            mode = 'peace'
            optionwindow()
            arrow = font.render('<---', True, red, blue)
            arrowrect= arrow.get_rect()
            arrowrect.center = (400,280)
            display_surface.blit(arrow, arrowrect)

    elif keys[pygame.K_3]:
            mode = 'obstacle'
            optionwindow()
            arrow = font.render('<---', True, red, blue)
            arrowrect= arrow.get_rect()
            arrowrect.center = (450,320)
            display_surface.blit(arrow, arrowrect)

    if keys[pygame.K_ESCAPE]:
           running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_g]:
        bgcolour= green
        optionwindow()
        arrow2 = font.render('<---', True, red, blue)
        arrow2rect= arrow2.get_rect()
        arrow2rect.center = (1120,240)
        display_surface.blit(arrow2, arrow2rect)
    
    elif keys[pygame.K_b]:
        bgcolour= black
        optionwindow()
        arrow2 = font.render('<---', True, red, blue)
        arrow2rect= arrow2.get_rect()
        arrow2rect.center = (1120,280)
        display_surface.blit(arrow2, arrow2rect)


    elif keys[pygame.K_w]:
        bgcolour= white
        optionwindow()
        arrow2 = font.render('<---', True, red, blue)
        arrow2rect= arrow2.get_rect()
        arrow2rect.center = (1120,320)
        display_surface.blit(arrow2, arrow2rect)
        
    elif keys[pygame.K_r]:
        bgcolour= red
        optionwindow()
        arrow2 = font.render('<---', True, red, blue)
        arrow2rect= arrow2.get_rect()
        arrow2rect.center = (1120,360)
        display_surface.blit(arrow2, arrow2rect)
        
    if keys[pygame.K_SPACE]:
        running = False



#Second part of the game 
#The actual game

# Window size
window_x = 1350
window_y = 710

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

snake_body = [[20,40],[40,40],[60,40],[80,40]]
snake_speed = 20
snake_direction = "right"

snake_spawn = True
# fruit position
food_x = 600
food_y = 600
food_colour = yellow

score = 0

# setting default snake direction
# towards right
direction = 'RIGHT'
chngdirection = direction


font = pygame.font.Font('freesansbold.ttf', 32)
 

snakecolour = red
snakecolour2 = green

def game_over():
    overtxt = font.render('GAME OVER', True, red, blue)
    overtxtrect = overtxt.get_rect()
    overtxtrect.center = (500,500)
    win.blit(overtxt, overtxtrect)

    


run = True
while run:
    pygame.time.delay(100)
    win.fill(bgcolour)
    pygame.display.update()
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_ESCAPE]:
           run = False

    if snake_spawn == True:
        pygame.draw.rect(win, snakecolour,(snake_body[0][0],snake_body[0][1],  width, height))
        pygame.draw.rect(win, snakecolour,(snake_body[1][0],snake_body[1][1],  width, height))
        pygame.draw.rect(win, snakecolour,(snake_body[2][0],snake_body[2][1],  width, height))
        pygame.draw.rect(win, snakecolour,(snake_body[3][0],snake_body[3][1],  width, height))

    fruit_spawn = True
    if fruit_spawn == True:
        pygame.draw.rect(win, food_colour, (food_x, food_y, width, height))
    op = '''

    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        x-=vel
        if direction != 'Right':
            direction = 'Left'
            snake_position[0] -= 20
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
            snake_position[1] +=10
    '''
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
       
        # Check if snake and food overlap
    if snake_body[0][0] == food_x and snake_body[0][1] == food_y:
        food_x = 20*(random.randint(0, (width/2)))
        food_y = 20*(random.randint(0, (height/2)))
        snake_body.append([snake_body[-1][0],snake_body[-1][1]])
        pygame.display.update()
    
    # Draw the snake and food
    win.fill((0, 0, 0))
    for i in range(len(snake_body)):
        pygame.draw.rect(win, (255, 0, 0), (snake_body[i][0], snake_body[i][1], 20, 20))
    pygame.draw.rect(win, (0, 255, 0), (food_x, food_y,20,20))

    op2 = '''               
    #Snake Movement
    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'RIGHT':
        snake_position[0] += 10
    '''
    
    op3 = '''
    #Snake body growing mechanism
    snake_body.insert(0, list(snake_position))
    if snake_body[0][0] == food_x and snake_body[0][1] == food_y:
        score += 1
        food_x = random.randint(20, window_x-20)
        food_y = random.randint(20, window_y-20)
    else:
        snake_body.pop(-1)

    #Collision detection: 
    if snake_body[0][0] == food_x and snake_body[0][1] == food_y:
        food_x = random.randint(20, window_x-20)
        food_y = random.randint(20, window_y-20)
        score+=1
        pygame.display.update()
        '''
    #if snake_body[0][0]>window_x or snake_body[0][0]<0 or snake_body[0][1]()>window_y or snake_body[0][1]<0:
        #time.sleep(1)
        #snake_body.goto(0,0)
        #snake_body = "stop"
 
    #Game over conditions:
    #CODE IT!!
    
    sc = font.render('Score:', True, yellow, black)
    screct = sc.get_rect()
    screct.center = (550,50)
    display_surface.blit(sc,screct) 
    

    

    
pygame.quit()
