# Example file showing a circle moving on screen
from board import boards
import pygame
import math

# pygame setup
pygame.init()
WIDTH = 900
HEIGHT = 950
screen = pygame.display.set_mode([WIDTH, HEIGHT])
clock = pygame.time.Clock()
running = True
dt = 0
font = pygame.font.Font('freesansbold.ttf', 20)
level = boards
color = "blue" 
PI = math.pi
vx = 80
vy = 0
count = 0


rec1 = pygame.Rect(0,0,950, 40)
rec2 = pygame.Rect(348,380,205,110)
rec3 = pygame.Rect(0,0,45,410)
rec4 = pygame.Rect(110,100,85,50)
rec5 = pygame.Rect(708,100,85,50)
rec6 = pygame.Rect(260,100,115,50)
rec7 = pygame.Rect(528,100,117,50)
rec8 = pygame.Rect(112,212,78,25)
rec9 = pygame.Rect(712,212,78,25)
rec10 = pygame.Rect(256,210,30,195)
rec11 = pygame.Rect(618,208,30,200)
rec12 = pygame.Rect(260,295,115,30)
rec13 = pygame.Rect(528,295,110,30)
rec14 = pygame.Rect(345,210,210,30)
rec15 = pygame.Rect(436,220,30,105)
rec16 = pygame.Rect(618,465,30,110)
rec17 = pygame.Rect(258,465,30,110)
rec18 = pygame.Rect(346,545,210,30)
rec19 = pygame.Rect(345,210,210,30)
rec20 = pygame.Rect(436,550,30,105)
rec21 = pygame.Rect(260,630,115,30)
rec22 = pygame.Rect(528,630,110,30)
rec23 = pygame.Rect(258,715,30,110)
rec24 = pygame.Rect(618,715,30,110)
rec25 = pygame.Rect(112,630,78,25)
rec26 = pygame.Rect(712,630,78,25)
rec27 = pygame.Rect(112,800,265,25)
rec28 = pygame.Rect(528,800,265,30)
rec29 = pygame.Rect(165,630,30,110)
rec30 = pygame.Rect(708,630,30,110)
rec31 = pygame.Rect(346,713,210,30)
rec32 = pygame.Rect(436,720,30,105)
rec33 = pygame.Rect(860,0,45,410)
rec34 = pygame.Rect(0,880,900,30)
rec35 = pygame.Rect(436,50,30,105)
rec36 = pygame.Rect(860,450,45,850)
rec37 = pygame.Rect(0,450,45,850)
rec38 = pygame.Rect(20,300,180,100)
rec39 = pygame.Rect(20,470,180,100)
rec40 = pygame.Rect(700,300,180,100)
rec41 = pygame.Rect(700,470,180,100)
rec42 = pygame.Rect(20,710,80,30)
rec43 = pygame.Rect(790,710,80,30)
arena = [rec1, rec2, rec3, rec4, rec5, rec6, rec7, rec8, rec9, rec10, rec11, rec12, rec13, rec14, rec15, rec16, rec17, rec18, rec19, rec20, rec21, rec22, rec23, rec24, rec25, rec26, rec27, rec28, rec29,rec30, rec31, rec32, rec33, rec34, rec35, rec36, rec37, rec38, rec39, rec40, rec41, rec42, rec43]

