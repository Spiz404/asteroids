import pygame
import math
from constants import STARSHIP_SIZE, SCREEN_WIDTH, SCREEN_HEIGHT, STARSHIP_COLOR

class Starship:
    def __init__(self, rotation_angle, centroid):
        self.size = STARSHIP_SIZE
        self.centroid = centroid
        self.rotation_angle = -math.pi / 2
        x, y = self.centroid
        self.vertices = []
        self.update_vertices()

    def draw(self, screen):
        pygame.draw.polygon(screen, STARSHIP_COLOR, self.vertices, 1)

    def update_vertices(self):
        x, y = self.centroid
        angle = self.rotation_angle
        vertices = []
        for i in range(3):
            vx = x + self.size * math.cos(angle)
            vy = y + self.size * math.sin(angle)
            vertices.append((vx, vy))
            angle += 2 * math.pi / 3
        self.vertices = vertices

    def rotate(self, rotation):
       self.rotation_angle += rotation
       self.update_vertices()

    def move(self, speed, rotation):
        updated_centroid =  (self.centroid[0] + speed * math.cos(rotation), self.centroid[1] +  speed * math.sin(rotation))
        self.centroid = updated_centroid
        self.update_vertices()
