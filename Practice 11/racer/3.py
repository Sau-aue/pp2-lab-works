import pygame
import sys
import random
import time
from pygame.locals import *

# --- Константы (без изменений) ---
SCREEN_WIDTH  = 500
SCREEN_HEIGHT = 600
FPS           = 60
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED   = (255, 0, 0)
INITIAL_SPEED = 5
SPEED_INCREMENT = 1.5

# --- Инициализация ---
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock  = pygame.time.Clock()
pygame.display.set_caption("Dodge & Collect")

font_big   = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)

# --- Настройка фона ---
background = pygame.image.load("AnimatedStreet.png")
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Начальные координаты для двух копий фона
bg_y1 = 0
bg_y2 = -SCREEN_HEIGHT

# --- Классы (Player, Enemy, Coin остаются такими же, как у тебя) ---
# ... (вставь сюда свои классы Player, Enemy, Coin без изменений) ...

# (Пример сокращенного класса для работы кода)
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player.png")
        self.rect  = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT - 80)
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[K_LEFT] and self.rect.left > 0: self.rect.x -= 5
        if keys[K_RIGHT] and self.rect.right < SCREEN_WIDTH: self.rect.x += 5

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Enemy.png")
        self.rect  = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
    def move(self, speed, score_ref):
        self.rect.y += speed
        if self.rect.top > SCREEN_HEIGHT:
            score_ref[0] += 1
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.base_image = pygame.image.load("Coin.png")
        self.weight = 1
        self.spawn()
    def spawn(self):
        self.weight = random.randint(1, 3)
        size = 20 + self.weight * 10
        self.image = pygame.transform.scale(self.base_image, (size, size))
        self.rect  = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
    def move(self, speed):
        self.rect.y += speed
        if self.rect.top > SCREEN_HEIGHT: self.spawn()

def draw_hud(surface, dodge_score, coin_score):
    txt_dodge = font_small.render(f"Score: {dodge_score}", True, BLACK)
    txt_coins = font_small.render(f"Coins: {coin_score}",  True, BLACK)
    surface.blit(txt_dodge, (10, 10))
    surface.blit(txt_coins, (SCREEN_WIDTH - 150, 10))

def show_game_over(surface):
    surface.fill(RED)
    label = font_big.render("Game Over", True, BLACK)
    surface.blit(label, (SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 - 50))
    pygame.display.update()
    time.sleep(2)
    pygame.quit()
    sys.exit()

# --- Создание объектов ---
player = Player()
enemy  = Enemy()
coin   = Coin()
enemy_group = pygame.sprite.Group(enemy)
coin_group  = pygame.sprite.Group(coin)
all_sprites = pygame.sprite.Group(player, enemy, coin)

speed = INITIAL_SPEED
dodge_score = [0]
coin_score = 0
speed_threshold = 0

# ─────────────────────────────────────────────
# ГЛАВНЫЙ ИГРОВОЙ ЦИКЛ
# ─────────────────────────────────────────────
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # -- 1. ДВИЖЕНИЕ ФОНА --
    # Смещаем координаты фона вниз со скоростью игры
    bg_y1 += speed
    bg_y2 += speed

    # Если первая картинка ушла за нижний край, переносим её наверх
    if bg_y1 >= SCREEN_HEIGHT:
        bg_y1 = -SCREEN_HEIGHT
    
    # Если вторая картинка ушла за нижний край, переносим её наверх
    if bg_y2 >= SCREEN_HEIGHT:
        bg_y2 = -SCREEN_HEIGHT

    # -- 2. Обновление состояния объектов --
    player.move()
    enemy.move(speed, dodge_score)
    coin.move(speed)

    # -- 3. Проверка коллизий --
    for hit_coin in pygame.sprite.spritecollide(player, coin_group, dokill=False):
        coin_score += hit_coin.weight
        hit_coin.spawn()
        new_threshold = coin_score // 10
        if new_threshold > speed_threshold:
            speed += SPEED_INCREMENT
            speed_threshold = new_threshold

    if pygame.sprite.spritecollideany(player, enemy_group):
        time.sleep(0.5)
        show_game_over(screen)

    # -- 4. Отрисовка --
    # Рисуем две копии фона в их текущих позициях
    screen.blit(background, (0, bg_y1))
    screen.blit(background, (0, bg_y2))

    for sprite in all_sprites:
        screen.blit(sprite.image, sprite.rect)

    draw_hud(screen, dodge_score[0], coin_score)

    pygame.display.update()
    clock.tick(FPS)