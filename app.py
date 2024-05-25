## Import nesseasry libraries
import pygame
import random

# Initialize Pygame
pygame.init() # This starts Pygame, which allows us to create the game window and interact with things like the keyboard and mouse

# Screen dimensions
WIDTH, HEIGHT = 800, 600 # This sets the width and height of the game window in pixels

# Colors (didn't use all of them)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
LIGHT_BLUE = (173, 216, 230)
BLUE = (0, 0, 255)
DARK_BLUE = (0, 0, 139)
LIGHT_GREEN = (144, 238, 144)
GREEN = (0, 255, 0)
DARK_GREEN = (0, 128, 0)
BROWN = (139, 69, 19)

# Paddle dimensions these define the size of the player and AI paddles
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100

# Ball dimensions how fast the paddles can move
BALL_SIZE = 10

# Paddle speed
PADDLE_SPEED = 5

# Ball speed
BALL_SPEED_X, BALL_SPEED_Y = 5, 5

# Fonts
SCORE_FONT = pygame.font.Font(None, 74)
NAME_FONT = pygame.font.Font(None, 36)
TITLE_FONT = pygame.font.Font(None, 50)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("EMAI611 - KAU Pong League")

# Paddle positions
player_paddle = pygame.Rect(WIDTH - 20, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
ai_paddle = pygame.Rect(10, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)

# Ball position
ball = pygame.Rect(WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)

# Scores (these keep track of the player and AI scores)
player_score = 0
ai_score = 0

# Clock
clock = pygame.time.Clock()

# Main game loop  /this keeps the game running until the player quits
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get keys pressess keyboard
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and player_paddle.top > 0:
        player_paddle.y -= PADDLE_SPEED
    if keys[pygame.K_DOWN] and player_paddle.bottom < HEIGHT:
        player_paddle.y += PADDLE_SPEED

    # AI movement
    if ai_paddle.centery < ball.centery:
        ai_paddle.y += PADDLE_SPEED
    if ai_paddle.centery > ball.centery:
        ai_paddle.y -= PADDLE_SPEED

    # Ball movement
    ball.x += BALL_SPEED_X
    ball.y += BALL_SPEED_Y

    # Ball collision with top and bottom
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        BALL_SPEED_Y *= -1

    # Ball collision with paddles
    if ball.colliderect(player_paddle) or ball.colliderect(ai_paddle):
        BALL_SPEED_X *= -1

    # Ball out of bounds
    if ball.left <= 0:
        player_score += 1
        ball.x = WIDTH // 2 - BALL_SIZE // 2
        ball.y = HEIGHT // 2 - BALL_SIZE // 2
        BALL_SPEED_X *= -1
    if ball.right >= WIDTH:
        ai_score += 1
        ball.x = WIDTH // 2 - BALL_SIZE // 2
        ball.y = HEIGHT // 2 - BALL_SIZE // 2
        BALL_SPEED_X *= -1

    # Clear screen
    screen.fill(BROWN)

    # Draw paddles
    pygame.draw.rect(screen, LIGHT_GREEN, player_paddle)
    pygame.draw.rect(screen, DARK_GREEN, ai_paddle)

    # Draw ball
    pygame.draw.ellipse(screen, WHITE, ball)

    # Draw score box border
    pygame.draw.rect(screen, WHITE, (WIDTH // 2 - 150, 10, 300, 80), 2)

    # Draw scores and player names
    player_name = NAME_FONT.render("Player", True, WHITE)
    ai_name = NAME_FONT.render("KAU AI", True, WHITE)
    player_score_text = SCORE_FONT.render(str(player_score), True, WHITE)
    ai_score_text = SCORE_FONT.render(str(ai_score), True, WHITE)
    
    screen.blit(player_name, (WIDTH // 2 + 70, 15))
    screen.blit(ai_name, (WIDTH // 2 - 130, 15))
    screen.blit(player_score_text, (WIDTH // 2 + 60, 40))
    screen.blit(ai_score_text, (WIDTH // 2 - 120, 40))

    # Draw title
    title_text = TITLE_FONT.render("KAU Pong League", True, WHITE)
    screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, HEIGHT - 50))

    # Update screen
    pygame.display.flip()

    # Frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
