import pygame
import random
class Pipe:
    def __init__(self, x):
        self.image = pygame.image.load("Photos/Pipe.png")
        self.image = pygame.transform.scale(self.image,[300, 500])
        self.collision = self.image.get_rect()
        self.movement = 5
        self.collision.y = random.randint(175,450)
        self.collision.x = x
        
        
    def update(self,screen):
        screen.blit(self.image, self.collision)
        if self.collision.x <= -185:
            self.collision.x = 700
            self.collision.y = random.randint(175,450)
        self.collision.x -= self.movement
        