import pygame
from pygame.locals import *
import random

pygame.init()

Width = 1000
Height = 800

screen = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Racer")

clock = pygame.time.Clock()
fps = 60

class track_point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def draw(self):
        pygame.draw.circle(screen, "grey", (self.x, self.y), 5)
    def co_draw(self):
        pygame.draw.circle(screen, "grey", (self.x - 200, self.y), 5)

shift = random.randint(400, 600)

points = []

for i in range(10):
    px = random.randint(500, 800)
    py = Height - shift
    shift += random.randint(400, 600)

    p = track_point(px, py)

    points.append(p)

last_x = points[0].x
last_y = Height

first_gone = False

x = last_x - 100

speed = 0

running = True

n = 0

while running:
    screen.fill("black")

    clock.tick(fps)

    player = pygame.draw.circle(screen, "orange", (x, Height - 100), 20)

    for index, obj in enumerate(points):
        # obj.draw()
        # obj.co_draw()

        line1 = pygame.draw.line(screen, "grey", (last_x, last_y), (obj.x, obj.y), 5)
        line2 = pygame.draw.line(screen, "grey", (last_x - 200, last_y), (obj.x - 200, obj.y), 5)

        obj.y += 5

        # if obj.y - 5 >= Height:
        #     obj.y = points[len(points) - 1].x - 500

        if index != len(points) - 1:
            last_x = obj.x
            last_y = obj.y
        elif not first_gone and index == len(points) - 1:
            last_x = Width // 4 * 3
            last_y = points[0].y + 500
        elif first_gone and index == len(points) - 1:
            last_x = obj.x
            last_y = points[0].y + 500
        
        if index == 0 and obj.y - 5 >= Height + 100:
            first_gone = True
            addit_shift = random.randint(400, 600)
            obj.y = points[len(points) - 1].y - addit_shift
            element = points.pop(0)
            points.append(element)
        
        if player.colliderect(line1) or player.colliderect(line2):
            # running = False
            n += 1
            print("You Lose", n)
            # pass

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
    
    keys = pygame.key.get_pressed()

    if keys[K_RIGHT]:
        speed = 5
        x += speed
    elif keys[K_LEFT]:
        speed = -5
        x += speed
    else:
        if speed > 0:
            
            speed -= 1
        elif speed < 0:
            speed += 1
        x += speed
    
    # print(speed)
   
    pygame.display.update()