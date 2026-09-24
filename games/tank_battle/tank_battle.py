import pygame
from pygame.locals import *
import math

pygame.init()

Width = 1000
Height = 800

clock = pygame.time.Clock()
fps = 60

screen = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Fortz")

track_len = 5
v = 100
angle_deg1 = 45
angle_deg2 = 90 + 45
t1 = 0
t2 = 0
gravity = 9.81

x1 = Width // 8
x2 = Width // 8 * 7
y0 = Height - 20

class Projectile:
    def __init__(self, x, y, t, angle_deg):
        self.original_x = x
        self.original_y = y
        self.x = None
        self.y = None
        self.t = t
        self.angle_deg = angle_deg
    def move(self):
        # for i in range(track_len):
        angle_rad = math.radians(self.angle_deg)
        self.t += 0.1
        self.x = self.original_x + v * self.t * math.cos(angle_rad)
        self.y = self.original_y - v * self.t * math.sin(angle_rad) + 0.5 * gravity * self.t**2
    def draw(self):
        canon_ball = pygame.draw.circle(screen, (20, 20, 20), (self.x, self.y), 10)
        return canon_ball

# launch1 = False
# launch2 = False

txs1 = []
tys1 = []

txs2 = []
tys2 = []

p1s = []
p2s = []

hp1x_shift = 0
hp2x_shift = 0

hp1_width = 40
hp2_width = 40

font = pygame.font.SysFont("Comic Sans", 48)

starting = True