#def draw_board
def draw_board():
    num1 = ((HEIGHT-50) // 32)
    num2 = (WIDTH // 30)
    for i in range(len(level)):
        for j in range(len(level[i])):
            if level[i][j] == 1: 
                pygame.draw.circle(screen, "white" , (j * num2 + (0.5 * num2), i * num1 + (0.5 * num1)), 4)
            if level[i][j] == 2:
                pygame.draw.circle(screen, "white" , (j * num2 + (0.5 * num2), i * num1 + (0.5 * num1)), 10)
            if level[i][j] == 3: 
                pygame.draw.line(screen, color, (j * num2 + (0.5 * num2), i * num1) , (j * num2 + (0.5 * num2) , i * num1 + num1), 3)  
            if level[i][j] == 4: 
                pygame.draw.line(screen, color, (j * num2, i * num1 + (0.5 * num1)) , (j * num2 + num2 , i * num1 + (0.5 * num1)), 3)  
            if level[i][j] == 5: 
               pygame.draw.arc(screen, color, [(j * num2 - (0.4 * num2))-2, (i * num1 + (0.5 * num1)), num2, num1], 0, PI/2, 3)
            if level[i][j] == 6: 
                pygame.draw.arc(screen, color, [(j * num2 + (0.5 * num2)), (i * num1 + (0.5 * num1)), num2, num1], PI/2 , PI, 3)
            if level[i][j] == 7: 
                pygame.draw.arc(screen, color, [(j * num2 + (0.5 * num2)), (i * num1 - (0.4 * num1)), num2, num1], PI , 3*PI/2, 3)
            if level[i][j] == 8: 
                pygame.draw.arc(screen, color, [(j * num2 - (0.4 * num2))-2, (i * num1 - (0.4 * num1)), num2, num1], 3*PI/2 , 2*PI, 3)
            if level[i][j] == 9: 
                pygame.draw.line(screen, "white" , (j * num2, i * num1 + (0.5 * num1)) , (j * num2 + num2 , i * num1 + (0.5 * num1)), 3)  

def eat():
    cell_height = ((HEIGHT-50) // 32)
    cell_width = (WIDTH // 30)
    index_y = round(pacman_pos.y / cell_height)

    index_x = round(pacman_pos.x / cell_width)
    if (level[index_y][index_x] == 1 or level[index_y][index_x] == 2):
        level[index_y][index_x] = 0

#carachteres
pacman_pos = pygame.Vector2(screen.get_width() / 18, screen.get_height() / 18)
pacmanimage = pygame.image.load ('pacman_o.png')
pacmanimage2 = pygame.image.load ('pacman_c.png')

while running:
    count += 1
    if count > 30:
        count = 0
    recpacman = pygame.Rect (pacman_pos.x, pacman_pos.y, 32, 32)
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")
    draw_board () 
    #for rec in arena:
        #pygame.draw.rect(screen, "red", rec, 0,20)
    
    pac_old_x = pacman_pos.x
    pac_old_y = pacman_pos.y

#moves
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        vx = 0
        vy = -80
        if pacman_pos.y - 150 * dt < 39:
            continue

    if keys[pygame.K_DOWN]:
        vx = 0
        vy = 80
        if pacman_pos.y + 150 * dt > 859:
            continue

    if keys[pygame.K_LEFT]:
        vx = -80
        vy = 0
        if pacman_pos.x - 150 * dt < 39:
            continue
    if keys[pygame.K_RIGHT]:
        vx = 80
        vy = 0
        if pacman_pos.x + 150 * dt > 859:
            continue
    
    pacman_pos.x += vx * dt
    pacman_pos.y += vy * dt
    eat()

    for rect in arena:
        collide = pygame.Rect.colliderect(rect, recpacman)
        if collide:
            pacman_pos.x = pac_old_x - vx * dt * 2
            pacman_pos.y = pac_old_y - vy * dt * 2
            # pacman_pos.x = screen.get_width() / 18
            # pacman_pos.y = screen.get_height() / 18
            vx = 0
            vy = 0

    if pacman_pos.x <39:
        pacman_pos.x = 39
    if pacman_pos.x > 859:
        pacman_pos.x = 859
    if pacman_pos.y <39:
        pacman_pos.y = 39
    if pacman_pos.y > 859:
        pacman_pos.y = 859
    if count < 15 :
        screen.blit(pacmanimage, pacman_pos)
    else:
        screen.blit(pacmanimage2, pacman_pos)
        

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()