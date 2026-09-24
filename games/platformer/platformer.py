import pygame
from pygame.locals import *
import time

pygame.init()

Width = 900
Height = 900

screen = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Platformer")

clock = pygame.time.Clock()
fps = 60

class ListNode:
    def __init__(self, val, next):
        self.val = val
        self.next = next

class TreeNode:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right

# level1 = [["f", "", "", "", "", "", "", "", ""],
#          ["r", "r", "r", "r", "r", "", "r", "", ""],
#          ["", "", "", "", "", "", "", "", "r"],
#          ["", "", "", "", "", "", "", "r", ""],
#          ["", "", "", "", "", "", "", "", ""],
#          ["", "", "", "", "", "r", "", "", ""],
#          ["", "", "", "", "r", "", "", "", ""],
#          ["", "", "", "", "", "", "", "", ""],
#          ["r", "r", "r", "r", "r", "r", "r", "r", "r"]]

# level_ = ListNode([["", "", "", "", "", "", "", "", ""],
#                    ["", "", "", "", "", "", "", "", ""],
#                    ["", "", "", "", "", "", "", "", ""],
#                    ["", "", "", "", "", "", "", "", ""],
#                    ["", "", "", "", "", "", "", "", ""],
#                    ["", "", "", "", "", "", "", "", ""],
#                    ["", "", "", "", "", "", "", "", ""],
#                    ["", "", "", "", "", "", "", "", ""],
#                    ["", "", "", "", "", "", "", "", ""]], None)

level9 = ListNode([["", "", "", "", "", "", "", "", ""],
                   ["", "", "r", "", "", "", "", "", ""],
                   ["f", "", "", "", "", "", "", "", ""],
                   ["r", "", "", "", "r", "", "", "", ""],
                   ["", "", "", "", "", "", "r", "", ""],
                   ["", "", "", "", "", "", "", "", ""],
                   ["", "", "", "", "", "", "r", "", ""],
                   ["", "", "", "", "", "", "", "", ""],
                   ["r", "", "", "r", "", "", "r", "", ""]], None)

level8 = ListNode([["", "", "", "", "", "", "", "", ""],
                   ["", "", "", "", "", "f", "", "", ""],                   
                   ["", "", "", "", "", "r", "", "", ""],
                   ["", "", "", "", "", "r", "", "", ""],
                   ["r", "r", "r", "r", "", "r", "r", "", ""],
                   ["", "", "", "", "", "r", "", "", ""],
                   ["r", "", "", "", "", "", "", "r", ""],
                   ["", "", "", "", "", "r", "", "", ""],
                   ["", "", "r", "", "", "", "", "", ""]], level9)

level7 = ListNode([["", "", "", "", "", "", "", "", ""],
                   ["", "", "r", "", "", "", "", "", "f"],                   
                   ["", "", "", "", "", "r", "", "", "r"],
                   ["r", "", "", "", "", "", "", "", ""],
                   ["", "r", "", "", "", "", "", "", ""],
                   ["", "", "", "", "", "", "", "", ""],
                   ["r", "", "r", "", "", "", "", "", ""],
                   ["", "", "", "", "", "", "", "", ""],
                   ["", "", "", "", "", "", "", "", ""]], level8)

level6 = ListNode([["", "", "", "", "", "", "", "", ""],
                   ["", "", "", "", "", "", "", "", ""],
                   ["", "", "", "", "r", "", "", "", ""],
                   ["", "", "", "", "", "", "", "", ""],
                   ["", "", "r", "", "", "", "r", "", ""],
                   ["", "", "", "", "r", "r", "r", "", ""],
                   ["r", "", "", "", "", "", "", "", "r"],
                   ["", "", "", "", "", "f", "", "", ""],
                   ["", "", "", "", "", "r", "r", "", ""]], level7)

level5 = ListNode([["", "", "", "", "", "", "", "", ""],
                   ["", "", "", "", "", "f", "", "", ""],                   
                   ["", "", "", "", "", "r", "", "", ""],
                   ["", "", "", "", "", "", "", "", ""],
                   ["", "", "", "", "", "", "", "", "r"],
                   ["", "", "", "", "", "", "", "", ""],
                   ["", "", "", "", "", "", "r", "", ""],
                   ["", "", "", "", "", "", "", "", ""],
                   ["r", "", "", "r", "", "", "r", "", ""]], level6)

level4 = ListNode([["", "", "", "", "", "", "", "", ""],
                   ["", "", "", "", "", "f", "", "", ""],
                   ["", "", "", "", "", "r", "", "", ""],
                   ["", "", "", "", "", "", "", "", ""],
                   ["", "", "", "", "", "r", "", "", ""],
                   ["", "", "", "", "", "", "", "", ""],
                   ["", "", "", "", "", "r", "", "", ""],
                   ["r", "", "", "r", "", "", "", "", ""],
                   ["", "", "", "", "", "", "", "", ""]], level5)

level3 = ListNode([["", "", "", "", "", "", "", "", ""],
                   ["", "", "", "r", "", "", "", "", ""],
                   ["", "r", "", "", "", "r", "", "", ""],
                   ["", "", "", "", "", "", "", "", ""],
                   ["", "", "r", "", "", "", "", "", "f"],
                   ["", "", "", "", "", "", "", "", "r"],
                   ["", "", "", "r", "", "", "", "", ""],
                   ["r", "", "", "", "", "", "r", "", ""],
                   ["", "", "r", "", "", "", "", "", ""]], level4)

