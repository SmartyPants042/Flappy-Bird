import pygame
import config as cfg

def draw():
    pygame.draw.rect(cfg.SCREEN, cfg.DARK_BLUE, 
        (0, cfg.SCREEN_HEIGHT-cfg.GROUND_HEIGHT, cfg.SCREEN_WIDTH, cfg.GROUND_HEIGHT)
    )

    pygame.draw.rect(cfg.SCREEN, cfg.LIGHT_BLUE, 
        (0, 0, cfg.SCREEN_WIDTH, cfg.SKY_HEIGHT)
    )