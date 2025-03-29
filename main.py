import pygame
pygame.init()
screen = pygame.display.set_mode((400,600))
screen.fill("white")

is_running =  True
while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
            pygame.quit()

    pygame.display.flip()
