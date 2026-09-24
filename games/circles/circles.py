import pygame, random
from pygame.locals import *
pygame.init()

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Circles")

x = 20
y = 240
x1 = 620
y1 = 240
fps = 10
radius = 20
n = 40

direction = 0

wall1 = pygame.Rect(640, 0, 5, 480)
wall2 = pygame.Rect(-5, 0, 5, 480)

while True:
    clock = pygame.time.Clock()
    clock.tick(fps)
    screen.fill((0, 0, 0))

    # draw the initial cicles, left one at x and right one at x1
    pygame.draw.circle(screen, (255, 0, 0), (x, y), radius)
    pygame.draw.circle(screen, (0, 0, 255), (x1, y1), radius)

    # move left circle right by 20
    if direction == 0:
        x += 20
        x1 -= 20
        # print("Direction 0: x = ", x)
        # print("Direction 0: x1 = ", x1)
    elif direction == 1:
        x -= 20
        x1 += 20
        # print("Direction 1: x = ", x)
        # print("Direction 1: x1 = ", x1)

    if x == 300:
        # print("x = 320")
        direction = 1
    elif x == 20:
        # print("x = 20")
        direction = 0

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == MOUSEBUTTONDOWN:
            m = random.randint(-5, 10)

    pygame.display.update()