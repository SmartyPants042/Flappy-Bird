from Birds import Bird
from Pipes import Pipes
import Borders
import config as cfg
import time
import neat
import os
from Utility import collision_detection

import pygame
pygame.init()

def neat_play(genomes, config):

    # pipes
    pipes = [Pipes()]

    # AGLORITHM SETUP
    networks = []
    birds = []
    genes = []
    for genome_id, genome in genomes:
        genome.fitness = 0
        network = neat.nn.FeedForwardNetwork.create(genome, config)
        networks.append(network)
        birds.append(Bird())
        genes.append(genome)

    # GAME LOOP
    running = True
    while running and len(birds):

        # Handling exit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            # if event.type == pygame.KEYDOWN:
            #     if event.key == pygame.K_SPACE:
            #         bird.jump()

        
        # UPDATING OBJECTS        
        ## Jumping Birds
        ### feature `1`: next pipe's index
        i = 0
        while pipes[i].left < birds[0].x:
            i += 1
        send_pipe_index = i
        ### feature `2`: bird's y pos
        
        birds_alive = []
        for i, bird in enumerate(birds):
            genes[i].fitness += 0.01 # you get 0.01 point for staying alive
            birds_alive.append(bird.move())

            predictions = networks[i].activate(
                (
                    bird.x,
                    bird.y,
                    pipes[send_pipe_index].left, 
                    bird.y - pipes[send_pipe_index].bottom_pipe_top, 
                    bird.y - pipes[send_pipe_index].top_pipe_height,
                    bird.y - pipes[send_pipe_index].bottom_pipe_height 
            )
            )
            if predictions[0] > 0.5:
                bird.jump()

        
        # pipes: destruction
        for pipe in pipes:
            if not pipe.move():
                del pipe
        # pipes: generation        
        if pipes[-1].left <= cfg.SCREEN_WIDTH - cfg.PIPE_WIDTH - cfg.PIPE_SPACER:
            pipes.append(Pipes())


        # COLLISION DETECTION
        for i, bird in enumerate(birds):
            for pipe in pipes:
                if collision_detection(bird, pipe):
                    birds_alive[i] = False
                    break
            
        # DRAWING OBJECTS
        # fill screen with background
        cfg.SCREEN.fill(cfg.BLUE)
        
        # pipes
        for pipe in pipes:
            pipe.draw()

        # birds
        chinese_maal = []
        for i, bird in enumerate(birds):        
            if birds_alive[i]:
                bird.draw()
            else:
                bird.color = cfg.RED
                bird.draw()
                chinese_maal.append(bird)
                
        for bird in chinese_maal:
            networks.pop(birds.index(bird))
            genes.pop(birds.index(bird))
            birds.pop(birds.index(bird))

        # UPDATE SCREEN
        Borders.draw()
        pygame.display.update()

def algo(config_file):
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation,
                         config_file)

    pop = neat.Population(config)

    pop.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    pop.add_reporter(stats)

    # runs for inf generations
    winner = pop.run(neat_play, None)

    # show final stats
    print('\nBest genome:\n{!s}'.format(winner))

if __name__ == '__main__':
    local = os.path.dirname(__file__)
    config_file = os.path.join(local, 'Algorithm/config-feedforward.txt')
    algo(config_file)