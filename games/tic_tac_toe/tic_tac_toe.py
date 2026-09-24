import pygame, time
from pathlib import Path
from pygame.locals import *

pygame.init()

ASSET_DIR = Path(__file__).parent / "assets"

Height = 640
Width = 640

screen = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Tic Tac Toe")

count = 0

rects = []

font = pygame.font.Font(str(ASSET_DIR / "font.ttf"), 32)

state = {1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: ''}

def checkerboard(rows, columns):
    color = (255, 255, 255)
    r_h = Height/rows
    c_w = Width/columns
    for col in range(columns):
        for row in range(rows):
            r = pygame.Rect(col * c_w, row * r_h, c_w, r_h)
            rects.append(r)
            pygame.draw.rect(screen, color, r, 5)

checkerboard(3, 3)

def x(rect):
    pygame.draw.line(screen, 'white', rect.topleft, rect.bottomright, 10)
    pygame.draw.line(screen, 'white', rect.bottomleft, rect.topright, 10)

def o(rect):
    pygame.draw.circle(screen, 'white', rect.center, rect.width//2, 10)

def checkAndDeclareWinner():
    global rects
    global state
    global count
    continue_text = font.render("Press any key to play again", True, 'orange')
    continue_rect = continue_text.get_rect()
    continue_rect.center = (320, 400)

    winner = ''
    if state[1] == state[2] == state[3] and state[1] != '':
        winner = state[1]
    elif state[4] == state[5] == state[6] and state[4] != '':
        winner = state[4]
    elif state[7] == state[8] == state[9] and state[7] != '':
        winner = state[7]
    elif state[1] == state[5] == state[9] and state[1] != '':
        winner = state[1]
    elif state[1] == state[4] == state[7] and state[1] != '':
        winner = state[1]
    elif state[2] == state[5] == state[8] and state[2] != '':
        winner = state[2]
    elif state[3] == state[6] == state[9] and state[3] != '':
        winner = state[3]
    elif state[3] == state[5] == state[7] and state[3] != '':
        winner = state[3]

    if winner != '':
        win = font.render(winner + " Wins!", True, 'orange')
        win_rect = win.get_rect()
        win_rect.center = (320, 320)
        time.sleep(1)
        screen.fill('black')
        screen.blit(win, win_rect)
        screen.blit(continue_text, continue_rect)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            if event.type == KEYDOWN:
                screen.fill('black')
                rects = []
                count = 0
                state = {1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: ''}
                checkerboard(3, 3)

    if state[1] != '' and state[2] != '' and state[3] != '' and state[4] != '' and state[5] != '' and state[6] != '' and state[7] != '' and state[1] != '' and state[8] != '' and state[9] != '' and winner == '':
        tie = font.render("It's a Tie!", True, 'red')
        tie_rect = tie.get_rect()
        tie_rect.center = (320, 320)
        time.sleep(1)
        screen.fill('black')
        screen.blit(tie, tie_rect)
        screen.blit(continue_text, continue_rect)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            if event.type == KEYDOWN:
                screen.fill('black')
                rects = []
                count = 0
                state = {1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: ''}
                checkerboard(3, 3)

while True:
    winner = ''

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
    
        if event.type == MOUSEBUTTONDOWN:
            index = 0
            for rect in rects:
                index += 1
                if state[index] == '':
                    if rect.collidepoint((event.pos[0], event.pos[1])):
                        count += 1
                        if count % 2 == 1:
                            x(rect)
                            state[index] = 'X'
                        else:
                            o(rect)
                            state[index] = 'O'
    
    pygame.display.update()
    
    checkAndDeclareWinner()