import sys
import pygame
import random

# Importing classes
from Car import Car
from TrafficVehicle import TrafficVehicle


pygame.init()

screenHeight = 700
screenWidth = 500
clock = pygame.time.Clock()


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
bgMusic.set_volume(0.05)
bgMusic.play(-1)

# VEHICLES
# Player Car
playerCar = Car(screen.get_width() // 2, screen.get_height() //
                2, 0, 0, "images/Vehicles/playerCar.png")

# TRAFFIC
trafficVehicles = ["images/Vehicles/truck.png", "images/Vehicles/redCar.png"]

def spawnTraffic(trafficArray):
    # Vehicle at random x but fixed y 
    selectedCar = random.choice(trafficArray)
    selectedCar = TrafficVehicle(random.randint(100, screenWidth - 50), -200, selectedCar)
    
    return selectedCar

# truck = Truck(100, 100, "images/Vehicles/truck.png")
# redCar = RedCar(200, 200, "images/Vehicles/redCar.png")

# trafficVehicles.append(truck)
# trafficVehicles.append(redCar)

# selectedCar = random.choice(trafficVehicles)
selectedCar = spawnTraffic(trafficVehicles)

gameState = 0

# GAME LOOP
while True:
    # screen.fill(backgroundColor)

    # Controls
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Clicking the mouse
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Clicking on the exit button
            if (exitButtonRect.collidepoint(event.pos)):
                bgMusic.stop()
                pygame.quit()
                sys.exit()
            # Start the game
            elif (startButtonRect.collidepoint(event.pos)):
                gameState = 1

        # Listening for controls while the game is running
        if gameState == 1:
            if event.type == pygame.KEYDOWN:
                # Move the car left
                if event.key == pygame.K_a:
                    # print("The car will move LEFT now")
                    playerCar.accelX = -0.2
                # Move the car right
                elif event.key == pygame.K_d:
                    # print("The car will move RIGHT now")
                    playerCar.accelX = 0.2
                elif event.key == pygame.K_w:
                    playerCar.accelY = -0.2
                elif event.key == pygame.K_s:
                    playerCar.accelY = 0.2
            elif event.type == pygame.KEYUP:
                if event.key in (pygame.K_a, pygame.K_d):
                    playerCar.accelX = 0
                elif event.key in (pygame.K_w, pygame.K_s):
                    playerCar.accelY = 0

    # UPDATE

    # DRAW
    # Main Menu
    if gameState == 0:
        screen.blit(backgroundImageSurface, backgroundImageRect)
        screen.blit(logoSurface, logoRectangle)
        screen.blit(startButtonSurface, startButtonRect)
        screen.blit(exitButtonSurface, exitButtonRect)

    # Gameplay
    elif gameState == 1:
        # TODO: ADD ROAD INSTEAD OF COLOR
        screen.fill((40, 40, 40))
        # ADDING THE CAR TO THE SCREEN
        playerCar.draw(screen)
        
        selectedCar.draw(screen)

        # print(playerCar.deltaX)
        # print(playerCar.accelX)

        playerCar.update(screen)
        selectedCar.update(screen)

    pygame.display.update()
    clock.tick(60)
    