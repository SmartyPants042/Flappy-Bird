from Birds import Bird
from Pipes import Pipes
import Borders
import config as cfg
import time

import pygame
pygame.init()

def collision_detection(bird, pipe):
    top_pipe = pygame.Rect(pipe.left, pipe.top_pipe_top, pipe.width, pipe.top_pipe_height)
    bottom_pipe = pygame.Rect(pipe.left, pipe.bottom_pipe_top, pipe.width, pipe.bottom_pipe_height)

    bird_box = pygame.Rect(
        bird.x,
        bird.y,
        cfg.BIRD_SIZE,
        cfg.BIRD_SIZE
        )
    # print(bird_box)

    if pygame.Rect.colliderect(top_pipe, bird_box)\
        or pygame.Rect.colliderect(bottom_pipe, bird_box):
        return True

    return False

# yey, birb!
bird = Bird()

# pipes
pipes = []
pipe = Pipes()
pipes.append(pipe)

running = True
while running:

    # Handling exit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird.jump()

    # UPDATING OBJECTS        
    # bird
    bird_alive =  bird.move()
    
    # pipes: destruction
    for pipe in pipes:
        if not pipe.move():
            del pipe
    
    # pipes: generation        
    if pipes[-1].left <= cfg.SCREEN_WIDTH - cfg.PIPE_WIDTH - cfg.PIPE_SPACER:
        pipes.append(Pipes())


    # COLLISION DETECTION
    for pipe in pipes:
        if collision_detection(bird, pipe):
            bird_alive = False
            break
    
    # DRAWING OBJECTS
    # fill screen with background
    cfg.SCREEN.fill(cfg.BLUE)
    
    # pipes
    for pipe in pipes:
        pipe.draw()
    
    # bird
    if bird_alive:
        bird.draw()
    else:
        bird.color = cfg.RED
        bird.draw()
        del bird
        running = False

    # UPDATE SCREEN
    Borders.draw()
    pygame.display.update()

    if not running:
        time.sleep(cfg.BIRD_DEATH_TIME)
