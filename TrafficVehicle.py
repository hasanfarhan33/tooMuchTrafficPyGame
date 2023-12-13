import pygame 
import random

class TrafficVehicle:
    def __init__(self, x, y, imageDirectory):
        self.trafficVehicleImage = pygame.image.load(imageDirectory).convert_alpha()
        self.trafficVehicleImageRect = self.trafficVehicleImage.get_rect(center = (x, y))
        self.deltaY = random.randint(1, 4)
        self.passed = False 
        
    def draw(self, screen):
        screen.blit(self.trafficVehicleImage, self.trafficVehicleImageRect)
    
    def update(self, screen):
        self.trafficVehicleImageRect.centery = round(self.trafficVehicleImageRect.centery + self.deltaY)