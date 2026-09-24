import pygame, random
from pathlib import Path

from pygame.locals import *
pygame.init()

ASSET_DIR = Path(__file__).parent / "assets"

Width = 640
Height = 480

screen = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Snake!")

w = 20
speed = 20

foodx = (random.randint(0, 620) // w) * w
foody = (random.randint(0, 460) // w) * w

snakex = (random.randint(0, 620) // w) * w
snakey = (random.randint(0, 460) // w) * w

down = 0
up = 0
right = 0
left = 0

clock = pygame.time.Clock()

# empty list for snake coordinates
snakelist = []
# append snake head to the list
snakelist.append([snakex, snakey])

font = pygame.font.Font(str(ASSET_DIR / "font.ttf"), 32)

score = 0

#Set text
score_text = font.render("Score: " + str(score), True, 'purple')
score_rect = score_text.get_rect()
score_rect.topleft = (10, 10)

game_over_text = font.render("GAME OVER", True, 'green')
game_over_rect = game_over_text.get_rect()
game_over_rect.center = (Width//2, Height//2)

continue_text = font.render("Press any key to play again", True, 'green')
continue_rect = continue_text.get_rect()
continue_rect.center = (Width//2, Height//2 + 32)

pygame.mixer.music.load(str(ASSET_DIR / "song.wav"))
food_sound = pygame.mixer.Sound(str(ASSET_DIR / "sound.wav"))
loss_sound = pygame.mixer.Sound(str(ASSET_DIR / "loss.wav"))

m = 0

def menu():
    global m
    # print("entered menu function")
    p = pygame.draw.rect(screen, 'orange', (170, 190, 100, 50))
    q = pygame.draw.rect(screen, 'orange', (370, 190, 100, 50))
    
    play_text = font.render("Play", True, 'white')
    play_text_rect = play_text.get_rect()
    play_text_rect.center = (p.center)

    quit_text = font.render("Quit", True, 'white')
    quit_text_rect = quit_text.get_rect()
    quit_text_rect.center = (q.center)

    screen.blit(play_text, play_text_rect)
    screen.blit(quit_text, quit_text_rect)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

        if event.type == MOUSEBUTTONDOWN:
            if p.collidepoint(event.pos):
                m = 1
                # print("m after play clicked", m)
            elif q.collidepoint(event.pos):
                pygame.quit()

pygame.mixer.music.play(-1, 0.0)

i = 0

def checkerboard(rows, columns):
    r_h = Height/rows
    c_w = Width/columns
    for col in range(columns):
        for row in range(rows):
            pygame.draw.rect(screen, 'orange', (col * c_w, row * r_h, c_w, r_h), 1)

while True:
    clock.tick(10)

    screen.fill('black')

    if m == 0:
        menu()
        pygame.display.update()
    
    if m == 1:       
        # checkerboard(24, 32)

        food = pygame.Rect((foodx, foody, w, w))

        snakehead = pygame.Rect(snakelist[0] + [w, w])

        # draw red color food
        pygame.draw.rect(screen, 'red', food)

        # draw all segments in snakelist
        # print(snakelist)
        # draw snake head which is at index 0
        pygame.draw.rect(screen, 'green', snakehead, 3)

        pygame.draw.circle(screen, 'green', (snakex + 5, snakey + 5), 2)
        pygame.draw.circle(screen, 'green', (snakex + 15, snakey + 5), 2)
        # count = 1
        # draw the rest of the rects
        for i in range(1, len(snakelist)):
            # count += 1
            # print("drawing segment: ", i, snakelist[i])
            snake = pygame.draw.rect(screen, 'green', snakelist[i] + [w, w], 3)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            elif event.type == KEYDOWN:
                if event.key == K_DOWN:
                    if up == 0:
                        down = 1
                        up, right, left = 0, 0, 0
                elif event.key == K_UP:
                    if down == 0:
                        up = 1
                        down, right, left = 0, 0, 0
                elif event.key == K_RIGHT:
                    if left == 0:
                        right = 1
                        left, down, up = 0, 0, 0
                elif event.key == K_LEFT:
                    if right == 0:
                        left = 1
                        right, down, up = 0, 0, 0
                elif event.key == K_q:
                    pygame.quit()
                break

        if down == 1:
            snakey += speed
            # segment[1] += speed
            # for segment in snakelist:
            #     segment[1] += speed
        elif up == 1:
            snakey -= speed
            # segment[1] -= speed
            # for segment in snakelist:
            #     segment[1] -= speed
        elif right == 1:
            snakex += speed
            # segment[0] += speed
            # for segment in snakelist:
            #     segment[0] += speed
        elif left == 1:
            snakex -= speed
            # segment[0] -= speed
            # for segment in snakelist:
            #     segment[0] -= speed

        for segment in snakelist[1:]:
            if len(snakelist) >= 1:
                if segment == snakelist[0]:
                        screen.fill('black')
                        # screen.blit(game_over_text, game_over_rect)
                        # screen.blit(continue_text, continue_rect)
                        # screen.blit(score_text, score_rect)
                        
                        pygame.display.update()

                        # paused = True
                        # while paused:
                        m = 0
                        # pygame.mixer.music.stop()
                        loss_sound.play()
                        snakelist = []
                        score = 0
                        foodx = (random.randint(0, 640) // w) * w
                        foody = (random.randint(0, 480) // w) * w

                        snakex = (random.randint(0, 640) // w) * w
                        snakey = (random.randint(0, 480) // w) * w

                        up, down, left, right = 0, 0, 0, 0

                        # for event in pygame.event.get():
                        #     if event.type == KEYDOWN: 
                        #         # paused = False
                        #         if event.key == K_q:
                        #             pygame.quit()
                        #     elif event.type == QUIT:
                        #         pygame.quit()
                        # if m == 0:
                        # menu()
                        # pygame.display.update()

                        # if m == 1:
                        # paused = False

        if snakex == 640:
            right = 1
            left, down, up = 0, 0, 0
            snakex = -20
        elif snakex == -20:
            left = 1
            right, down, up = 0, 0, 0
            snakex = 640
        elif snakey == 480:
            down = 1
            up, right, left = 0, 0, 0
            snakey = -20
        elif snakey == -20:
            up = 1
            down, right, left = 0, 0, 0
            snakey = 480

        if snakehead.colliderect(food):
            food_sound.play()
            foodx = (random.randint(w, 640 - w) // w) * w
            foody = (random.randint(w, 480 - w) // w) * w
            # eat food amd append snake head coordinates
            # print("snanelist before eating food: ", snakelist)
            snakelist.append([snakex, snakey])
            score += 1
            # print("snakelist after eating food: ", snakelist)
            while True:
                allgood = True
                for segment in snakelist:
                    if segment == [foodx, foody]:
                        allgood = False
                if allgood == False:
                    foodx = (random.randint(0, 640) // w) * w
                    foody = (random.randint(0, 480) // w) * w
                else:
                    break

        # insert new coordinates of the head and remove the tail
        if len(snakelist) >= 1:
            snakelist.pop(len(snakelist) - 1)
        snakelist.insert(0, [snakex, snakey])
        #print("snanelist after pop and insert: ", snakelist)

        score_text = font.render("Score: " + str(score), True, 'purple')

        screen.blit(score_text, score_rect)

        pygame.display.update()