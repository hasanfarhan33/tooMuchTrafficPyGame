import pygame


class Car:

    def __init__(self, carX, carY, deltaX, deltaY, imageDirectory):
        super().__init__()
        self.carX = carX
        self.carY = carY
        self.maxXSpeed = 5
        self.maxYSpeed = 8
        self.deltaX = deltaX
        self.deltaY = deltaY
        self.carImage = pygame.image.load(imageDirectory).convert_alpha()
        self.carImage = pygame.transform.rotozoom(self.carImage, 0, 0.95)
        self.carImageRect = self.carImage.get_rect(
            center=(self.carX, self.carY))
        self.moveLeft = False
        self.moveRight = False
        self.accelX = 0
        self.accelY = 0

    def draw(self, screen):
        screen.blit(self.carImage, self.carImageRect)

    # TODO: Implement this function
    def update(self, screen):

        if self.carImageRect.left < 0:
            self.carImageRect.left = 0
        elif self.carImageRect.right > screen.get_width():
            self.carImageRect.right = screen.get_width()

        if self.carImageRect.bottom > screen.get_height():
            self.carImageRect.bottom = screen.get_height()
        elif self.carImageRect.top < 0:
            self.carImageRect.top = 0

        # TURNING
        self.deltaX += self.accelX  # Accelerate
        if abs(self.deltaX) >= self.maxXSpeed:
            self.deltaX = self.deltaX / abs(self.deltaX) * self.maxXSpeed

        # SPEED UP AND DOWN
        self.deltaY += self.accelY
        if abs(self.deltaY) >= self.maxYSpeed:
            self.deltaY = self.deltaY / abs(self.deltaY) * self.maxYSpeed

        # Deceleration
        if self.accelX == 0:
            self.deltaX *= 0.91
        if self.accelY == 0:
            self.deltaY *= 0.91

        # Updating
        self.carImageRect.centerx = round(
            self.carImageRect.centerx + self.deltaX)
        self.carImageRect.centery = round(
            self.carImageRect.centery + self.deltaY)
