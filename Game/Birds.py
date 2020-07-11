import pygame
import config as cfg
import time
import random

class Bird():
    def __init__(self):
        # Design
        self.color = cfg.BIRD_COLOR
        
        # Positions
        self.x = cfg.BIRD_X_INIT
        self.y = random.randint( \
            cfg.BIRD_SIZE + cfg.SKY_HEIGHT + cfg.BIRD_SPACER_INIT, \
            cfg.SCREEN_HEIGHT - cfg.GROUND_HEIGHT - cfg.BIRD_SIZE - cfg.BIRD_SPACER_INIT)
        
        # Time
        self.t = 0
        
        # Velocities
        self.v = cfg.BIRD_INITIAL_VELOCITY
        self.tv = cfg.BIRD_TERMINAL_VELOCITY

        # Accleration
        self.g = cfg.GRAVITY

    def jump(self):
        self.t = 1
        self.v = cfg.BIRD_UPWARD_VELOCITY
        self.y += cfg.BIRD_JUMP_HEIGHT

    def move(self):
        """
        returns False if bird is to be killed
        else True
        """
        # time
        self.t += 1

        # velocity
        self.v = self.v + self.g * self.t
        if self.v >= self.tv:
            self.v = self.tv

        # displacement
        self.y = self.y + self.v * self.t + 0.5 * self.g * self.t**2

        # # Top Stop
        # if self.y <= cfg.BIRD_SIZE + cfg.SKY_HEIGHT:
        #     self.y = cfg.BIRD_SIZE + cfg.SKY_HEIGHT

        # Top also death
        if self.y <= cfg.BIRD_SIZE + cfg.SKY_HEIGHT:
            self.y = cfg.BIRD_SIZE + cfg.SKY_HEIGHT
            return False
            
        # Bottom DEATH
        if self.y >= (cfg.SCREEN_HEIGHT - cfg.GROUND_HEIGHT - cfg.BIRD_SIZE):
            self.y = cfg.SCREEN_HEIGHT - cfg.GROUND_HEIGHT - cfg.BIRD_SIZE
            return False

        # Birb still alive!
        return True

    def draw(self):
        pygame.draw.circle(cfg.SCREEN, self.color, (int(self.x), int(self.y)), cfg.BIRD_SIZE)