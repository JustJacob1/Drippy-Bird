import pygame
import random

class Asteroid:
    def __init__(self, image, screen_width, screen_height):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0 + self.rect.width, screen_width - self.rect.width)  # This makes sure that when the asteroid appears somewhere on the screen that is fully visible
        self.rect.y = random.randint(0 + self.rect.width, screen_height - self.rect.height)
        self.speed = random.randint(2,4)
        direction = pygame.Vector2(screen_width / 2 - self.rect.centerx, screen_height / 2 - self.rect.centery).normalize()
        self.velocity = direction * self.speed
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def move(self):
        self.rect.y += self.velocity.y
        self.rect.x += self.velocity.x

       # if self.rect.top > 800:  
        #    self.rect.x = random.randint(0, 1500 - self.rect.width)
