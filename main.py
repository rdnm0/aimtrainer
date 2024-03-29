import pygame
import sys
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Aim Trainer")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

circle_radius = 30
score = 0
clock = pygame.time.Clock()

accuracy = 0
clicks = 0

running = True

def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    text_rect.center = (x, y)
    surface.blit(text_obj, text_rect)

def generate_circle_position():
    x = random.randint(circle_radius, WIDTH - circle_radius)
    y = random.randint(circle_radius, HEIGHT - circle_radius)
    return x, y

def game_loop(time_limit):
    global score, clicks, accuracy
    score = 0
    clicks = 0
    accuracy = 0
    start_time = pygame.time.get_ticks()

    circle_x, circle_y = generate_circle_position()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                dist = ((circle_x - mouse_pos[0]) ** 2 + (circle_y - mouse_pos[1]) ** 2) ** 0.5
                if dist <= circle_radius:
                    score += 1
                clicks += 1
                accuracy = round((score / clicks) * 100) if clicks > 0 else 0
                circle_x, circle_y = generate_circle_position()

        screen.fill(WHITE)

        pygame.draw.circle(screen, RED, (circle_x, circle_y), circle_radius)

        font = pygame.font.SysFont(None, 36)
        draw_text("Score: " + str(score), font, BLACK, screen, 100, 50)
        draw_text("Accuracy: " + str(accuracy) + "%", font, BLACK, screen, 700, 50)

        elapsed_time = pygame.time.get_ticks() - start_time
        draw_text("Time Left: " + str(round((time_limit - elapsed_time) / 1000, 2)) + "s", font, BLACK, screen, 400, 50)

        if elapsed_time >= time_limit:
            return True

        pygame.display.flip()

        clock.tick(30)

while running:
    screen.fill(WHITE)
    font = pygame.font.SysFont(None, 36)
    draw_text("Choose a countdown time:", font, BLACK, screen, WIDTH // 2, HEIGHT // 4)

    option_texts = ["10 seconds", "20 seconds", "30 seconds"]
    option_positions = [(WIDTH // 2, HEIGHT // 2 + i * 50) for i in range(3)]

    for text, pos in zip(option_texts, option_positions):
        draw_text(text, font, BLACK, screen, *pos)

    pygame.display.flip()

    chosen = False
    while not chosen:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                for i, pos in enumerate(option_positions):
                    if pos[0] - 100 < mouse_pos[0] < pos[0] + 100 and pos[1] - 25 < mouse_pos[1] < pos[1] + 25:
                        chosen = True
                        if i == 0:
                            time_limit = 10000
                        elif i == 1:
                            time_limit = 20000
                        elif i == 2:
                            time_limit = 30000

    if game_loop(time_limit):
        draw_text("Time's up! Your final score: " + str(score), font, BLACK, screen, WIDTH // 2, HEIGHT // 2)
        pygame.display.flip()
        pygame.time.wait(3000)  
    else:
        break

pygame.quit()
sys.exit()