while starting:
    screen.fill((135, 206, 235))

    sun = pygame.draw.circle(screen, (251, 208, 38), (Width, 0), 150)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                if q.collidepoint(event.pos):
                    pygame.quit()
                    exit()
                elif p.collidepoint(event.pos):
                    starting = False

    p = pygame.draw.rect(screen, (149, 39, 39), (Width // 2 - 150, Height // 2 - 75 // 2, 100, 75))
    q = pygame.draw.rect(screen, (149, 39, 39), (Width // 2 + 50, Height // 2 - 75 // 2, 100, 75))

    play_text = font.render("Play", True, "pink")
    play_rect = play_text.get_rect()
    play_rect.center = p.center

    quit_text = font.render("Quit", True, "pink")
    quit_rect = quit_text.get_rect()
    quit_rect.center = q.center

    txs1 = []
    tys1 = []
    for i in range(track_len):
        angle_rad1 = math.radians(angle_deg1)
        t1 += 0.1
        px = x1 + v * t1 * math.cos(angle_rad1)
        py = y0 - v * t1 * math.sin(angle_rad1) + 0.5 * gravity * t1**2

        txs1.append(px)
        tys1.append(py)
    t1 = 0

    txs2 = []
    tys2 = []
    for i in range(track_len):
        angle_rad2 = math.radians(angle_deg2)
        t2 += 0.1
        px2 = x2 + v * t2 * math.cos(angle_rad2)
        py2 = y0 - v * t2 * math.sin(angle_rad2) + 0.5 * gravity * t2**2

        txs2.append(px2)
        tys2.append(py2)
    t2 = 0

    for index, x in enumerate(txs1):
        pygame.draw.circle(screen, "white", (x, tys1[index]), 3)

    for index, x in enumerate(txs2):
        pygame.draw.circle(screen, "white", (x, tys2[index]), 3)
    
    player1 = pygame.draw.circle(screen, "red", (x1, Height - 20), 20)

    hp1 = pygame.draw.rect(screen, "red", (x1 - 20 + hp1x_shift, y0 - 30, hp1_width, 5))

    player2 = pygame.draw.circle(screen, "blue", (x2, Height - 20), 20)

    hp2 = pygame.draw.rect(screen, "red", (x2 - 20 + hp2x_shift, y0 - 30, hp2_width, 5))
    
    screen.blit(play_text, play_rect)
    screen.blit(quit_text, quit_rect)
    
    pygame.display.update()

while True:
    screen.fill((135, 206, 235))

    clock.tick(fps)

    sun = pygame.draw.circle(screen, (251, 208, 38), (Width, 0), 150)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                projectile = Projectile(x1, y0, 0, angle_deg1)
                p1s.append(projectile)
            if event.key == K_RCTRL:
                projectile = Projectile(x2, y0, 0, angle_deg2)
                p2s.append(projectile)
    
    keys = pygame.key.get_pressed()

    if keys[K_d]:
        x1 += 10
    if keys[K_a]:
        x1 -= 10
    if keys[K_w]:
        angle_deg1 += 1
    if keys[K_s]:
        angle_deg1 -= 1
    if keys[K_RIGHT]:
        x2 += 10
    if keys[K_LEFT]:
        x2 -= 10
    if keys[K_UP]:
        angle_deg2 -= 1
    if keys[K_DOWN]:
        angle_deg2 += 1

    txs1 = []
    tys1 = []
    for i in range(track_len):
        angle_rad1 = math.radians(angle_deg1)
        t1 += 0.1
        px = x1 + v * t1 * math.cos(angle_rad1)
        py = y0 - v * t1 * math.sin(angle_rad1) + 0.5 * gravity * t1**2

        txs1.append(px)
        tys1.append(py)
    t1 = 0

    txs2 = []
    tys2 = []
    for i in range(track_len):
        angle_rad2 = math.radians(angle_deg2)
        t2 += 0.1
        px2 = x2 + v * t2 * math.cos(angle_rad2)
        py2 = y0 - v * t2 * math.sin(angle_rad2) + 0.5 * gravity * t2**2

        txs2.append(px2)
        tys2.append(py2)
    t2 = 0

    for index, x in enumerate(txs1):
        pygame.draw.circle(screen, "white", (x, tys1[index]), 3)

    for index, x in enumerate(txs2):
        pygame.draw.circle(screen, "white", (x, tys2[index]), 3)
    
    for p1 in p1s:
        p1.move()

        if p1.y - 20 >= Height:
            p1s.remove(p1)
        
        if p1.draw().colliderect(player2):
            hp2x_shift += 5
            hp2_width -= 10
            p1s.remove(p1)
    
    for p2 in p2s:
        p2.move()

        if p2.y - 20 >= Height:
            p2s.remove(p2)
        
        if p2.draw().colliderect(player1):
            hp1x_shift += 5
            hp1_width -= 10
            p2s.remove(p2)

    if x1 - 20 <= 0:
        x1 = 20
    elif x1 + 20 >= Width // 2 - 100:
        x1 = Width // 2 - 120
    
    if x2 + 20 >= Width:
        x2 = Width - 20
    elif x2 - 20 <= Width // 2 + 100:
        x2 = Width // 2 + 120

    player1 = pygame.draw.circle(screen, "red", (x1, Height - 20), 20)

    hp1 = pygame.draw.rect(screen, "red", (x1 - 20 + hp1x_shift, y0 - 30, hp1_width, 5))

    player2 = pygame.draw.circle(screen, "blue", (x2, Height - 20), 20)

    hp2 = pygame.draw.rect(screen, "red", (x2 - 20 + hp2x_shift, y0 - 30, hp2_width, 5))

    pygame.display.update()

    while hp1_width <= 0 or hp2_width <= 0:
        screen.fill((135, 206, 235))

        sun = pygame.draw.circle(screen, (251, 208, 38), (Width, 0), 150)

        if hp1_width <= 0:
            win_text = font.render("Blue Wins!", True, "blue")
        elif hp2_width <= 0:
            win_text = font.render("Red Wins!", True, "red")
        win_rect = win_text.get_rect()
        win_rect.center = (Width // 2, Height // 2 - 50)

        p = pygame.draw.rect(screen, (149, 39, 39), (Width // 2 - 150, Height // 2 + 50, 100, 75))
        q = pygame.draw.rect(screen, (149, 39, 39), (Width // 2 + 50, Height // 2 + 50, 100, 75))

        play_text = font.render("Play", True, "pink")
        play_rect = play_text.get_rect()
        play_rect.center = p.center

        quit_text = font.render("Quit", True, "pink")
        quit_rect = quit_text.get_rect()
        quit_rect.center = q.center

        player1 = pygame.draw.circle(screen, "red", (x1, Height - 20), 20)

        hp1 = pygame.draw.rect(screen, "red", (x1 - 20 + hp1x_shift, y0 - 30, hp1_width, 5))

        player2 = pygame.draw.circle(screen, "blue", (x2, Height - 20), 20)

        hp2 = pygame.draw.rect(screen, "red", (x2 - 20 + hp2x_shift, y0 - 30, hp2_width, 5))

        txs1 = []
        tys1 = []
        for i in range(track_len):
            angle_rad1 = math.radians(angle_deg1)
            t1 += 0.1
            px = x1 + v * t1 * math.cos(angle_rad1)
            py = y0 - v * t1 * math.sin(angle_rad1) + 0.5 * gravity * t1**2

            txs1.append(px)
            tys1.append(py)
        t1 = 0

        txs2 = []
        tys2 = []
        for i in range(track_len):
            angle_rad2 = math.radians(angle_deg2)
            t2 += 0.1
            px2 = x2 + v * t2 * math.cos(angle_rad2)
            py2 = y0 - v * t2 * math.sin(angle_rad2) + 0.5 * gravity * t2**2

            txs2.append(px2)
            tys2.append(py2)
        t2 = 0

        for index, x in enumerate(txs1):
            pygame.draw.circle(screen, "white", (x, tys1[index]), 3)

        for index, x in enumerate(txs2):
            pygame.draw.circle(screen, "white", (x, tys2[index]), 3)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    if q.collidepoint(event.pos):
                        pygame.quit()
                        exit()
                    elif p.collidepoint(event.pos):
                        txs1 = []
                        tys1 = []

                        txs2 = []
                        tys2 = []

                        p1s = []
                        p2s = []

                        hp1x_shift = 0
                        hp2x_shift = 0

                        hp1_width = 40
                        hp2_width = 40

                        track_len = 5
                        v = 100
                        angle_deg1 = 45
                        angle_deg2 = 90 + 45
                        t1 = 0
                        t2 = 0
                        gravity = 9.81

                        x1 = Width // 8
                        x2 = Width // 8 * 7
                        y0 = Height - 20
        
        for p1 in p1s:
            p1.draw()
        
        for p2 in p2s:
            p2.draw()
        
        screen.blit(win_text, win_rect)
        screen.blit(play_text, play_rect)
        screen.blit(quit_text, quit_rect)

        pygame.display.update()