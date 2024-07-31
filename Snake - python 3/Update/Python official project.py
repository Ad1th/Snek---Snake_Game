import pygame
import random
pygame.init()



def game_over():
    text2 = font.render('GAME OVER', True, red, blue)
    textRect2 = text2.get_rect()
    textRect2.center = (fruit_position[0],fruit_position[1])
    win.blit(text2, textRect2)
    
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)


X = 1366
Y = 700
display_surface = pygame.display.set_mode((X, Y))

font = pygame.font.Font('freesansbold.ttf', 32)

texta = font.render('Choose Game Mode:', True, green, blue)
textRecta = texta.get_rect()
textRecta.center = (180,40)
    
text1 = font.render('Mode 1', True, green, blue)
textRect1 = text1.get_rect()
textRect1.center = (180,80)

text2 = font.render('Mode 2', True, green, blue)
textRect2 = text2.get_rect()
textRect2.center = (180,120)

text3 = font.render('Mode 3', True, green, blue)
textRect3 = text3.get_rect()
textRect3.center = (180,160)

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

display_surface.fill(blue)
display_surface.blit(texta, textRecta)
display_surface.blit(text1, textRect1)
display_surface.blit(text2, textRect2)
display_surface.blit(text3, textRect3)
display_surface.blit(text4,textRect4)
display_surface.blit(text5,textRect5)
display_surface.blit(text6,textRect6)
display_surface.blit(text7,textRect7)
display_surface.blit(text8,textRect8)


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
           running = False
           mode = 1
        
    if keys[pygame.K_g]:
        bgcolour= green

    if keys[pygame.K_w]:
        bgcolour= white
        
    if keys[pygame.K_r]:
        bgcolour= red
        
    if keys[pygame.K_b]:
        bgcolour= black
# Window size
window_x = 780
window_y = 620

win = pygame.display.set_mode((window_x,window_y))
pygame.display.set_caption("pYtHoN")

x = 50
y = 50
width = 40
height = 60
vel = 15 

# defining snake default position
snake_position = [100, 50]
 
# defining first 4 blocks of snake
# body
snake_body = [  [100, 50],
                [90, 50],
                [80, 50],
                [70, 50]
             ]

# fruit position
fruit_position = [random.randrange(1, (window_x//10)) * 10,
                  random.randrange(1, (window_y//10)) * 10]
fruitposition = [90,90]
fruit_spawn = True
 
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
        x -= vel

    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        x += vel

    if keys[pygame.K_UP] or keys[pygame.K_w]:
        y -= vel

    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        y += vel
        
     # Game Over conditions
    if (snake_position[0] < 0 or snake_position[0] > window_x-10):
        game_over()
    if (snake_position[1] < 0 or snake_position[1] > window_y-10):
        game_over()
        
    text2 = font.render('Mode 2', True, green, blue)
    textRect2 = text2.get_rect()
    textRect2.center = (fruit_position[0],fruit_position[1])
                        
    win.fill(bgcolour)
    pygame.draw.rect(win, (255,0,0), (x, y, width, height))   
    pygame.display.update()
    if fruit_spawn == True:
        win.blit(text2, textRect2)
    
pygame.quit()
