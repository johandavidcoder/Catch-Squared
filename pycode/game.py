import pygame
import random
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Catch the Squares")

BG_COLOR = (18, 18, 24)
PLAYER_COLOR = (0, 245, 255)
GOOD_COLOR = (255, 46, 99)
BAD_COLOR = (255, 159, 67)
TEXT_COLOR = (240, 240, 240)
SHADOW_COLOR = (10, 10, 15)

PLAYER_WIDTH = 120
PLAYER_HEIGHT = 15
player_x = WIDTH // 2 - PLAYER_WIDTH // 2
player_y = HEIGHT - 60
player_speed = 10

enemy_width = 40
enemy_height = 40
enemy_speed = 6
enemies = []

score = 0
clock = pygame.time.Clock()

try:
    font = pygame.font.SysFont("Verdana", 28, bold=True)
    score_font = pygame.font.SysFont("Verdana", 24)
except:
    font = pygame.font.Font(None, 36)
    score_font = pygame.font.Font(None, 30)

game_over = False

def draw_text(text, font, color, surface, x, y, center=False):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    if center:
        textrect.center = (x, y)
    else:
        textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def reset_game():
    global player_x, enemies, score, game_over
    player_x = WIDTH // 2 - PLAYER_WIDTH // 2
    enemies = []
    score = 0
    game_over = False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r and game_over:
                reset_game()

    if not game_over:
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and player_x > 0:
            player_x -= player_speed
        if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and player_x < WIDTH - PLAYER_WIDTH:
            player_x += player_speed

        if random.randint(1, 40) == 1:
            e_x = random.randint(20, WIDTH - enemy_width - 20)
            e_y = -enemy_height
            e_type = 0 if random.random() > 0.4 else 1 
            enemies.append([e_x, e_y, e_type])

        for enemy in enemies[:]:
            enemy[1] += enemy_speed
            
            player_rect = pygame.Rect(player_x, player_y, PLAYER_WIDTH, PLAYER_HEIGHT)
            enemy_rect = pygame.Rect(enemy[0], enemy[1], enemy_width, enemy_height)

            if player_rect.colliderect(enemy_rect):
                if enemy[2] == 0: 
                    score += 1
                    enemies.remove(enemy)
                else:
                    game_over = True
            elif enemy[1] > HEIGHT:
                enemies.remove(enemy)

    screen.fill(BG_COLOR)

    pygame.draw.line(screen, (40, 40, 50), (0, player_y + PLAYER_HEIGHT + 10), (WIDTH, player_y + PLAYER_HEIGHT + 10), 2)

    pygame.draw.rect(screen, PLAYER_COLOR, (player_x, player_y, PLAYER_WIDTH, PLAYER_HEIGHT), border_radius=8)
    
    for enemy in enemies:
        color = GOOD_COLOR if enemy[2] == 0 else BAD_COLOR
        pygame.draw.rect(screen, color, (enemy[0], enemy[1], enemy_width, enemy_height), border_radius=6)

    draw_text(f"SCORE: {score}", score_font, TEXT_COLOR, screen, 20, 20)

    if game_over:
        overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 180))
        screen.blit(overlay, (0,0))
        
        draw_text("GAME OVER", font, GOOD_COLOR, screen, WIDTH // 2, HEIGHT // 2 - 40, center=True)
        draw_text("PRESS 'R' TO RESTART", score_font, TEXT_COLOR, screen, WIDTH // 2, HEIGHT // 2 + 10, center=True)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
