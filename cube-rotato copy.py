import numpy as np
import pygame
from math import *

def connect_points(i,j,points):
    pygame.draw.line(screen, rainbow_color(color), ((points[i][0]), (points[i][1])), ((points[j][0]), (points[j][1])), 2)
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
#circle_pos = [width/2, height/2]
circle_pos = [0, 0]

# Set up the points
points = []
for x in (1, -1):
    for y in (1, -1):
        for z in (1, -1):
            points.append(np.array([x, y, z, 1]))
            
points = np.array([points]).T

# Create projection points array
projected_points = [[n, n] for n in range(len(points))]

# Projection Matrix
d = 1
projmatrix = np.array([
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 0, -d],
    [0, 0, -1/d, 0],
    ])
d_increase = False
d_decrease = False

clock = pygame.time.Clock()
pygame.font.init()
my_font = pygame.font.SysFont('comic sans', 30)

text_surface = my_font.render('cube rotato', True, (255, 255, 255))

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
            if event.key == pygame.K_w:
                d_increase = True
            if event.key == pygame.K_s:
                d_decrease = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                d_increase = False
            if event.key == pygame.K_s:
                d_decrease = False

    if d_increase:
        d += 0.02
    if d_decrease and d >= 0:
        d -= 0.02

    projmatrix = np.array([
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 0, -d],
        [0, 0, -1/d, 0],
        ])

    rotate_x = np.array([
        [1, 0, 0, 0],
        [0, cos(angle), -sin(angle), 0],
        [0, sin(angle), cos(angle), 0],
        [0, 0, 0, 1],
    ])

    rotate_y = np.array([
        [cos(angle), 0, sin(angle), 0],
        [0, 1, 0, 0],
        [-sin(angle), 0, cos(angle), 0],
        [0, 0, 0, 1],
    ])

    rotate_z = np.array([
        [cos(angle), -sin(angle), 0, 0],
        [sin(angle), cos(angle), 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1],
    ])

    angle += 0.01

    screen.fill(BLACK)
    screen.blit(text_surface, text_surface.get_rect(center = screen.get_rect().center))

    i = 0
    for point in points:

        rotated2d = np.dot(rotate_z, point.reshape((4,1)))
        rotated2d = np.dot(rotate_y, rotated2d)
        rotated2d = np.dot(rotate_x, rotated2d)

        #rotated2d = np.dot(np.array([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]), point.reshape((4,1)))

        projected2d = np.dot(projmatrix, rotated2d)

        projected2d[0] = projected2d[0]/projected2d[3]
        projected2d[1] = projected2d[1]/projected2d[3]

        projected2d = np.dot(np.array([ [1, 0, 0, width/2], [0, 1, 0, height/2], [0, 0, 1, 0], [0, 0, 0, 1] ]), projected2d)

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

    # connect_points(0, 7, projected_points)
    # connect_points(1, 6, projected_points)
    # connect_points(2, 5, projected_points)
    # connect_points(3, 4, projected_points)

    

    pygame.display.update()