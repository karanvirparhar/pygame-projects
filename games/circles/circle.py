import pygame
from pygame.locals import *
pygame.init()

screen = pygame.display.set_mode((640, 640))
pygame.display.set_caption("Circle")

radius = 10
fps = 10
direction = 0

while True:
    clock = pygame.time.Clock()
    clock.tick(fps)
    screen.fill((0, 0, 0))

    pygame.draw.circle(screen, (255, 0, 0), (320, 320), radius)

    if direction == 0:
        radius += 10
    else:
        radius -= 10

    if radius == 320:
        direction = 1
    
    if radius == 10:
        direction = 0

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    pygame.display.update()