import pygame
from pygame.locals import *
pygame.init()

screen = pygame.display.set_mode((1280, 480))
pygame.display.set_caption("Pong!")

x = 80
y = 190
x1 = 1180
y1 = 190
cx = 640
cy = 240

font = pygame.font.Font('Font.ttf', 32)

score = 0
score1 = 0
radius = 20
velocity = 5
fps = 120
x_speed = 3
y_speed = 3

clock = pygame.time.Clock()

while True:
    r = pygame.Rect(x, y, 20, 100)
    r1 = pygame.Rect(x1, y1, 20, 100)
    c = pygame.Rect(cx, cy, 20, 20)

    screen.fill((0, 0, 0))
    clock.tick(fps)
    
    pygame.draw.rect(screen, (255, 0, 0), r)

    pygame.draw.rect(screen, (0, 0, 255), r1)

    pygame.draw.ellipse(screen, (0, 255, 0), c)

    cx += x_speed
    cy += y_speed

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_w]:
        y -= velocity
    if keys[pygame.K_s]:
        y += velocity

    if y <= 0:
        y = 0
    elif y >= 380:
        y = 380
    if y1 <= 0:
        y1 = 0
    elif y1 >= 380:
        y1 = 380

    if x_speed == 3:        
        if c.centery <= r1.centery:
            y1 -= velocity
        if c.centery >= r1.centery:
            y1 += velocity

    elif x_speed == -3:
        if r1.centery > 240:
            while r1.centery != 240:
                y1 -= velocity
                if r1.centery == 240:
                    break
                break

        if r1.centery < 240:
            while r1.centery != 240:
                y1 += velocity
                if r1.centery == 240:
                    break
                break

    if cx >= 1260:
        cx = 640
        score += 1
    elif cx <= 20:
        cx = 640
        score1 += 1
    elif cy <= 20:
        y_speed = 3
    elif cy >= 460:
        y_speed = -3

    if r.colliderect(c):
        x_speed = 3
    elif r1.colliderect(c):
        x_speed = -3

    score_text = font.render("Player 1: " + str(score), True, 'orange')
    score_text_rect = score_text.get_rect()
    score_text_rect.topleft = (50, 50)

    score1_text = font.render("Player 2: " + str(score1), True, 'orange')
    score1_text_rect = score1_text.get_rect()
    score1_text_rect.topleft = (1035, 50)

    player_win_text = font.render("Player 1 Wins!", True, 'orange')
    player_win_text_rect = player_win_text.get_rect()
    player_win_text_rect.center = (640, 240)

    player_win1_text = font.render("Player 2 Wins!", True, 'orange')
    player_win1_text_rect = player_win1_text.get_rect()
    player_win1_text_rect.center = (640, 240)

    continue_text = font.render("Press any key to play again", True, 'orange')
    continue_rect = continue_text.get_rect()
    continue_rect.center = (640, 300)

    screen.blit(score_text, score_text_rect)
    screen.blit(score1_text, score1_text_rect)

    if score == 20:
        screen.blit(player_win_text, player_win_text_rect)
        screen.blit(continue_text, continue_rect)
        pygame.display.update()

        is_paused = True
        while is_paused:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    score = 0
                    score1 = 0
                    is_paused = False
                if event.type == QUIT:
                    pygame.quit()
        
    if score1 == 20:
        screen.blit(player_win1_text, player_win1_text_rect)
        screen.blit(continue_text, continue_rect)
        pygame.display.update()

        is_paused = True
        while is_paused:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    score = 0
                    score1 = 0
                    is_paused = False
                if event.type == QUIT:
                    pygame.quit()

    pygame.display.update()