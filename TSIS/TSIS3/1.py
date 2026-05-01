import pygame
import sys
import random
import time
import json
import os
from pygame.locals import *

# Инициализация
pygame.init()
pygame.mixer.init()

# ================= Настройки и Константы =================
FPS = 60
FramePerSec = pygame.time.Clock()
SCREEN_WIDTH, SCREEN_HEIGHT = 500, 800

# Цвета
BLUE, RED, BLACK, WHITE = (0, 0, 255), (255, 0, 0), (0, 0, 0), (255, 255, 255)
GREEN, YELLOW, GRAY, CYAN = (0, 255, 0), (255, 255, 0), (100, 100, 100), (0, 255, 255)
DARK_BLUE = (0, 0, 139)

font_title = pygame.font.SysFont("Verdana", 50, bold=True)
font_large = pygame.font.SysFont("Verdana", 40)
font_medium = pygame.font.SysFont("Verdana", 25)
font_small = pygame.font.SysFont("Verdana", 18)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Ultimate Arcade Racer")

# ================= Вспомогательные функции =================
def load_json(filename, default):
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            try: return json.load(f)
            except: return default
    return default

def save_json(filename, data):
    with open(filename, 'w') as f: json.dump(data, f, indent=4)

def safe_load_image(filename, size, color):
    """Загружает картинку или создает цветной прямоугольник, если файла нет"""
    try:
        img = pygame.image.load(filename).convert_alpha()
        return pygame.transform.scale(img, size)
    except:
        surf = pygame.Surface(size)
        surf.fill(color)
        return surf

# ================= КЭШИРОВАНИЕ РЕСУРСОВ (Убирает фризы) =================
# Загружаем всё заранее, чтобы не читать диск во время игры
settings = load_json("settings.json", {"sound": True, "difficulty": "NORMAL", "car_color": "BLUE"})
leaderboard = load_json("leaderboard.json", [])

IMG_PLAYER_BLUE = safe_load_image("Player.png", (50, 90), BLUE)
IMG_PLAYER_RED = safe_load_image("redcar1.png", (50, 90), RED)
IMG_ENEMY = safe_load_image("Enemy.png", (50, 90), BLACK)
IMG_COIN = safe_load_image("Coin.png", (30, 30), YELLOW)
IMG_BG = safe_load_image("AnimatedStreet.png", (SCREEN_WIDTH, SCREEN_HEIGHT), GRAY)

# Словарь для препятствий
HAZARD_IMAGES = {
    "OIL": safe_load_image("Oil.png", (60, 40), GRAY),
    "POTHOLE": safe_load_image("Pothole.png", (50, 50), BLACK),
    "BARRIER": safe_load_image("barricade.png", (70, 40), RED)
}

# Звуки
crash_sound = None
if os.path.exists("crash.wav"): crash_sound = pygame.mixer.Sound("crash.wav")

def play_bg_music():
    if settings.get("sound", True) and os.path.exists("background.wav"):
        if not pygame.mixer.music.get_busy():
            try:
                pygame.mixer.music.load("background.wav")
                pygame.mixer.music.play(-1)
            except: pass

# ================= Переменные состояния =================
current_speed = 5.0
score, coins, distance = 0, 0, 0.0
player_name, game_state, bg_y = "", "MENU", 0 
active_powerup, powerup_timer, player_lives, has_shield = None, 0, 3, False

# ================= Классы объектов =================
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Берем готовую картинку из кэша
        self.image = IMG_PLAYER_RED if settings.get("car_color") == "RED" else IMG_PLAYER_BLUE
        self.rect = self.image.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 100))
    
    def move(self):
        keys = pygame.key.get_pressed()
        spd = 12 if active_powerup == "NITRO" else 7
        if self.rect.left > 0 and keys[K_LEFT]: self.rect.move_ip(-spd, 0)
        if self.rect.right < SCREEN_WIDTH and keys[K_RIGHT]: self.rect.move_ip(spd, 0)
    
    def draw(self, surface):
        surface.blit(self.image, self.rect)
        if has_shield: 
            pygame.draw.rect(surface, CYAN, self.rect.inflate(10, 10), 3, border_radius=5)

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = IMG_ENEMY
        self.rect = self.image.get_rect()
        self.spawn()
    def spawn(self):
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), random.randint(-500, -50))
    def move(self):
        spd = current_speed * 2 if active_powerup == "NITRO" else current_speed
        self.rect.move_ip(0, int(spd))
        if self.rect.top > SCREEN_HEIGHT: self.spawn()

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = IMG_COIN
        self.rect = self.image.get_rect()
        self.spawn()
    def spawn(self):
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), random.randint(-800, -50))
    def move(self):
        spd = current_speed * 2 if active_powerup == "NITRO" else current_speed
        self.rect.move_ip(0, int(spd))
        if self.rect.top > SCREEN_HEIGHT: self.spawn()

