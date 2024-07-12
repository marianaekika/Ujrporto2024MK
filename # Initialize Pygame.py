# Example file showing a circle moving on screen
import pygame

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the title and icon
pygame.display.set_caption("Pac-Man")
icon = pygame.image.load("pacman_icon.png")
pygame.display.set_icon(icon)

# Load the player and dot images
player_image = pygame.image.load("pacman.png")
dot_image = pygame.image.load("dot.png")

# Set up the player and dot positions
player_x = 300
player_y = 300
dot_x = 100
dot_y = 100

# Set up the game variables
running = True
score = 0

# Main game loop
while running:
    # Check for player input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x -= 5
            elif event.key == pygame.K_RIGHT:
                player_x += 5
            elif event.key == pygame.K_UP:
                player_y -= 5
            elif event.key == pygame.K_DOWN:
                player_y += 5
    
    # Update game state
    if abs(player_x - dot_x) < 20 and abs(player_y - dot_y) < 20:
        score += 1
        dot_x = -100
        dot_y = -100
    
    # Draw game
    screen.fill((0, 0, 0))
    screen.blit(player_image, (player_x, player_y))
    screen.blit(dot_image, (dot_x, dot_y))
    font = pygame.font.Font("freesansbold.ttf", 32)
    text = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(text, (10, 10))
    pygame.display.flip()

# Quit Pygame
pygame.quit()