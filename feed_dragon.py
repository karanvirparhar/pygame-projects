import pygame, random

pygame.init()

window_width = 1000
window_height = 400
display_surface = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Feed The Dragon")

#Set FPS and clock
FPS = 60
clock = pygame.time.Clock()

#Set game values
Player_Starting_Lives = 5
Player_Velocity = 10
Coin_Starting_Velocity = 10
Coin_Acceleration = .5
Buffer_Distance = 100

score = 0
player_lives = Player_Starting_Lives
coin_velocity = Coin_Starting_Velocity

#Set colors
Green = (0, 255, 0)
DarkGreen = (10, 50, 10)
White = (255, 255, 255)
Black = (0, 0, 0)
Red = (255, 0, 0)
Grey = (127, 127, 127)

#Set fonts
font = pygame.font.Font("Font.ttf", 32)

#Set text
score_text = font.render("Score: " + str(score), True, Green, DarkGreen)
score_rect = score_text.get_rect()
score_rect.topleft = (10, 10)
title_text = font.render("Feed the Dragon", True, Green, Grey)
title_rect = title_text.get_rect()
title_rect.centerx = window_width//2
title_rect.y = 10

lives_text = font.render("Lives: " + str(player_lives), True, Green, DarkGreen)
lives_rect = lives_text.get_rect()
lives_rect.topright = (window_width - 10, 10)

game_over_text = font.render("GAME OVER", True, Green, DarkGreen)
game_over_rect = game_over_text.get_rect()
game_over_rect.center = (window_width//2, window_height//2)

continue_text = font.render("Press any key to play again", True, Green, DarkGreen)
continue_rect = continue_text.get_rect()
continue_rect.center = (window_width//2, window_height//2 + 32)

#Set sounds and music
coin_sound = pygame.mixer.Sound("Power_up.wav")
loss_sound = pygame.mixer.Sound("Loss.wav")
pygame.mixer.music.load("song.wav")

#Set images
player_image = pygame.image.load("dragon_right.png")
player_rect = player_image.get_rect()
player_rect.left = 32
player_rect.centery = window_height//2

coin_image = pygame.image.load("coin.png")
coin_rect = coin_image.get_rect()
coin_rect.x = window_width + Buffer_Distance
coin_rect.y = random.randint(64, window_height)

pygame.mixer.music.play(-1, 0.0)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and player_rect.top > 64:
        player_rect.y -= Player_Velocity
    if keys[pygame.K_DOWN] and player_rect.bottom < window_height:
        player_rect.y += Player_Velocity

    if coin_rect.x < 0:
        player_lives -= 1
        loss_sound.play()
        coin_rect.x = window_width + Buffer_Distance
        coin_rect.y = random.randint(64, window_height - 32)
    else:
        coin_rect.x -= coin_velocity

    if player_rect.colliderect(coin_rect):
        score += 1
        coin_sound.play()
        coin_velocity += Coin_Acceleration
        coin_rect.x = window_width + Buffer_Distance
        coin_rect.y = random.randint(64, window_height - 32)

    score_text = font.render("Score: " + str(score), True, Green, DarkGreen)
    lives_text = font.render("Lives: " + str(player_lives), True, Green, DarkGreen)

    if player_lives == 0:
        display_surface.blit(game_over_text, game_over_rect)
        display_surface.blit(continue_text, continue_rect)
        pygame.display.update()

        pygame.mixer.music.stop()
        is_paused = True
        while is_paused:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    score = 0
                    player_lives = Player_Starting_Lives
                    player_rect.y = window_height//2
                    coin_velocity = Coin_Starting_Velocity
                    pygame.mixer.music.play(-1, 0.0)
                    is_paused = False
                if event.type  == pygame.QUIT:
                    is_paused = False
                    running = False

    display_surface.fill(Black)

    display_surface.blit(score_text, score_rect)
    display_surface.blit(title_text, title_rect)
    display_surface.blit(lives_text, lives_rect)
    pygame.draw.line(display_surface, White, (0, 64), (window_width, 64), 2)

    display_surface.blit(player_image, player_rect)
    display_surface.blit(coin_image, coin_rect)

    pygame.display.update()

    clock.tick(FPS)

pygame.quit()
