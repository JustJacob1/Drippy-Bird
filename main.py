import pygame
import random
pygame.init()
screen = pygame.display.set_mode((400,600))
clock = pygame.time.Clock()

player = pygame.image.load('Photos/West.png').convert_alpha()
player = pygame.transform.smoothscale(player, [100,100])
player = player.subsurface(player.get_bounding_rect())
player_pos = pygame.Vector2(0,225)
y_axis = 0
backround = pygame.image.load
pipe = pygame.image.load("Pipe.png")
pipe_width = pipe.get_width()
pipe_height = pipe.get_height()

#Pipes
pipe_gap = 150
pipe_distance = 200
pipe_speed = 2
pipes = []
for i in range(3):
    x = 400 + pipe_distance * 1
    y_offset = random.randint(-150, 0)
    pipes.append({"x": x, "y_offset": y_offset})

is_running =  True
while is_running:
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
    for pipe_data in pipes:
        pipe_data["x"] -= pipe_speed

        if pipe_data["x"] <-pipe_width
            pipe_data['x'] = max(p["x"])
            pipe_data["y_offset"] = random.randint(-150,0)
        backround.blit([pipe,(pipe_data["x"], pipe_data"y_offset"])
        bottom_pipe = pygame.transform.flip(pipe,False,True)
        bottom_y = pipe_data["y_offset"] + pipe_height + pipe_gap
        backround.blit(bottom_pipe(pipe_data["x"], bottom_y))


    screen.fill("white")
    screen.blit(player, player_pos)
    pygame.display.flip()
    clock.tick(60)