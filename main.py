import pygame
import math
from starship import Starship
from constants import DEFAULT_SPEED, SCREEN_WIDTH, SCREEN_HEIGHT

screen = pygame.display.set_mode((SCREEN_WIDTH , SCREEN_HEIGHT))

speed = DEFAULT_SPEED

starship = Starship(0.5, (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
moving = False
while True:
    screen.fill((0, 0, 0))
    if speed < 0.1:
        moving = False
        speed = DEFAULT_SPEED

    starship.draw(screen)
    pygame.draw.circle(screen, (255, 255, 255), starship.centroid, 1)
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
            pygame.quit()
            exit()

    if pygame.key.get_pressed()[pygame.K_UP]:
        #current_rotation = starship.direction
        moving = True
        #starship.move(starship.direction, speed)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        starship.rotate(-0.004)
    if keys[pygame.K_RIGHT]:
        starship.rotate(0.004)

    if keys[pygame.K_UP]:
        starship.move(0.5)
    pygame.display.update()
    pygame.display.flip()
