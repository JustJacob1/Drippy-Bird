import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1800, 1100))
clock = pygame.time.Clock()
running = True



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
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("gray15")
    pygame.draw.circle(screen, "white", player, 15)
    pygame.draw.line(screen, "white", player, player+pygame.Vector2(20, 0).rotate(Angle))
    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()