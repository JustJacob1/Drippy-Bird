import pygame
import random
class Pipe:
    def __init__(self, x):
        self.image = pygame.image.load("Photos/Pipe.png")
        self.image = pygame.transform.scale(self.image,[300, 500])
        self.image_clone = pygame.transform.flip(self.image,False,True)
        self.collision_2 = self.image_clone.get_rect()
        self.collision = self.image.get_rect()
        self.movement = 5
        self.collision.y = random.randint(175,450)
        self.collision.x = x
        self.collision_2.x = self.collision.x
        self.collision_2.y = self.collision.y - 600
        
        
    def update(self,screen):
        # these two lines draw the pipes on the screen
        screen.blit(self.image, self.collision)
        screen.blit(self.image_clone, self.collision_2)
        
        # Teleports the pipe back to the right side of the screen to make it look like a new pipe has entered the view of the screen
        if self.collision.x <= -185:
            # sets the x back to 700 to the right side of the screen
            self.collision.x = 700 
            # sets the y at a random location
            self.collision.y = random.randint(175,450)
            
            self.collision_2.x = 700
            self.collision_2.y = self.collision.y - 600
        
            
        # moves the x by movement value  
        self.collision.x -= self.movement
        self.collision_2.x -= self.movement
        