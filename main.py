import sys
import pygame

pygame.init()

screenHeight = 700
screenWidth = 500
clock = pygame.time.Clock()

backgroundColor = "#7692FF"  # TODO: Add a background image instead
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Too Much Traffic!")


# Loading Start and Stop buttons
# Start Button
startButtonSurface = pygame.image.load(
    "images/UI/startButton.png").convert_alpha()
startButtonSurface = pygame.transform.scale2x(startButtonSurface)
startButtonRect = startButtonSurface.get_rect(
    center=(screenWidth // 2, 450))

# Exit Button
exitButtonSurface = pygame.image.load(
    "images/UI/exitButton.png").convert_alpha()
exitButtonSurface = pygame.transform.scale2x(exitButtonSurface)
exitButtonRect = exitButtonSurface.get_rect(center=(screenWidth // 2, 560))

# Loading the background
backgroundImageSurface = pygame.image.load(
    "images/backgroundImage.png").convert_alpha()
backgroundImageRect = backgroundImageSurface.get_rect(
    center=(screenWidth // 2, screenHeight // 2))

# Loading the logo
logoSurface = pygame.image.load(
    "images/tooMuchTrafficLogo.png").convert_alpha()
logoRectangle = logoSurface.get_rect(center=(screenWidth // 2, 200))

# Background music
bgMusic = pygame.mixer.Sound("sounds/backgroundMusic.mp3")
bgMusic.set_volume(0.1)
bgMusic.play(-1)

gameState = 0

# GAME LOOP
while True:
    screen.fill(backgroundColor)

    # Controls
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # UPDATE

    # DRAW
    # Main Menu
    if gameState == 0:
        screen.blit(backgroundImageSurface, backgroundImageRect)
        screen.blit(logoSurface, logoRectangle)
        screen.blit(startButtonSurface, startButtonRect)
        screen.blit(exitButtonSurface, exitButtonRect)

    pygame.display.update()
    clock.tick(60)
