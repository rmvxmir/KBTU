# Imports
import pygame
import random
from pygame.locals import *
from time import sleep

# Initialize
pygame.init()

# InGame Variables
FPS = 60
clock = pygame.time.Clock()

screen_width = 400
screen_height = 600
score = 0
speed = 5
coins_amount = 0
coin_speed = 5

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
dark_red = (70, 0, 0)

# Setting up display
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('RACER')

font = pygame.font.Font(None, 60)
score_font = pygame.font.Font(None, 30)
coin_font = pygame.font.Font(None, 30)
game_over_font = font.render('Game Over!', True, black)

background_image = pygame.image.load('lab8/materials/background.png')
background = pygame.transform.scale(background_image, (400, 600))

# Player mechanic
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('lab8/materials/player.png')
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < screen_width:     
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)

# Enemy mechanic
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('lab8/materials/enemy.png')
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, screen_width - 40), 0)
    def move(self):
        global score
        self.rect.move_ip(0, speed)
        if self.rect.top > 600:
            score += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, screen_width - 40), 0)

# Coin mechanic
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.coin_type = random.choices(['goldencoin', 'silvercoin', 'bronzecoin'], weights=[0.2, 0.3, 0.5])[0] # Adding different coin types
        self.coin_image = pygame.image.load(f'lab8/materials/{self.coin_type}.png')
        self.image = pygame.transform.scale(self.coin_image, (30, 30))
        self.rect = self.image.get_rect()
        self.respawn()
    def respawn(self):
        self.rect.center = (random.randint(40, screen_width - 40), 0)
    def move(self):
        self.rect.move_ip(0, coin_speed)
        if (self.rect.top > 600):
            self.respawn()

# Setting up sprites
P = Player()
E = Enemy()

enemies = pygame.sprite.Group()
enemies.add(E)

all_sprites = pygame.sprite.Group()
all_sprites.add(P)
all_sprites.add(E)

coins = pygame.sprite.Group()

# Adding user event
inc_speed = pygame.USEREVENT + 1
pygame.time.set_timer(inc_speed, 1500)

# Main Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == inc_speed:
            speed += 0.5

    screen.blit(background, (0, 0))
    points = score_font.render('Score: ' + str(score), True, black)
    screen.blit(points, (10, 10))

    # Preventing many coins from appearing
    if len(coins) < 1:
        if random.random() < 0.2: # 20% Chance
            new_coin = Coin()
            coins.add(new_coin)
            all_sprites.add(new_coin)

    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)
        entity.move()

    coins_collected = coin_font.render('Coins: ' + str(coins_amount), True, black)
    screen.blit(coins_collected, (10, 40))

    # Coin collecting
    for coin in coins:
        if pygame.sprite.collide_rect(P, coin):
            coin.kill()
            if coin.coin_type == 'goldencoin':
                coins_amount += 5
            elif coin.coin_type == 'silvercoin':
                coins_amount += 3
            else:
                coins_amount += 1
            pygame.mixer.Sound('lab8/materials/coin_collected.mp3').play()
            if coins_amount > 0 and coins_amount % 10 == 0:
                speed += 1.5

    # Enemy collide
    if pygame.sprite.spritecollideany(P, enemies):
        pygame.mixer.Sound('lab8/materials/lost.mp3').play()
        sleep(1.1)

        screen.fill(dark_red)
        screen.blit(game_over_font, (80, 250))

        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        sleep(2)
        pygame.quit()

    pygame.display.update()
    clock.tick(FPS)
# Code end