import pygame
from pygame.locals import *
import random
import math
from easygui import *
import json
from pathlib import Path

ASSET_DIR = Path(__file__).parent / "assets"
DATA_FILE = ASSET_DIR / "usernames.json"


def asset_path(filename):
    return str(ASSET_DIR / filename)

pygame.init()

Width = 1500
Height = 500

text = "Enter your Username"
title = "Login"
# d_text = "Enter here..."
name = enterbox(text, title)

screen = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Physics Runner")

anime_run = []
anime_jump = []

clock = pygame.time.Clock()
fps = 25

with open(DATA_FILE, "r") as file:
    data = json.load(file)

score = 0
high_score = 0

if name in data:
    high_score = data[name]

if name == None:
    pygame.quit()

# def get_high_score():
#     with open("score.txt", "r") as file:
#         return int(file.read())
    
# def save_high_score(score):
#     with open("score.txt", "w") as file:
#         file.write(str(score))
    
# high_score = get_high_score()

bg = pygame.image.load(asset_path('BG.jpg'))
bg_width = bg.get_width()

num_collectibles = 100
collectibles = []

m = 2

physics_facts = [
    "The speed of light in a vacuum is approximately 299,792,458 meters per second.",
    "The universe is approximately 13.8 billion years old.",
    "The Milky Way galaxy is about 100,000 light-years in diameter.",
    "A light-year is the distance light travels in one year, about 5.88 trillion miles.",
    "The theory of relativity was developed by Albert Einstein.",
    "E=mc^2 is Einstein's famous equation relating energy (E) to mass (m) and the speed of light (c).",
    "Quantum mechanics describes the behavior of particles on very small scales.",
    "The Heisenberg Uncertainty Principle states that it is impossible to simultaneously know the exact position and momentum of a particle.",
    "The Higgs boson is a particle associated with the Higgs field, which gives other particles mass.",
    "Black holes are regions of space where gravity is so strong that not even light can escape.",
    "The event horizon is the boundary around a black hole beyond which nothing can escape.",
    "The Big Bang theory describes the origin of the universe as a rapid expansion from a hot, dense state.",
    "Dark matter is a form of matter that does not emit or absorb light and is thought to make up most of the matter in the universe.",
    "Dark energy is a mysterious force causing the accelerated expansion of the universe.",
    "The electromagnetic spectrum includes radio waves, microwaves, infrared radiation, visible light, ultraviolet radiation, X-rays, and gamma rays.",
    "Visible light is only a small part of the electromagnetic spectrum.",
    "The Doppler effect describes the change in frequency or wavelength of a wave in relation to an observer moving relative to the source of the wave.",
    "Redshift occurs when light from an object moving away from an observer is shifted to longer wavelengths.",
    "Blueshift occurs when light from an object moving toward an observer is shifted to shorter wavelengths.",
    "Gravity is a force of attraction between masses.",
    "Isaac Newton formulated the laws of motion and universal gravitation.",
    "Newton's first law states that an object at rest stays at rest and an object in motion stays in motion unless acted upon by an external force.",
    "Newton's second law states that the force acting on an object is equal to its mass times its acceleration (F=ma).",
    "Newton's third law states that for every action, there is an equal and opposite reaction.",
    "The law of conservation of energy states that energy cannot be created or destroyed, only transformed from one form to another.",
    "The law of conservation of momentum states that the total momentum of a closed system remains constant if no external forces act on it.",
    "Thermodynamics is the study of heat and energy transfer.",
    "The first law of thermodynamics states that energy cannot be created or destroyed, only transferred or converted from one form to another.",
    "The second law of thermodynamics states that the total entropy of an isolated system always increases over time.",
    "Entropy is a measure of the disorder or randomness in a system.",
    "Absolute zero is the lowest possible temperature, where all molecular motion stops, and it is 0 Kelvin or -273.15 degrees Celsius.",
    "The Kelvin scale is an absolute temperature scale starting at absolute zero.",
    "Heat is the transfer of thermal energy between objects with different temperatures.",
    "Conduction is the transfer of heat through direct contact between materials.",
    "Convection is the transfer of heat through the movement of fluids (liquids or gases).",
    "Radiation is the transfer of energy through electromagnetic waves.",
    "A photon is a particle of light and a quantum of electromagnetic radiation.",
    "Electrons are negatively charged particles that orbit the nucleus of an atom.",
    "Protons are positively charged particles found in the nucleus of an atom.",
    "Neutrons are neutral particles found in the nucleus of an atom.",
    "Atoms are made up of protons, neutrons, and electrons.",
    "Isotopes are atoms with the same number of protons but different numbers of neutrons.",
    "Radioactive decay is the process by which unstable atomic nuclei lose energy by emitting radiation.",
    "Alpha decay involves the emission of an alpha particle (two protons and two neutrons) from a nucleus.",
    "Beta decay involves the emission of a beta particle (an electron or positron) from a nucleus.",
    "Gamma decay involves the emission of gamma radiation (high-energy photons) from a nucleus.",
    "Nuclear fission is the splitting of a heavy atomic nucleus into two lighter nuclei, releasing energy.",
    "Nuclear fusion is the combining of two light atomic nuclei to form a heavier nucleus, releasing energy.",
    "Stars generate energy through nuclear fusion reactions in their cores.",
    "The Sun is a main-sequence star composed primarily of hydrogen and helium.",
    "A supernova is a powerful explosion that occurs when a massive star exhausts its nuclear fuel and collapses under its own gravity.",
    "A neutron star is a dense remnant left after a supernova explosion, composed mostly of neutrons.",
    "A pulsar is a rapidly rotating neutron star that emits beams of electromagnetic radiation.",
    "A white dwarf is a small, dense remnant left after a low-mass star exhausts its nuclear fuel and sheds its outer layers.",
    "A black hole forms when a massive star collapses under its own gravity to a point where its escape velocity exceeds the speed of light.",
    "The Schwarzschild radius is the radius within which the escape velocity from a black hole exceeds the speed of light.",
    "Hawking radiation is theoretical radiation predicted to be emitted by black holes due to quantum effects near the event horizon.",
    "The cosmic microwave background radiation is residual thermal radiation from the Big Bang, filling the universe almost uniformly.",
    "The Hubble Space Telescope has provided valuable observations and images\nof distant galaxies and other astronomical objects since its launch in 1990.",
    "The Large Hadron Collider (LHC) is the world's largest and most powerful particle accelerator, located at CERN near Geneva, Switzerland.",
    "The Standard Model of particle physics describes the fundamental particles and forces (except gravity) that make up the universe.",
    "Quarks are elementary particles that combine to form protons and neutrons.",
    "Leptons are elementary particles that include electrons, muons, tau particles, and neutrinos.",
    "Gluons are elementary particles that mediate the strong nuclear force between quarks.",
    "Photons are elementary particles that mediate the electromagnetic force between charged particles.",
    "W and Z bosons are elementary particles that mediate the weak nuclear force responsible for radioactive decay processes.",
    "Gravitons are hypothetical elementary particles that would mediate the force of gravity if they exist (not yet observed).",
    "String theory proposes that fundamental particles are not point-like\nbut rather tiny vibrating strings with different modes corresponding to different particles.",
    "General relativity describes gravity as the curvature of spacetime caused by mass and energy."
]

