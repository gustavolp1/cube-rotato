import numpy as np
import pygame
import math

# Colors
BLACK = (0,0,0)
GREEN = (0,255,0)

# Aspect Ratio: 16:9
width = 1280
height = 720

# Screen Setup
pygame.display.set_caption('Cube Rotato')
screen = pygame.display.set_mode((width, height))

# Cube setup using NumPy

scale = 100
circle_pos = [width/2, height/2]

points = []
for x in (-1, 1):
    for y in (-1, 1):
        for z in (-1, 1):
            points.append(np.array([x, y, z]))

projection_matrix = np.array([ [1,0,0],[0,1,0],[0,0,0] ])

# Base PyGame loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()


    screen.fill(BLACK)
    
    for point in points:
        projected2d = np.dot(projection_matrix, point.reshape((3,1)))
        x = int(projected2d[0][0] * scale) + circle_pos[0]
        y = int(projected2d[1][0] * scale) + circle_pos[1]
        pygame.draw.circle(screen, GREEN, (x, y), 5)

    pygame.display.update()