import pygame
import math
from starship import Starship
from constants import DEFAULT_SPEED, SCREEN_WIDTH, SCREEN_HEIGHT, ROTATION_SPEED, DAMPING, SHOT_LIFE

screen = pygame.display.set_mode((SCREEN_WIDTH , SCREEN_HEIGHT))

speed = DEFAULT_SPEED
game_started = False
starship = Starship(0.5, (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
moving = False
rotation = starship.rotation_angle
starship_shots = []

while True:

    screen.fill((0, 0, 0))
    for i, [shot, time] in enumerate(starship_shots):
        if time > SHOT_LIFE:
            starship_shots.remove([shot, time])
            continue

        starship_shots[i] = [shot, time + 1]
        shot.update_position()
        shot.show(screen)

    starship.draw(screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                starship_shots.append([starship.shot(), 0])

    if pygame.key.get_pressed()[pygame.K_UP]:
        if not game_started: game_started = True
        moving = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        starship.rotate(ROTATION_SPEED * -1)
    if keys[pygame.K_RIGHT]:
        starship.rotate(ROTATION_SPEED)

    if keys[pygame.K_UP]:
        speed = DEFAULT_SPEED
        rotation = starship.rotation_angle
        starship.move(speed, rotation)
    else:
        if game_started:
            speed -= speed * 0.001
            starship.move(speed, rotation)

    pygame.display.update()
    pygame.display.flip()
