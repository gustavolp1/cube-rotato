import numpy as np
import pygame
from math import *

# https://www.youtube.com/watch?v=qw0oY6Ld-L0&ab_channel=Pythonista_

def connect_points(i,j,points):
    pygame.draw.line(screen, rainbow_color(color), ((points[i][0]), (points[i][1])), ((points[j][0]), (points[j][1])))
    return

color = 0
def rainbow_color(value):
    step = (value // 256) % 6
    pos = value % 256

    if step == 0:
        return (255, pos, 0)
    if step == 1:
        return (255-pos, 255, 0)
    if step == 2:
        return (0, 255, pos)
    if step == 3:
        return (0, 255-pos, 255)
    if step == 4:
        return (pos, 0, 255)
    if step == 5:
        return (255, 0, 255-pos)

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
angle = 1
circle_pos = [width/2, height/2]

points = []
for x in (1, -1):
    for y in (1, -1):
        for z in (1, -1):
            points.append(np.array([x, y, z]))

print(points)

projection_matrix = np.array([
    [1,0,0],
    [0,1,0],
    [0,0,0]
    ])

projected_points = [[n, n] for n in range(len(points))]

clock = pygame.time.Clock()

# Base PyGame loop
while True:

    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()

    rotate_x = np.array([
        [1, 0, 0],
        [0, cos(angle), -sin(angle)],
        [0, sin(angle), cos(angle)]
    ])

    rotate_y = np.array([
        [cos(angle), 0, sin(angle)],
        [0, 1, 0],
        [-sin(angle), 0, cos(angle)]
    ])

    rotate_z = np.array([
        [cos(angle), -sin(angle), 0],
        [sin(angle), cos(angle), 0],
        [0, 0, 1]
    ])

    angle += 0.01

    screen.fill(BLACK)
    
    i = 0
    for point in points:

        rotated2d = np.dot(rotate_z, point.reshape((3,1)))
        rotated2d = np.dot(rotate_y, rotated2d)
        rotated2d = np.dot(rotate_x, rotated2d)

        projected2d = np.dot(projection_matrix, rotated2d)

        x = int(projected2d[0][0] * scale) + circle_pos[0]
        y = int(projected2d[1][0] * scale) + circle_pos[1]

        projected_points[i] = [x,y]
        pygame.draw.circle(screen, rainbow_color(color), (x, y), 5)
        i += 1

    color = (color + 1) % (256 * 6)
    
    connect_points(0, 1, projected_points)
    connect_points(1, 3, projected_points)
    connect_points(3, 2, projected_points)
    connect_points(2, 0, projected_points)

    connect_points(4, 5, projected_points)
    connect_points(5, 7, projected_points)
    connect_points(7, 6, projected_points)
    connect_points(6, 4, projected_points)

    connect_points(0, 4, projected_points)
    connect_points(1, 5, projected_points)
    connect_points(2, 6, projected_points)
    connect_points(3, 7, projected_points)

    pygame.display.update()