import math
import pygame
from constants import SHOT_SPEED, SCREEN_HEIGHT, SCREEN_WIDTH, SHOT_SIZE, SHOT_COLOR
class Shot:
    def __init__(self, direction, position):
        self.direction = direction
        self.position  = position

    def update_position(self):
        x, y = self.position
        x += math.cos(self.direction) * SHOT_SPEED
        y += math.sin(self.direction) * SHOT_SPEED
        if x > SCREEN_WIDTH: x = 0
        if x < 0: x = SCREEN_WIDTH
        if y < 0: y = SCREEN_HEIGHT
        if y > SCREEN_HEIGHT: y = 0
        self.position = (x, y)

    def show(self, screen):
        pygame.draw.circle(screen, SHOT_COLOR, self.position, SHOT_SIZE, 0)

    def split(self):
        pass
