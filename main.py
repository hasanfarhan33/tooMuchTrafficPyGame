import sys
import pygame

pygame.init()

screenHeight = 700
screenWidth = 500
clock = pygame.time.Clock()

backgroundColor = "#7692FF"
screen = pygame.display.set_mode((screenWidth, screenHeight))

# GAME LOOP
while True:
    screen.fill(backgroundColor)

    # Controls
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update

    # Draw

    pygame.display.update()
    clock.tick(60)
