from constants import ASTEROIDS_SPEEDS, ASTEROIDS_SIZES, SCREEN_HEIGHT, SCREEN_WIDTH
import pygame
import math

class Asteroid:
    def __init__(self, position, speed, direction, size):
        self.position = position
        self.direction = direction
        self.size = ASTEROIDS_SIZES[size] if size < len(ASTEROIDS_SIZES) and size > 0 else ASTEROIDS_SIZES[-1]
        self.speed = ASTEROIDS_SPEEDS[size]
        self.vertices = []


    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.size)

    def move(self):
        posx = self.position[0] + self.speed * math.cos(self.direction)
        if posx > SCREEN_WIDTH:
            posx = 0
        if posx < 0:
            posx = SCREEN_WIDTH
        posy = self.position[1] + self.speed * math.sin(self.direction)

        if posy > SCREEN_HEIGHT:
            posy = 0

        if posy < 0:
            posy = SCREEN_HEIGHT

        self.position = (posx, posy)
