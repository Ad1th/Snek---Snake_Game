import pygame
pygame.init()

white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)

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
    
display_surface.fill(blue)
display_surface.blit(texta, textRecta)
display_surface.blit(text1, textRect1)
display_surface.blit(text2, textRect2)
display_surface.blit(text3, textRect3)

run = True
while run:
    
    # iterate over the list of Event objects
    # that was returned by pygame.event.get() method.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        pygame.display.update()
