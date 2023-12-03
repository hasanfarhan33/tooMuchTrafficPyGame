import pygame
import random


class Truck:
    def __init__(self, truckX, truckY, truckImageDirectory):
        super().__init__()
        self.truckImage = pygame.image.load(
            truckImageDirectory).convert_alpha()
        self.truckImage = pygame.transform.rotozoom(self.truckImage, 0, 1.35)
        self.truckImageRect = self.truckImage.get_rect(center=(truckX, truckY))
        self.deltaY = -3
        self.passed = False

    def draw(self, screen):
        screen.blit(self.truckImage, self.truckImageRect)

    def update(self, screen):
        pass
