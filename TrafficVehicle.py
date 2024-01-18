import pygame 
import random

class TrafficVehicle:
    def __init__(self, x, y):
        vehicleArray = ["images/Vehicles/truck.png", "images/Vehicles/redCar.png", "images/Vehicles/blueCar.png", "images/Vehicles/purpleCar.png"]
        selectedDirectory = random.choice(vehicleArray)
        self.trafficVehicleImage = pygame.image.load(selectedDirectory).convert_alpha()
        self.trafficVehicleImageRect = self.trafficVehicleImage.get_rect(center = (x, y))
        self.deltaY = 2
        
    def draw(self, screen):
        screen.blit(self.trafficVehicleImage, self.trafficVehicleImageRect)
    
    def update(self, screen):
        self.trafficVehicleImageRect.centery = round(self.trafficVehicleImageRect.centery + self.deltaY)
        