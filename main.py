import pygame
import sys
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Clicking Game")

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