class Hazard(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.spawn()
    def spawn(self):
        self.type = random.choice(["OIL", "POTHOLE", "BARRIER"])
        self.image = HAZARD_IMAGES[self.type] # Берем из кэша, никаких safe_load_image здесь!
        self.rect = self.image.get_rect(center=(random.randint(40, SCREEN_WIDTH-40), random.randint(-1200, -100)))
    def move(self):
        spd = current_speed * 2 if active_powerup == "NITRO" else current_speed
        self.rect.move_ip(0, int(spd))
        if self.rect.top > SCREEN_HEIGHT: self.spawn()

class PowerUp(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.spawn()
    def spawn(self):
        self.type = random.choice(["NITRO", "SHIELD", "REPAIR"])
        self.image = pygame.Surface((30, 30))
        if self.type == "NITRO": self.image.fill(DARK_BLUE)
        elif self.type == "REPAIR": self.image.fill(GREEN)
        else: self.image.fill(CYAN)
        self.rect = self.image.get_rect(center=(random.randint(40, SCREEN_WIDTH-40), random.randint(-2000, -500)))
    def move(self):
        spd = current_speed * 2 if active_powerup == "NITRO" else current_speed
        self.rect.move_ip(0, int(spd))
        if self.rect.top > SCREEN_HEIGHT: self.spawn()

class Button:
    def __init__(self, x, y, width, height, text, color):
        self.rect = pygame.Rect(x, y, width, height)
        self.text, self.color = text, color
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect, border_radius=10)
        t = font_medium.render(self.text, True, WHITE)
        surface.blit(t, t.get_rect(center=self.rect.center))
    def is_clicked(self, pos): return self.rect.collidepoint(pos)

# ================= Группы и логика игры =================
P1 = Player()
enemies, coins_group, hazards, powerups, all_sprites = pygame.sprite.Group(), pygame.sprite.Group(), pygame.sprite.Group(), pygame.sprite.Group(), pygame.sprite.Group()

def reset_game():
    global current_speed, score, coins, distance, active_powerup, player_lives, has_shield, P1, bg_y
    current_speed, score, coins, distance, bg_y = 5.0, 0, 0, 0.0, 0
    active_powerup, player_lives, has_shield = None, 3, False
    all_sprites.empty(); enemies.empty(); coins_group.empty(); hazards.empty(); powerups.empty()
    P1 = Player()
    for _ in range(3): e = Enemy(); enemies.add(e); all_sprites.add(e)
    for _ in range(2): c = Coin(); coins_group.add(c); all_sprites.add(c)
    h = Hazard(); hazards.add(h); all_sprites.add(h)
    p = PowerUp(); powerups.add(p); all_sprites.add(p)

def save_score():
    global leaderboard
    ts = int(score + (coins * 10) + distance)
    leaderboard.append({"name": player_name, "score": ts, "distance": int(distance)})
    leaderboard = sorted(leaderboard, key=lambda x: x["score"], reverse=True)[:10]
    save_json("leaderboard.json", leaderboard)

# Интерфейс
btn_play = Button(150, 200, 200, 50, "Play", BLUE)
btn_lb = Button(150, 280, 200, 50, "Leaderboard", BLUE)
btn_set = Button(150, 360, 200, 50, "Settings", BLUE)
btn_quit = Button(150, 440, 200, 50, "Quit", RED)
btn_retry = Button(150, 400, 200, 50, "Retry", GREEN)
btn_main = Button(150, 480, 200, 50, "Main Menu", BLUE)
btn_back = Button(150, 700, 200, 50, "Back", GRAY)

# ================= ГЛАВНЫЙ ЦИКЛ =================
while True:
    screen.fill(WHITE)
    m_pos = pygame.mouse.get_pos()
    
    for event in pygame.event.get():
        if event.type == QUIT: pygame.quit(); sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            if game_state == "MENU":
                if btn_play.is_clicked(m_pos): game_state = "INPUT_NAME"
                elif btn_lb.is_clicked(m_pos): game_state = "LEADERBOARD"
                elif btn_set.is_clicked(m_pos): game_state = "SETTINGS"
                elif btn_quit.is_clicked(m_pos): pygame.quit(); sys.exit()
            elif game_state in ["LEADERBOARD", "SETTINGS"]:
                if btn_back.is_clicked(m_pos): game_state = "MENU"
                if game_state == "SETTINGS":
                    if 150 < m_pos[1] < 200:
                        opts = ["EASY", "NORMAL", "HARD"]
                        settings["difficulty"] = opts[(opts.index(settings["difficulty"]) + 1) % 3]
                    elif 220 < m_pos[1] < 270:
                        settings["car_color"] = "RED" if settings.get("car_color") == "BLUE" else "BLUE"
                    save_json("settings.json", settings)
            elif game_state == "GAME_OVER":
                if btn_retry.is_clicked(m_pos): reset_game(); play_bg_music(); game_state = "GAME"
                elif btn_main.is_clicked(m_pos): game_state = "MENU"
        
        if event.type == KEYDOWN and game_state == "INPUT_NAME":
            if event.key == K_RETURN and player_name: 
                reset_game(); play_bg_music(); game_state = "GAME"
            elif event.key == K_BACKSPACE: player_name = player_name[:-1]
            elif len(player_name) < 10 and event.unicode.isprintable(): player_name += event.unicode

    if game_state == "MENU":
        screen.blit(font_title.render("ARCADE RACER", True, BLACK), (60, 80))
        btn_play.draw(screen); btn_lb.draw(screen); btn_set.draw(screen); btn_quit.draw(screen)
    
    elif game_state == "INPUT_NAME":
        screen.blit(font_large.render("Enter Name:", True, BLACK), (130, 200))
        screen.blit(font_title.render(player_name + "_", True, BLUE), (150, 300))
    
    elif game_state == "SETTINGS":
        screen.blit(font_medium.render(f"Difficulty: {settings['difficulty']}", True, BLACK), (50, 160))
        screen.blit(font_medium.render(f"Car Color: {settings['car_color']}", True, BLACK), (50, 230))
        btn_back.draw(screen)
    
    elif game_state == "LEADERBOARD":
        for i, e in enumerate(leaderboard):
            screen.blit(font_small.render(f"{i+1}. {e['name']} - {e['score']}", True, BLACK), (50, 120 + i*35))
        btn_back.draw(screen)
    
    elif game_state == "GAME":
        # Скорость с учетом нитро
        eff_speed = current_speed * 2 if active_powerup == "NITRO" else current_speed
        bg_y = (bg_y + int(eff_speed)) % SCREEN_HEIGHT
        screen.blit(IMG_BG, (0, bg_y)); screen.blit(IMG_BG, (0, bg_y - SCREEN_HEIGHT))
        
        distance += eff_speed / 600
        current_speed += 0.0005 # Постепенное ускорение

        if active_powerup == "NITRO" and time.time() > powerup_timer: 
            active_powerup = None
        
        # Движение и отрисовка всех спрайтов
        for entity in all_sprites:
            entity.move()
            screen.blit(entity.image, entity.rect)
        
        P1.move()
        P1.draw(screen)

        # Столкновения (Смерть)
        collision_list = list(enemies) + list(hazards)
        for target in collision_list:
            if P1.rect.colliderect(target.rect):
                if crash_sound and settings.get("sound"): crash_sound.play()
                if has_shield: 
                    has_shield = False
                else:
                    player_lives -= 1
                    current_speed = max(5.0, current_speed - 1.5)
                    if player_lives <= 0: 
                        pygame.mixer.music.stop()
                        save_score()
                        game_state = "GAME_OVER"
                target.spawn()

        # Монеты
        for c in pygame.sprite.spritecollide(P1, coins_group, False): 
            coins += 1; score += 10
            current_speed += 0.1
            c.spawn()
        
        # Бонусы
        for p in pygame.sprite.spritecollide(P1, powerups, False):
            if p.type == "NITRO": 
                active_powerup = "NITRO"
                powerup_timer = time.time() + 5
            elif p.type == "SHIELD": has_shield = True
            elif p.type == "REPAIR": player_lives += 1
            p.spawn()

        # HUD
        txt_color = DARK_BLUE if active_powerup == "NITRO" else BLACK
        info = f"Score: {score} | Coins: {coins} | Lives: {player_lives}"
        if active_powerup == "NITRO":
            info += f" | NITRO: {int(powerup_timer - time.time())}s"
        screen.blit(font_small.render(info, True, txt_color), (10, 10))
    
    elif game_state == "GAME_OVER":
        screen.blit(font_title.render("GAME OVER", True, RED), (110, 150))
        btn_retry.draw(screen); btn_main.draw(screen)

    pygame.display.update()
    FramePerSec.tick(FPS)