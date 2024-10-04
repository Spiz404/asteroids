import pygame
import math
from constants import STARSHIP_SIZE, SCREEN_WIDTH, SCREEN_HEIGHT, STARSHIP_COLOR
from Shot import Shot

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
        outside_right = outside_left = outside_top = outside_down = 0

        for i in range(3):
            vx = x + self.size * math.cos(angle)
            vy = y + self.size * math.sin(angle)
            if vx > SCREEN_WIDTH: outside_right += 1
            if vx < 0: outside_left += 1
            if vy < 0: outside_top += 1
            if vy > SCREEN_HEIGHT: outside_down += 1
            vertices.append((vx, vy))
            angle += 2 * math.pi / 3

        if outside_right == 3: self.centroid = (0, self.centroid[1])
        if outside_left == 3: self.centroid = (SCREEN_WIDTH, self.centroid[1])
        if outside_top == 3: self.centroid = (self.centroid[0], SCREEN_HEIGHT)
        if outside_down == 3: self.centroid = (self.centroid[0], 0)

        self.vertices = vertices

    def rotate(self, rotation):
       self.rotation_angle += rotation
       self.update_vertices()

    def move(self, speed, rotation):
        updated_centroid =  (self.centroid[0] + speed * math.cos(rotation), self.centroid[1] +  speed * math.sin(rotation))
        self.centroid = updated_centroid
        self.update_vertices()

    # function that returns a new shot component
    def shot(self):
        return Shot(self.rotation_angle, self.centroid)