randomindex = random.randint(0, len(physics_facts) - 1)

def starting_menu():
    global m
    global score

    screen.fill('black')

    p = pygame.draw.rect(screen, (149, 39, 39), (Width // 2 - 150, Height // 2 - 25, 100, 50))
    q = pygame.draw.rect(screen, (149, 39, 39), (Width // 2 + 50, Height // 2 - 25, 100, 50))

    play_text = font.render("Play", True, "pink")
    play_text_rect = play_text.get_rect()
    play_text_rect.center = p.center

    quit_text = font.render("Quit", True, "pink")
    quit_text_rect = quit_text.get_rect()
    quit_text_rect.center = q.center

    screen.blit(play_text, play_text_rect)
    screen.blit(quit_text, quit_text_rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_q:
                pygame.quit()
                exit()
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1 and p.collidepoint(event.pos):
                m = 0
                score = 0
                player_rect.y = Height - new_player_image.get_height()
                initcollectibles()
            if event.button == 1 and q.collidepoint(event.pos):
                pygame.quit()
                exit()

    pygame.display.update()

def game_over_menu():
    global randomindex
    global m
    global score

    screen.fill('black')

    randomfact = physics_facts[randomindex]

    game_over_text = font.render('Game Over!!', True, 'red')
    game_over_rect = game_over_text.get_rect()
    game_over_rect.center = (Width // 2, Height // 2)

    physics_text = font1.render('Physics Fact:', True, 'light grey')
    physics_text_rect = physics_text.get_rect()
    physics_text_rect.center = (Width // 2, Height // 2 - 150)

    screen.blit(physics_text, physics_text_rect)

    lines = randomfact.split("\n")
    line_height = font1.get_height()

    for i, line in enumerate(lines):
        fact_text = font1.render(line.center(1500), True, 'white')
        fact_text_rect = fact_text.get_rect()
        fact_text_rect.center = (Width // 2, Height // 2 - 100 + i * line_height)
        screen.blit(fact_text, fact_text_rect)

    # fact_text = font1.render(randomfact.center(1500), True, 'white')
    # fact_text_rect = fact_text.get_rect()
    # fact_text_rect.center = (Width // 2, Height // 2 - 100)

    screen.blit(game_over_text, game_over_rect)
    # screen.blit(fact_text, fact_text_rect)

    p = pygame.draw.rect(screen, (149, 39, 39), (Width // 2 - 150, Height // 2 + 100, 100, 50))
    q = pygame.draw.rect(screen, (149, 39, 39), (Width // 2 + 50, Height // 2 + 100, 100, 50))

    play_text = font.render("Play", True, "pink")
    play_text_rect = play_text.get_rect()
    play_text_rect.center = p.center

    quit_text = font.render("Quit", True, "pink")
    quit_text_rect = quit_text.get_rect()
    quit_text_rect.center = q.center

    screen.blit(play_text, play_text_rect)
    screen.blit(quit_text, quit_text_rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_q:
                pygame.quit()
                exit()
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1 and p.collidepoint(event.pos):
                m = 0
                score = 0
                player_rect.y = Height - new_player_image.get_height()
                initcollectibles()
            if event.button == 1 and q.collidepoint(event.pos):
                pygame.quit()
                exit()

    pygame.display.update()

class Collectible():
    def __init__(self, image_name, score_boost, iscone):
        self.image_name = image_name
        self.score_boost = score_boost
        self.iscone = iscone
        self.rect = None

for i in range(1, 5):
    image_name = "player-run-" + str(i) + ".png"
    player_image = pygame.image.load(asset_path(image_name))
    new_player_image = pygame.transform.scale(player_image, (72, 90))
    player_rect = new_player_image.get_rect()
    player_rect.centerx = Width//2
    player_rect.y = player_y = Height - new_player_image.get_height()
    anime_run.append(new_player_image)

for i in range(1, 3):
    image_name = "player-jump-" + str(i) + ".png"
    player_image = pygame.image.load(asset_path(image_name))
    new_player_image = pygame.transform.scale(player_image, (72, 90))
    player_rect = new_player_image.get_rect()
    player_rect.centerx = Width//2
    player_rect.y = player_y = Height - new_player_image.get_height()
    anime_jump.append(new_player_image)

def initcollectibles():
    global collectibles
    collectibles = []
    for i in range(num_collectibles):
        chance = random.randint(1, 100)
        if chance <= 40:
            energy = Collectible("energy.png", 10, False)
            collectibles.append(energy)
        elif chance > 40:
            cone = Collectible("cone.png", -10, True)
            collectibles.append(cone)

    space = random.randint(25, 100)

    for i in range(len(collectibles)):
        collect_image = pygame.image.load(asset_path(collectibles[i].image_name))
        collectibles[i].rect = collect_image.get_rect()
        collectibles[i].rect.x = Width + space
        ground = random.randint(0, 1)
        if collectibles[i].iscone:
            collectibles[i].rect.y = Height - collect_image.get_height()
        else:
            collectibles[i].rect.y = Height - collect_image.get_height() - 100 * ground
        space += random.randint(250, 350)

initcollectibles()

font = pygame.font.Font(asset_path("Ankh.otf"), 32)
font1 = pygame.font.Font(asset_path("Ankh.otf"), 24)
font2 = pygame.font.Font(asset_path("Ankh.otf"), 40)

scroll = 0
collectable_scroll = 7
count = 0
jump_count = 0
y_velocity = 0
jump_velocity = -15
gravity = 0.9
y_speed = -5

tiles = math.ceil(Width / bg_width) + 1

is_jumping = False

pygame.mixer.music.load(asset_path("song.wav"))
pygame.mixer.music.play(-1, 0.0)

loss_sound = pygame.mixer.Sound(asset_path("Loss.wav"))
collect_sound = pygame.mixer.Sound(asset_path("collect.wav"))

while True:
    clock.tick(fps)

    if m == 1:
        game_over_menu()

    if m == 2:
        starting_menu()

    if m == 0:
        if collectibles[num_collectibles - 1].rect.x < - collectibles[num_collectibles - 1].rect.width:
            initcollectibles()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    if not is_jumping:
                        is_jumping = True
                        jump_count = 0
                        y_velocity = jump_velocity
                if event.key == K_q:
                    pygame.quit()
                    exit()
                if event.key == K_ESCAPE:
                    m = 2
                    score = 0
                    player_rect.y = player_y
                    is_jumping = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    if not is_jumping:
                        is_jumping = True
                        jump_count = 0
                        y_velocity = jump_velocity

        score_text = font2.render('Score: ' + str(score), True, (1, 50, 24))
        score_text_rect = score_text.get_rect()
        score_text_rect = (10, 10)

        high_score_text = font2.render('High Score: ' + str(high_score), True, 'dark red')
        high_score_rect = score_text.get_rect()
        high_score_rect = (1150, 10)
       
        for i in range(0, tiles):
            screen.blit(bg, (i * bg_width + scroll, 0))

        score += 1
        high_score = max(score, high_score)
        data[name] = high_score
        with open(DATA_FILE, "w") as file:
            json.dump(data, file, indent=4)

        # save_high_score(high_score)

        if abs(scroll) > bg_width:
            scroll = 0

        if score <= 750:
            scroll -= 7
        elif score <= 1500:
            scroll -= 8
        elif score <= 2250:
            scroll -= 9
        elif score > 2250:
            scroll -= 10

        if score <= 750:
            collectable_scroll = 7
        elif score <= 1500:
            collectable_scroll = 8
        elif score <= 2250:
            collectable_scroll = 9
        elif score > 2250:
            collectable_scroll = 10
               
        if is_jumping:
            player_rect.y += y_velocity
            y_velocity += gravity

            if jump_count <= 3:
                screen.blit(anime_jump[0], player_rect)
            elif jump_count > 3:
                screen.blit(anime_jump[1], player_rect)

            jump_count += 1
        else:
            if count % 4 == 0:
                screen.blit(anime_run[0], player_rect)
            elif count % 4 == 1:
                screen.blit(anime_run[1], player_rect)
            elif count % 4 == 2:
                screen.blit(anime_run[2], player_rect)
            elif count % 4 == 3:
                screen.blit(anime_run[3], player_rect)
           
            count += 1

        for i in range(len(collectibles)):
            collect_image = pygame.image.load(asset_path(collectibles[i].image_name))
            screen.blit(collect_image, (collectibles[i].rect.x, collectibles[i].rect.y))
            collectibles[i].rect.x -= collectable_scroll
            # collectibles[i].rect.y += y_speed
            # if collectibles[i].rect.bottom > Height:
            #     collectibles[i].rect.bottom = Height
            #     y_speed = -5
            # if collectibles[i].rect.y <= 400:
            #     y_speed = 5

        for collectible in collectibles:
            if collectible.rect.colliderect(player_rect) and collectible.iscone:
                m = 1
                collectible.rect.y += 200
                score += collectible.score_boost
                loss_sound.play()
            elif collectible.rect.colliderect(player_rect) and collectible.iscone == False:
                score += collectible.score_boost
                collectible.rect.y += 200
                collect_sound.play()
       
        if player_rect.bottom > Height:
            player_rect.bottom = Height
            is_jumping = False
            jump_count = 0

        screen.blit(score_text, score_text_rect)
        screen.blit(high_score_text, high_score_rect)

        pygame.display.update()