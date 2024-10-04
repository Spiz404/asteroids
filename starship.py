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
        pygame.draw.polygon(screen, STARSHIP_COLOR, self.vertices)

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

    def move(self, direction, speed):
        print("moving")
        print(self.vertices)
        vertices_outside = 0
        for i in range(3):
            x, y = self.vertices[i]
            x += speed * math.cos(direction)
            y += speed * math.sin(direction)
            if x > SCREEN_WIDTH or y > SCREEN_WIDTH or x < 0 or y < 0:
                vertices_outside += 1
            self.vertices[i] = (x, y)

        if vertices_outside == 3:
            if self.vertices[0][0] > SCREEN_WIDTH:
                self.vertices[0] = (0, self.vertices[0][1])
                self.vertices[1] = (0, self.vertices[1][1])
                self.vertices[2] = (0, self.vertices[2][1])
            if self.vertices[0][1] > SCREEN_HEIGHT:
                self.vertices[0] = (self.vertices[0][0], 0)
                self.vertices[1] = (self.vertices[1][0], 0)
                self.vertices[2] = (self.vertices[2][0], 0)
        print(self.vertices)
