import pygame
import random
class Pipe:
    def __init__(self, x):
        self.image = pygame.image.load("Photos/Pipe.png")
        self.image = pygame.transform.scale(self.image,[100, 100])
        self.collision = self.image.get_rect()
        self.movement = 5
        self.collision.y = random.randint(0,600)
        self.collision.x = x
        
        
    def update(self,screen):
        screen.blit(self.image, self.collision)