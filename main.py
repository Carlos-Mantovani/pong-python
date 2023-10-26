import pygame, sys, random

def ball_animation():
    
    global ball_speed_x, ball_speed_y, player_score, opponent_score

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
    if ball.left <= 0:
        player_score += 1
        ball_restart()
    if ball.right >= screen_width:
        opponent_score += 1
        ball_restart()

    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1
        ball_speed_y *= -1

def ball_restart():
    global ball_speed_x, ball_speed_y
    ball.center = (screen_width / 2, screen_height / 2)
    ball_speed_y *= random.choice((1, -1))
    ball_speed_x *= random.choice((1, -1))

def player_animation():
    player.y += player_speed

    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height

def opponent_ai():
    if opponent.top < ball.y:
        opponent.y += opponent_speed
    if opponent.bottom > ball.y:
        opponent.y -= opponent_speed

    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height

pygame.init()
clock = pygame.time.Clock()

screen_width = 1280
screen_height = 720

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pong')

ball_size = 30
ball = pygame.Rect(screen_width/2 - ball_size/2,screen_height/2 - ball_size/2, ball_size, ball_size)

player_width = 10
player_height = 140
player = pygame.Rect(screen_width - 20, screen_height/2 - player_height/2, player_width, player_height)
opponent = pygame.Rect(20 - player_width, screen_height/2 - player_height/2, player_width, player_height)

bg_color = pygame.Color('grey12')
lightgrey = (200, 200, 200)

ball_speed_x = 7 * random.choice((1, -1))
ball_speed_y = 7 * random.choice((1, -1))
player_speed = 0
opponent_speed = 7

player_score = 0
opponent_score = 0
game_font = pygame.font.Font('freesansbold.ttf', 32)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += 7
            if event.key == pygame.K_UP:
                player_speed -= 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= 7
            if event.key == pygame.K_UP:
                player_speed += 7

    ball_animation()
    player_animation()
    opponent_ai()
    
    screen.fill(bg_color)
    pygame.draw.rect(screen, lightgrey, player)
    pygame.draw.rect(screen, lightgrey, opponent)
    pygame.draw.rect(screen, lightgrey, ball)
    pygame.draw.aaline(screen, lightgrey, (screen_width / 2, 0), (screen_width / 2, screen_height))

    player_text = game_font.render(f'{player_score}', False, lightgrey)
    screen.blit(player_text, (660, 360))

    opponent_text = game_font.render(f'{opponent_score}', False, lightgrey)
    screen.blit(opponent_text, (600, 360))

    pygame.display.flip()
    clock.tick(60)