level2 = ListNode([["", "", "", "", "", "", "", "", ""],
                   ["", "", "", "", "", "", "", "", ""],
                   ["", "", "", "", "", "", "", "", "f"],
                   ["", "", "", "", "", "", "", "", "r"],
                   ["", "", "", "", "", "", "", "", ""],
                   ["", "", "", "", "r", "", "", "r", ""],
                   ["", "", "r", "", "", "", "", "", ""],
                   ["", "", "", "", "", "", "r", "", ""],
                   ["r", "", "", "", "", "", "", "", ""]], level3)

level1 = ListNode([["f", "", "", "", "", "", "", "", ""],
                   ["r", "r", "r", "r", "r", "", "r", "", ""],
                   ["", "", "", "", "", "", "", "", "r"],
                   ["", "", "", "", "", "", "", "r", ""],
                   ["", "", "", "", "", "", "", "", ""],
                   ["", "", "", "", "", "r", "", "", ""],
                   ["", "", "", "", "r", "", "", "", ""],
                   ["", "", "", "", "", "", "", "", ""],
                   ["r", "r", "r", "r", "r", "r", "r", "r", "r"]], level2)

# level2 = [["", "", "", "", "", "", "", "", ""],
#           ["", "", "", "", "", "", "", "", ""],
#           ["", "", "", "", "", "", "", "", "f"],
#           ["", "", "", "", "", "", "", "", "r"],
#           ["", "", "", "", "", "", "", "", ""],
#           ["", "", "", "", "r", "", "", "r", ""],
#           ["", "", "r", "", "", "", "", "", ""],
#           ["", "", "", "", "", "", "r", "", ""],
#           ["r", "", "", "", "", "", "", "", ""]]

level = level1
# next_level = level2

x = 50
y = Height // 2
radius = 20

y_velocity = 0
gravity = 0.98

fall = True

n = 1

x_move = True

check_for_collisions = True

s = Width // len(level.val)

collision_detected = False

while True:
    screen.fill("black")

    clock.tick(fps)

    # print(x, y)
    player = pygame.draw.circle(screen, "red", (x, y), radius)

    if fall == True:
        y += y_velocity
        # print(y_velocity * 2)
        y_velocity += gravity
        # print(y)

    # collision_detected = False

    try:
        for i, row in enumerate(level.val):
            for j, col in enumerate(row):
                if col == "r":
                    r = pygame.draw.rect(screen, "orange", (j * s, i * s, s, s))

                    if player.colliderect(r):
                        collision_detected = True
                        if (y + radius) >= r.top and (y + radius) <= r.top + y_velocity * 2: # collision with top of rectangle
                            y = r.top - radius + 1 # add + 1 to make it detect a collision. if it doesn't detect this as a collision when it is at r.top - radius, it will set fall to True and go into the block and up again
                            y_velocity = 0
                            fall = False
                            x_move = True
                        if (y - radius) <= r.bottom and (y - radius) >= r.bottom + y_velocity * 2: # collision with bottom of rectangle
                            y_velocity = 0
                        elif ((x + radius) >= r.left and (x + radius) <= r.left + 20) or ((x - radius) <= r.right and (x - radius) >= r.right - 20): # collision with side of rectangle
                            x_move = False

                    # print(i, j)
                    # time.sleep(2)

                    # try:
                    #     if not fall:
                    #         if (x + radius <= r.left and level.val[i - 1][j] == "") or (x - radius >= r.right and level.val[i + 1][j] == ""):
                    #             print(x+radius)
                    #             print(r.left)
                    #             print(r.right)
                    #             fall = True
                    # except IndexError:
                    #     pass

                            
                if col == "f":
                    fl = pygame.draw.line(screen, "green", (j * s + s // 2 - 20, i * s + 20), (j * s + s // 2 - 20, i * s + s), 5)
                    ft = pygame.draw.polygon(screen, "green", ((j * s + s // 2 - 20, i * s + 20), (j * s + s // 2 - 20, i * s + 50), (j * s + s // 2 + 20, i * s + 50)))

                    if player.colliderect(fl) or player.colliderect(ft):
                        level = level.next
                        fall = True
                        check_for_collisions = True
                        x = 50
                        y = Height // 2
                        y_velocity = 0
            
        if not collision_detected:
            x_move = True
            fall = True
            # y_velocity = 0

    except AttributeError:
        level = level1
    
    # if fall == True:
    #     check_for_collisions = True
   
    keys = pygame.key.get_pressed()

    if x_move:
        if keys[K_d] or keys[K_RIGHT]:
            x += 7
            print(x)
        if keys[K_a] or keys[K_LEFT]:
            x -= 7
            print(x)
    
    print(x_move)

    # print(check_for_collisions)
   
    if x - radius <= 0:
        x = radius
    elif x + radius >= Width:
        x = Width - radius

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                if not fall:
                    fall = True
                    y_velocity = -20
                    # check_for_collisions = True
   
    if y - radius >= Height:
        level = level1
        fall = True
        # check_for_collisions = True
        x = 50
        y = Height // 2
        y_velocity = 0

    pygame.display.update()