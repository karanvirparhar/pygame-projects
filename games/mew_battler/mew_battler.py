import pygame
from pygame.locals import *
from pathlib import Path

ASSET_DIR = Path(__file__).parent / "assets"

pygame.init()

clock = pygame.time.Clock()
fps = 60

Width = 1000
Height = 800

screen = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Mew Battler (2 Player)")

font = pygame.font.SysFont("Comic Sans", 48)

class shot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class s_shot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

shots = []
s_shots = []

timer_event = pygame.event.custom_type()
pygame.time.set_timer(timer_event, 1000)
timer = 30

mewy = Height / 2 - 50
smewy = Height / 2 - 50

mew_hp = 100
smew_hp = 100

show_mew = True
show_smew = True

speed = 10

m = 0

def won():
    global m
    global mew_hp, s_shots
    global smew_hp, shots, show_smew
    global timer, mewy, smewy, show_mew

    p = pygame.draw.rect(screen, (149, 39, 39), (Width // 2 - 200, Height // 2 - 50, 100, 50))
    q = pygame.draw.rect(screen, (149, 39, 39), (Width // 2 + 100, Height // 2 - 50, 100, 50))

    if mew_hp > smew_hp:
        game_over_text = font.render("Mew Wins!", True, 'red')
    elif smew_hp > mew_hp:
        game_over_text = font.render("Shiny Mew Wins!", True, 'red')
    elif smew_hp == mew_hp:
        game_over_text = font.render("It's a Tie!", True, 'red')
    
    game_over_text_rect = game_over_text.get_rect()
    game_over_text_rect.center = (Width // 2, Height // 2 - 100)
    
    play_text = font.render("Play", True, 'pink')
    play_text_rect = play_text.get_rect()
    play_text_rect.center = (p.center)

    quit_text = font.render("Quit", True, 'pink')
    quit_text_rect = quit_text.get_rect()
    quit_text_rect.center = (q.center)

    screen.blit(play_text, play_text_rect)
    screen.blit(quit_text, quit_text_rect)
    screen.blit(game_over_text, game_over_text_rect)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        if event.type == MOUSEBUTTONDOWN:
            if p.collidepoint(event.pos):
                m = 0
                timer = 30

                mewy = Height / 2 - 50
                smewy = Height / 2 - 50

                show_mew = True
                show_smew = True

                mew_hp = 100
                smew_hp = 100

                shots = []
                s_shots = []
            elif q.collidepoint(event.pos):
                pygame.quit()
        if event.type == KEYDOWN:
            if event.key == K_q:
                pygame.quit()

while True:
    clock.tick(fps)

    if m == 0:
        screen.fill("black")
        
        mew_text = font.render('Mew HP: ' + str(mew_hp), True, "pink")
        mew_rect = mew_text.get_rect()
        mew_rect = (10, 10)

        smew_text = font.render('Shiny Mew HP: ' + str(smew_hp), True, "cyan")
        smew_rect = smew_text.get_rect()
        smew_rect = (Width - 430, 10)

        if mewy <= 0:
            mewy = 0
        elif mewy >= Height - 63:
            mewy = Height - 63
        if smewy <= 0:
            smewy = 0
        elif smewy >= Height - 60:
            smewy = Height - 60

        keys = pygame.key.get_pressed()

        if keys[K_w]:
            mewy -= 5
        elif keys[K_s]:
            mewy += 5
        if keys[K_UP]:
            smewy -= 5
        elif keys[K_DOWN]:
            smewy += 5

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            if event.type == KEYDOWN:
                if (event.key == K_q or event.key == K_SPACE or event.key == K_d) and mew:
                    shots.append(shot(mew_image_rect.centerx, mew_image_rect.centery))
                if (event.key == K_LEFT or event.key == K_RCTRL) and shiny_mew:
                    s_shots.append(s_shot(smew_image_rect.centerx, smew_image_rect.centery))
            if event.type == timer_event:
                if timer >= 0:
                    timer -= 1
        
        timer_text = font.render('Time Left: ' + str(timer), True, "red")
        timer_rect = timer_text.get_rect()
        timer_rect.centerx = Width / 2
        timer_rect.y = Height - 80

        if smew_hp <= 0 and mew_hp <= 0 or smew_hp <= 0 or mew_hp <= 0:
            m = 1
            # shots = []
            # s_shots = []
        
        if mew_hp == smew_hp == 0:
            show_mew = False
            show_smew = False
        elif smew_hp <= 0:
            show_smew = False
        elif mew_hp <= 0:
            show_mew = False

        if timer == 0:
            if smew_hp > mew_hp or mew_hp > smew_hp or mew_hp == smew_hp:
                m = 1
            
        for ss in s_shots:
            draw = pygame.draw.circle(screen, "cyan", (ss.x, ss.y), 10)
            ss.x -= speed

            if mew and shiny_mew:
                if draw.colliderect(mew_image_rect):
                    mew_hp -= 5
                    if ss in s_shots:
                        s_shots.remove(ss)
            
            if ss.x < 0: 
                s_shots.remove(ss)

        for s in shots:
            draw = pygame.draw.circle(screen, "pink", (s.x, s.y), 10)
            s.x += speed

            if mew and shiny_mew:
                if draw.colliderect(smew_image_rect):
                    smew_hp -= 5
                    if s in shots:
                        shots.remove(s)

            if s.x > Width:
                shots.remove(s)
        
            for ss in s_shots:
                if draw.colliderect(pygame.Rect(ss.x, ss.y, 10, 10)):
                    if s in shots:
                        shots.remove(s)
                    if ss in s_shots:
                        s_shots.remove(ss)

        if show_mew == True:
            # mew = pygame.draw.rect(screen, "pink", (50, mewy, 10, 100))
            mew = pygame.image.load(str(ASSET_DIR / "mew.png"))
            mew = pygame.transform.flip(mew, True, False)
            mew_image_rect = mew.get_rect()
            mew_image_rect = mew_image_rect.inflate(-10, 0)
            mew_image_rect.topleft = (25, mewy)
            screen.blit(mew, mew_image_rect)
        else:
            mew = None

        if show_smew == True:
            # shiny_mew = pygame.draw.rect(screen, "cyan", (Width - 60, smewy, 10, 100))
            shiny_mew = pygame.image.load(str(ASSET_DIR / "smew.png"))
            smew_image_rect = shiny_mew.get_rect()
            smew_image_rect = smew_image_rect.inflate(10, 0)
            smew_image_rect.topleft = (Width - 75, smewy)
            screen.blit(shiny_mew, smew_image_rect)
        else:
            shiny_mew = None

        screen.blit(mew_text, mew_rect)
        screen.blit(smew_text, smew_rect)
        screen.blit(timer_text, timer_rect)

        pygame.display.update()

    elif m == 1:
        won()
        pygame.display.update()