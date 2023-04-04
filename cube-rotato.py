import numpy as np
import pygame
from math import *

def connect_points(i,j,points):
    pygame.draw.line(screen, rainbow_color(color), ((points[i][0]), (points[i][1])), ((points[j][0]), (points[j][1])), 5)
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
angle = 0
anglex = 0
angley = 0
anglez = 0
#circle_pos = [width/2, height/2]
circle_pos = [0, 0]

# Set up the points
points = []
for x in (1, -1):
    for y in (1, -1):
        for z in (1, -1):
            points.append([x, y, z, 1])

points = np.array(points)

# Create projection points array
projected_points = [[n, n] for n in range(len(points))]
#print(projected_points)
# Projection Matrix

d = 300
d_increase = False
d_decrease = False

anglex_r = ''
angley_r = ''
anglez_r = ''

auto = False

clock = pygame.time.Clock()
pygame.font.init()
my_font = pygame.font.SysFont('impact', 36)

cube_rotato_text = my_font.render('CUBE ROTATO', True, (255, 255, 255))
bottom_text = my_font.render('BOTTOM TEXT', True, (255, 255, 255))

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
            if event.key == pygame.K_i:
                d_increase = True
            if event.key == pygame.K_o:
                d_decrease = True

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

            if event.key == pygame.K_SPACE:
                auto = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_i:
                d_increase = False
            if event.key == pygame.K_o:
                d_decrease = False

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

            if event.key == pygame.K_SPACE:
                auto = False

        if event.type == pygame.MOUSEWHEEL:
            if event.y > 0:
                d += 40
            elif event.y < 0:
                d -= 40


    if d_increase:
        d += 5
    if d_decrease and d > 0:
        d -= 5
    if d<=0:
        d = 5

    if anglex_r == 'clock' or auto:
        anglex += 0.02 
    if anglex_r == 'counter':
        anglex -= 0.02 

    if angley_r == 'clock' or auto:
        angley += 0.02
    if angley_r == 'counter':
        angley -= 0.02

    if anglez_r == 'clock' or auto:
        anglez += 0.02
    if anglez_r == 'counter':
        anglez -= 0.02

    T = np.array([
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 0, -d],
        [0, 0, -1/d, 0],
        ])

    rotate_x = np.array([
        [1, 0, 0, 0],
        [0, cos(anglex), -sin(anglex), 0],
        [0, sin(anglex), cos(anglex), 0],
        [0, 0, 0, 1],
    ])

    rotate_y = np.array([
        [cos(angley), 0, sin(angley), 0],
        [0, 1, 0, 0],
        [-sin(angley), 0, cos(angley), 0],
        [0, 0, 0, 1],
    ])

    rotate_z = np.array([
        [cos(anglez), -sin(anglez), 0, 0],
        [sin(anglez), cos(anglez), 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1],
    ])

    angle += 0.01

    screen.fill(BLACK)
    widthcenter = screen.get_rect().center[0]
    screen.blit(cube_rotato_text, cube_rotato_text.get_rect(center = (widthcenter, height*0.1)))
    screen.blit(bottom_text, bottom_text.get_rect(center = (widthcenter, height*0.9)))

    R = rotate_x@rotate_y@rotate_z # Prepara Matriz de Rotacao.
    z_deslocate = 3 # distancia do cubo.
    Tz = np.array(([1,0,0,0],[0,1,0,0],[0,0,1,z_deslocate],[0,0,0,1])) # matriz que aplica uma transformacao em z, o que adiciona uma variacao de "profundidade".
    transl = np.array([ [1,0,0, width/2], [0,1,0,height/2], [0,0,1,0], [0,0,0,1] ]) # translacao para o meio da tela
    T = transl@T@Tz@R # preparando a matriz de transformacao;
    # primeiro multiplicamos a matriz R por Tz para ajustarmos a posicao do cubo de nosso ponto de referencia'
    # depois passamos para o mundo 2d e por ultimo aplicamos a translacao para colocar o cubo no centro da tela
    d_points = T@(points).T

    p_points = []
    for point in d_points.T:
        x = point[0]/point[3]
        y = point[1]/point[3]
        p_points.append((x, y))
        pygame.draw.circle(screen, rainbow_color(color), (x, y), 5)

    color = (color + 1) % (256 * 6)
    

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

    # connect_points(0, 7, projected_points)
    # connect_points(1, 6, projected_points)
    # connect_points(2, 5, projected_points)
    # connect_points(3, 4, projected_points)

    

    pygame.display.update()