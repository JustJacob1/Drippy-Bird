import pygame
import random
from pipe import Pipe
pygame.init()
screen = pygame.display.set_mode((400,600))
clock = pygame.time.Clock()

player = pygame.image.load('Photos/West.png').convert_alpha()
player = pygame.transform.smoothscale(player, [100,100])
player = player.subsurface(player.get_bounding_rect())
player_pos = player.get_rect( topleft = [0,225])
y_axis = 0
backround = pygame.image.load("Photos/bg.png").convert_alpha()
backround = pygame.transform.scale(backround, [400,600])
backround = backround.get_rect()

green_pipe = Pipe(200)




is_running =  True
Font = pygame.font.SysFont("comicsansms", 30)
while is_running:
    pygame.display.set_caption("coool game")
    jump = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                jump = True

        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                jump = True
    

    y_axis += .25
    if jump:
        y_axis = -5

    player_pos.y += y_axis
    if not screen.get_rect().contains(player_pos):
        quit()


    screen.fill("white")
    screen.blit(player, player_pos)
    green_pipe.update(screen)
    text = Font.render(f"points {Pipe.points}", True, "Black")
    screen.blit(text,[0,0])
    pygame.display.flip()
    clock.tick(60)