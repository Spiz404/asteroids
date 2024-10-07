from constants import ASTEROIDS_SPEEDS, ASTEROIDS_SIZES, SCREEN_HEIGHT, SCREEN_WIDTH
import pygame
import math

class Asteroid:
    def __init__(self, position, speed, direction, size):
        self.position = position
        self.direction = direction
        self.size = ASTEROIDS_SIZES[size] if size < len(ASTEROIDS_SIZES) and size > 0 else ASTEROIDS_SIZES[-1]
        self.speed = ASTEROIDS_SPEEDS[size] if size < len(ASTEROIDS_SPEEDS) and size > 0 else ASTEROIDS_SPEEDS[-1]
        self.vertices = []


    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.size)

    def move(self):
        posx = self.position[0] + self.speed * math.cos(self.direction)
        if posx > SCREEN_WIDTH + self.size:
            posx = - self.size

        if posx < - self.size:
            posx = SCREEN_WIDTH + self.size
        posy = self.position[1] + self.speed * math.sin(self.direction)

        if posy > SCREEN_HEIGHT + self.size:
            posy = -self.size

        if posy < - self.size:
            posy = SCREEN_HEIGHT + self.size

        self.position = (posx, posy)
