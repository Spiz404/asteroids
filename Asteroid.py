from constants import ASTEROIDS_SIZES, SCREEN_HEIGHT, SCREEN_WIDTH
import pygame
import math

class Asteroid:
    def __init__(self, position, speed,direction, size):
        self.position = position
        self.speed = speed
        self.direction = direction
        self.size = ASTEROIDS_SIZES[size] if size < len(ASTEROIDS_SIZES) and size > 0 else ASTEROIDS_SIZES[-1]
        self.vertices = []


    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.size, 1)

    def move(self):
       self.position = (self.position[0] + self.speed * math.cos(self.direction), self.position[1] + self.speed * math.sin(self.direction))
