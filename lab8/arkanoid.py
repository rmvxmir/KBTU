import pygame 
import random

# Initialize
pygame.init()

# InGame Variables
W, H = 1200, 800
FPS = 60

screen = pygame.display.set_mode((W, H), pygame.RESIZABLE)
pygame.display.set_caption('ARKANOID')
clock = pygame.time.Clock()
bg = (0, 0, 0)

# Paddle
paddleW = 150
min_paddleW = 50
paddleH = 25
paddleSpeed = 20
paddle = pygame.Rect(W // 2 - paddleW // 2, H - paddleH - 30, paddleW, paddleH)

# Ball
ballRadius = 20
ballSpeed = 6
max_ballSpeed = 12
ball_rect = int(ballRadius * 2 ** 0.5)
ball = pygame.Rect(random.randrange(ball_rect, W - ball_rect), H // 2, ball_rect, ball_rect)
dx, dy = 1, -1

# Game score
game_score = 0
game_score_fonts = pygame.font.Font(None, 40)
game_score_text = game_score_fonts.render(f'Score: {game_score}', True, (0, 0, 0))
game_score_rect = game_score_text.get_rect()
game_score_rect.center = (70, 20)

# Catching sound
collision_sound = pygame.mixer.Sound('lab8/materials/catch.mp3')

def detect_collision(dx, dy, ball, rect):
    if dx > 0:
        delta_x = ball.right - rect.left
    else:
        delta_x = rect.right - ball.left
    if dy > 0:
        delta_y = ball.bottom - rect.top
    else:
        delta_y = rect.bottom - ball.top

    if abs(delta_x - delta_y) < 10:
        dx, dy = -dx, -dy
    if delta_x > delta_y:
        dy = -dy
    elif delta_y > delta_x:
        dx = -dx
    return dx, dy

# Block settings
color_list = []
for i in range(40):  # 10 blocks per row, 4 rows
    color = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
    
    # Append white color tuple with 20% probability
    if random.random() < 0.2:
        color_list.append((255, 255, 255))
    else:
        color_list.append(color)

block_list = [pygame.Rect(10 + 120 * (i % 10), 50 + 70 * (i // 10),
        100, 50) for i in range(40)]

# Game over Screen
losefont = pygame.font.Font(None, 60)
losetext = losefont.render('Game Over!', True, (255, 255, 255))
losetextRect = losetext.get_rect()
losetextRect.center = (W // 2, H // 2)

# Win Screen
winfont = pygame.font.Font(None, 60)
wintext = losefont.render('You win!', True, (0, 0, 0))
wintextRect = wintext.get_rect()
wintextRect.center = (W // 2, H // 2)

# Adding user events
inc_ball_speed = pygame.USEREVENT + 1
pygame.time.set_timer(inc_ball_speed, 1000)

shrink_paddle = pygame.USEREVENT + 2
pygame.time.set_timer(shrink_paddle, 2000)

# Main Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == inc_ball_speed:
            if ballSpeed < max_ballSpeed:
                ballSpeed += 0.25
        if event.type == shrink_paddle:
            if paddle.width > min_paddleW:
                paddle.width -= 5

    screen.fill(bg)
    
    # Drawing Blocks
    [pygame.draw.rect(screen, color_list[color], block)
     for color, block in enumerate (block_list)]
    pygame.draw.rect(screen, pygame.Color(255, 255, 255), paddle)
    pygame.draw.circle(screen, pygame.Color(255, 0, 0), ball.center, ballRadius)

    # Ball movement
    ball.x += ballSpeed * dx
    ball.y += ballSpeed * dy

    # Collision left 
    if ball.centerx < ballRadius or ball.centerx > W - ballRadius:
        dx = -dx

    # Collision top
    if ball.centery < ballRadius + 50: 
        dy = -dy

    # Collision with paddle
    if ball.colliderect(paddle) and dy > 0:
        dx, dy = detect_collision(dx, dy, ball, paddle)

    #Collision blocks
    hitIndex = ball.collidelist(block_list)

    if hitIndex != -1:
        hitRect = block_list[hitIndex]
        dx, dy = detect_collision(dx, dy, ball, hitRect)
        collision_sound.play()
        if color_list[hitIndex] != (255, 255, 255):
            block_list.pop(hitIndex)
            color_list.pop(hitIndex)
            game_score += 1
        
    # Game score
    game_score_text = game_score_fonts.render(f'Score: {game_score}', True, (255, 255, 255))
    screen.blit(game_score_text, game_score_rect)
    
    # Win/lose screens
    if ball.bottom > H:
        screen.fill((0, 0, 0))
        screen.blit(losetext, losetextRect)
    elif not len(block_list):
        screen.fill((255, 255, 255))
        screen.blit(wintext, wintextRect)

    #Paddle Control
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and paddle.left > 0:
        paddle.left -= paddleSpeed
    if key[pygame.K_RIGHT] and paddle.right < W:
        paddle.right += paddleSpeed

    pygame.display.flip()
    clock.tick(FPS)

'''
There are 3 perks: bonus ball, wide paddle and invincibility. ! Undone !
White bricks are considered as unbreakable.
'''