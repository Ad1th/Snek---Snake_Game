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
    MainheadingRect.center = (650,50)

    texta = font.render('Choose Game Mode:', True, green, blue)
    textRecta = texta.get_rect()
    textRecta.center = (180,200)
    
    text1 = font.render('1:Normal', True, green, blue)
    textRect1 = text1.get_rect()
    textRect1.center = (110,240)

    text2 = font.render('2: Peace Mode', True, green, blue)
    textRect2 = text2.get_rect()
    textRect2.center = (155,280)

    text4 = font.render('Choose Background colour:', True, green, blue)
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
window_x = 1360
window_y = 720

win = pygame.display.set_mode((window_x,window_y))
pygame.display.set_caption("pYtHoN")
win.fill(bgcolour)
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
    snake_speed=0
    overtxt = font.render('GAME OVER', True, red, blue)
    overtxtrect = overtxt.get_rect()
    overtxtrect.center = (500,500)
    win.blit(overtxt, overtxtrect)
    pygame.time.delay(1000)
    

    


run = True
while run:
    pygame.time.delay(70)
    win.fill(bgcolour)
    
    
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

    if (snake_body[0][0] < 0 or snake_body[0][1] < 0):
        snake_speed = 0
        while True:
            overtxt = font.render('GAME OVER, SCORE: ', True, red, bgcolour)
            overtxtrect = overtxt.get_rect()
            overtxtrect.center = (650,320)
            scoretext2 = font.render(score, True, red, bgcolour)
            scoretextrect2 = scoretext2.get_rect()
            scoretextrect2.center = (850, 320)
            win.blit(overtxt, overtxtrect)
            win.blit(scoretext2,scoretextrect2)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                if keys[pygame.K_ESCAPE]:
                    running = False
    if (snake_body[0][0]>window_x or snake_body[0][1] > window_y):
        snake_speed = 0
        while True:
            overtxt = font.render('GAME OVER, SCORE: ', True, red, bgcolour)
            overtxtrect = overtxt.get_rect()
            overtxtrect.center = (650,320)
            scoretext2 = font.render(score, True, red, bgcolour)
            scoretextrect2 = scoretext2.get_rect()
            scoretextrect2.center = (850, 320)
            win.blit(overtxt, overtxtrect)
            win.blit(scoretext2,scoretextrect2)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                if keys[pygame.K_ESCAPE]:
                    running = False





    score = int(score)   
        # Check if snake and food overlap
    if snake_body[0][0] == food_x and snake_body[0][1] == food_y:
        food_x = 20*(random.randint(0, (width)))
        food_y = 20*(random.randint(0, (height)))
        snake_body.append([snake_body[-1][0],snake_body[-1][1]])
        score+=1
        pygame.display.update()
    
    # Draw the snake and food
    win.fill((0, 0, 0))
    for i in range(len(snake_body)):
        pygame.draw.rect(win, (255, 0, 0), (snake_body[i][0], snake_body[i][1], 20, 20))
    pygame.draw.rect(win, (0, 255, 0), (food_x, food_y,20,20))

    
    #Collision detection: 
    if snake_body[0][0] == food_x and snake_body[0][1] == food_y:
        food_x = random.randint(20, window_x-20)
        food_y = random.randint(20, window_y-20)
        score+=1

    
    sc = font.render('Score:', True, yellow, black)
    screct = sc.get_rect()
    screct.center = (550,50)
    score = str(score)
    sc2 = font.render(score, True, yellow, black)
    sc2rect = sc2.get_rect()
    sc2rect.center = (620,50)
    display_surface.blit(sc,screct) 
    display_surface.blit(sc2,sc2rect)
    
    pygame.display.update()
    

    

    
pygame.quit()
