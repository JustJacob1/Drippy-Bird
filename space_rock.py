import pygame
import random

class Asteroid:
    def __init__(self, image, screen_width, screen_height):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, screen_width - self.rect.width)
        self.rect.y = random.randint(-200, -50)
        self.speed = random.randint(2,6)
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def move(self):
        self.rect.y += self.speed

       # if self.rect.top > 800:  
        #    self.rect.x = random.randint(0, 1500 - self.rect.width)
