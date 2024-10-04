import math
import pygame
from constants import SHOT_SPEED
class Shot:
    def __init__(self, direction, position):
        self.direction = direction
        self.position  = position

    def update_position(self):
        x, y = self.position
        x += math.cos(self.direction) * SHOT_SPEED
        y += math.sin(self.direction) * SHOT_SPEED
        self.position = (x, y)

    def show(self, screen):
        pygame.draw.circle(screen, (255,255,255), self.position, 1)
