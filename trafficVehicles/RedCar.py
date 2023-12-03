import pygame


class RedCar:
    def __init__(self, redCarX, redCarY, redCarImageDirectory):
        self.redCarImage = pygame.image.load(
            redCarImageDirectory).convert_alpha()
        self.redCarImageRect = self.redCarImage.get_rect(
            center=(redCarX, redCarY))
        self.deltaY = -1
        self.passed = False

    def draw(self, screen):
        screen.blit(self.redCarImage, self.redCarImageRect)

    def update(self):
        pass
