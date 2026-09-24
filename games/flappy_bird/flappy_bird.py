import pygame
from pygame.locals import *
import random
from pathlib import Path

ASSET_DIR = Path(__file__).parent / "assets"

pygame.init()

Width = 1000
Height = 800

screen = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Flappy Bird")

clock = pygame.time.Clock()
fps = 60

gravity = 0.5
jump_velocity = -10
velocity = 0

y = Height // 2

class rect:
    def __init__(self, x, y, l, score):
        self.x = x
        self.y = y
        self.l = l
        self.score = score

rects = []
x = Width

font = pygame.font.SysFont("Comic Sans", 48)

for i in range(10):
    shift = random.randint(250, 300)
    x += shift
    rect_y = 0
    l = random.randint(100, 500)

    rectangle = rect(x, rect_y, l, True)

    rects.append(rectangle)

score = 0

run = True

bg = pygame.image.load(str(ASSET_DIR / "flappybird.jpg"))
bg = pygame.transform.scale(bg, (1000, 800))

while run:
    screen.blit(bg, (0, 0))

    clock.tick(fps)

    # bird = pygame.draw.circle(screen, "orange", (100, y), 15)
    bird = pygame.image.load(str(ASSET_DIR / "bird.png"))
    # bird = pygame.transform.scale(bird, (50, 50))
    bird_rect = bird.get_rect()
    bird_rect.center = (100, y)

    score_text = font.render("Score: " + str(score), True, "purple")
    score_rect = score_text.get_rect()
    score_rect.topleft = (10, 10)
   
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                run = False
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                run = False
        if event.type == QUIT:
            pygame.quit()
   
    screen.blit(score_text, score_rect)
    screen.blit(bird, bird_rect)

    pygame.display.update()

dark_green = (0, 100, 0)

bg_xs = []

bg_x = 0

fall = True

running = True

while running:
    screen.blit(bg, (bg_x, 0))
    screen.blit(bg, (bg_x + Width, 0))

    bg_x -= 3

    if bg_x + Width <= 0:
        bg_x = 0

    clock.tick(fps)

    # bird = pygame.draw.circle(screen, "orange", (100, y), 15)
    bird = pygame.image.load(str(ASSET_DIR / "bird.png"))
    # bird = pygame.transform.scale(bird, (50, 50))
    bird_rect = bird.get_rect()
    bird_rect.center = (100, y)

    score_text = font.render("Score: " + str(score), True, "purple")
    score_rect = score_text.get_rect()
    score_rect.topleft = (10, 10)

    for index, obj in enumerate(rects):
        r = pygame.draw.rect(screen, dark_green, (obj.x, obj.y, 30, obj.l))

        r1 = pygame.draw.rect(screen, dark_green, (obj.x, obj.y + obj.l + 200, 30, Height - (obj.y + obj.l + 50)))
 
        obj.x -= 3

        if bird_rect.colliderect(r) or bird_rect.colliderect(r1):
            running = False
            print("You Lose")
       
        if obj.x + 30 < 0:
            shift = random.randint(200, 300)
            obj.x = last_x + shift
            obj.l = random.randint(100, 500)
            obj.score = True
            rects.remove(obj)
            rects.append(obj)
       
        if obj.x < 100 - 15 and obj.score == True:
            score += 1
            obj.score = False
   
    last_x = rects[9].x

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                velocity = jump_velocity
                fall = True
                if y + 15 >= Height:
                    y = Height - 16
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                velocity = jump_velocity
                fall = True
                if y + 15 >= Height:
                    y = Height - 16
   
    if y + bird_rect.height >= Height - 45:
        y = Height - 15
        fall = False
        running = False 
        print("You Lose")

    if fall == True:
        velocity += gravity

        y += velocity
   
    screen.blit(score_text, score_rect)
    screen.blit(bird, bird_rect)

    pygame.display.update()