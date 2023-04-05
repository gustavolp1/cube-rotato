import numpy as np
import pygame
from math import *

# Connects the points of the cube
def connect_points(i,j,points):
    pygame.draw.line(screen, rainbow_color(color), ((points[i][0]), (points[i][1])), ((points[j][0]), (points[j][1])), 5)
    return

# Changes the cube's color every frame, creating a rainbow effect
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

# Background color
BLACK = (0,0,0)

# Aspect Ratio: 16:9
width = 1280
height = 720

# Screen Setup
pygame.display.set_caption('Cube Rotato')
screen = pygame.display.set_mode((width, height))

# Cube angle and scale variables setup
scale = 100
anglex = 0
angley = 0
anglez = 0

# Set up the points
points = []
for x in (1, -1):
    for y in (1, -1):
        for z in (1, -1):
            points.append([x, y, z, 1])
points = np.array(points) # This gets us a matrix for the points we will use

# Focal distance initial value
d = 300

# Variables for rotation and focal distance adjustment inputs
d_increase = False
d_decrease = False
anglex_r = ''
angley_r = ''
anglez_r = ''
auto = False

# Setting up the PyGame clock for stable framerate
clock = pygame.time.Clock()
pygame.font.init()

# Font configuration and rendering
my_font = pygame.font.SysFont('impact', 36)
cube_rotato_text = my_font.render('CUBE ROTATO', True, (255, 255, 255))
bottom_text = my_font.render('BOTTOM TEXT', True, (255, 255, 255))

# Base PyGame loop
while True:

    clock.tick(60) # 60fps

    # Inputs
    for event in pygame.event.get():

        # Esc to quit
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()

            # Focal distance keyboard inputs
            if event.key == pygame.K_i:
                d_increase = True
            if event.key == pygame.K_o:
                d_decrease = True

            # Rotation keyboard inputs
            if event.key == pygame.K_w:
                anglex_r = 'clock'
            if event.key == pygame.K_s:
                anglex_r = 'counter'
            if event.key == pygame.K_d:
                angley_r = 'clock'
            if event.key == pygame.K_a:
                angley_r = 'counter'
            if event.key == pygame.K_e:
                anglez_r = 'clock'
            if event.key == pygame.K_q:
                anglez_r = 'counter'

            # Rotation on all axis keyboard inputs
            if event.key == pygame.K_SPACE:
                auto = True

        if event.type == pygame.KEYUP:

            # Focal distance keyboard inputs
            if event.key == pygame.K_i:
                d_increase = False
            if event.key == pygame.K_o:
                d_decrease = False

            # Rotation keyboard inputs
            if event.key == pygame.K_w:
                anglex_r = ''
            if event.key == pygame.K_s:
                anglex_r = ''
            if event.key == pygame.K_d:
                angley_r = ''
            if event.key == pygame.K_a:
                angley_r = ''
            if event.key == pygame.K_e:
                anglez_r = ''
            if event.key == pygame.K_q:
                anglez_r = ''

            # Rotation on all axis keyboard inputs
            if event.key == pygame.K_SPACE:
                auto = False

        # Focal distance mousewheel inputs
        if event.type == pygame.MOUSEWHEEL:
            if event.y > 0:
                d += 40
            elif event.y < 0:
                d -= 40

    # Modifies focal distance if inputs are detected
    if d_increase:
        d += 5
    if d_decrease and d > 0:
        d -= 5
    if d<=0:
        d = 5

    # Cube X rotation if inputs are detected
    if anglex_r == 'clock' or auto:
        anglex += 0.02 
    if anglex_r == 'counter':
        anglex -= 0.02 

    # Cube Y rotation if inputs are detected
    if angley_r == 'clock' or auto:
        angley += 0.02
    if angley_r == 'counter':
        angley -= 0.02

    # Cube Z rotation if inputs are detected
    if anglez_r == 'clock' or auto:
        anglez += 0.02
    if anglez_r == 'counter':
        anglez -= 0.02

    # Projection Matrix
    P = np.array([
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 0, -d],
        [0, 0, -1/d, 0],
        ])

    # X rotation matrix
    rotate_x = np.array([
        [1, 0, 0, 0],
        [0, cos(anglex), -sin(anglex), 0],
        [0, sin(anglex), cos(anglex), 0],
        [0, 0, 0, 1],
    ])

    # Y rotation matrix
    rotate_y = np.array([
        [cos(angley), 0, sin(angley), 0],
        [0, 1, 0, 0],
        [-sin(angley), 0, cos(angley), 0],
        [0, 0, 0, 1],
    ])

    # Z rotation matrix
    rotate_z = np.array([
        [cos(anglez), -sin(anglez), 0, 0],
        [sin(anglez), cos(anglez), 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1],
    ])

    # Draw a background and the text on screen
    screen.fill(BLACK)
    widthcenter = screen.get_rect().center[0]
    screen.blit(cube_rotato_text, cube_rotato_text.get_rect(center = (widthcenter, height*0.1)))
    screen.blit(bottom_text, bottom_text.get_rect(center = (widthcenter, height*0.9)))

    # Create main rotation matrix
    R = rotate_x@rotate_y@rotate_z

    # Z distance of the cube
    z_deslocate = 3

    # Tz matrix (adds depth)
    Tz = np.array(([1,0,0,0],[0,1,0,0],[0,0,1,z_deslocate],[0,0,0,1]))

    # Translation in x and y matrix (center the cube on screen)
    Txy = np.array([ [1,0,0, width/2], [0,1,0,height/2], [0,0,1,0], [0,0,0,1] ])

    # Final transformation matrix
    T = Txy@P@Tz@R

    # Multiply T and the transposed points matrix
    d_points = T@(points).T

    # Get each point's x and y values and draw them on screen
    p_points = []
    for point in d_points.T:
        x = point[0]/point[3]
        y = point[1]/point[3]
        p_points.append((x, y))
        pygame.draw.circle(screen, rainbow_color(color), (x, y), 5)

    # Color change for the rainbow effect
    color = (color + 1) % (256 * 6)
    
    # Create the lines that connect the vertices in the cube
    connect_points(0, 1, p_points)
    connect_points(1, 3, p_points)
    connect_points(3, 2, p_points)
    connect_points(2, 0, p_points)
    connect_points(4, 5, p_points)
    connect_points(5, 7, p_points)
    connect_points(7, 6, p_points)
    connect_points(6, 4, p_points)
    connect_points(0, 4, p_points)
    connect_points(1, 5, p_points)
    connect_points(2, 6, p_points)
    connect_points(3, 7, p_points)

    # Update screen
    pygame.display.update()