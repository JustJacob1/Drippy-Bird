import pygame
from space_rock import Asteroid

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1500, 800))
clock = pygame.time.Clock()
running = True

backround_image = pygame.image.load("Photos/bg_space.jpg").convert_alpha()
backround_image = pygame.transform.scale(backround_image, [1500,800])
backround_rect = backround_image.get_rect()
Astroid = pygame.image.load("Photos/Astroid.png").convert_alpha()
Astroid = pygame.transform.scale(Astroid, [80,80])

astroid_list = []
for _ in range(10):
    asteroid = Asteroid(Astroid, 1500, 800)
    astroid_list.append(asteroid)








player = pygame.Vector2(1800, 1100)/2
Angle = 220
speed = pygame.Vector2()
while running:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
    Angle += keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]
    speed.x += keys[pygame.K_UP] - keys[pygame.K_DOWN]
    speed*= 0.7
    player += speed.rotate(Angle)
    screen.blit(backround_image, backround_rect)
    screen.blit(Astroid, backround_rect)
    pygame.draw.circle(screen, "white", player, 15)
    pygame.draw.line(screen, "white", player, player+pygame.Vector2(20, 0).rotate(Angle))
    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()