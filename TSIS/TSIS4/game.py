# game.py
import pygame
import random
import sys
import json
import os
import db
from config import *

class SnakeGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Advanced Snake (TSIS 4)")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Arial", 20)
        self.big_font = pygame.font.SysFont("Arial", 40)
        
        db.init_db()
        self.load_settings()
        
        self.state = "MENU" # MENU, PLAYING, GAME_OVER, LEADERBOARD, SETTINGS
        self.username = ""
        self.personal_best = 0
        self.reset_game()

    def load_settings(self):
        self.settings = {"snake_color": GREEN, "grid": True, "sound": False}
        if os.path.exists("settings.json"):
            try:
                with open("settings.json", "r") as f:
                    data = json.load(f)
                    self.settings.update(data)
            except: pass

    def save_settings(self):
        with open("settings.json", "w") as f:
            json.dump(self.settings, f)

    def reset_game(self):
        self.snake = [(10, 10), (10, 11)]
        self.direction = (0, -1)
        self.score = 0
        self.level = 1
        self.speed = INITIAL_FPS
        
        # Объекты на карте
        self.food = [] # Список еды (pos, type, expiry)
        self.powerups = [] # Список бонусов (pos, type, expiry)
        self.obstacles = [] # Стены
        
        # Активные эффекты
        self.active_powerup = None
        self.powerup_end_time = 0
        self.shield_active = False
        
        self.generate_food()

    def generate_obstacles(self):
        self.obstacles = []
        if self.level >= 3:
            num_blocks = self.level * 2
            for _ in range(num_blocks):
                x = random.randint(0, WIDTH - 1)
                y = random.randint(0, HEIGHT - 1)
                # Избегаем появления на змейке и в радиусе головы
                if (x, y) not in self.snake and abs(self.snake[0][0] - x) > 2 and abs(self.snake[0][1] - y) > 2:
                    self.obstacles.append((x, y))

    def generate_food(self):
        # Удаляем старую еду
        self.food = [f for f in self.food if f[2] > pygame.time.get_ticks() or f[2] == 0]
        
        if len(self.food) < 2:
            x, y = self.get_empty_pos()
            rand = random.random()
            if rand < 0.15: # 15% Яд
                self.food.append(((x, y), 'poison', pygame.time.get_ticks() + 6000))
            elif rand < 0.35: # 20% Золотая
                self.food.append(((x, y), 'special', pygame.time.get_ticks() + 4000))
            else: # 65% Обычная
                self.food.append(((x, y), 'normal', 0)) # 0 = не исчезает

    def generate_powerup(self):
        if len(self.powerups) == 0 and random.random() < 0.05: # Маленький шанс каждый кадр
            x, y = self.get_empty_pos()
            ptype = random.choice(['speed', 'slow', 'shield'])
            self.powerups.append(((x, y), ptype, pygame.time.get_ticks() + 8000))

    def get_empty_pos(self):
        while True:
            x = random.randint(0, WIDTH - 1)
            y = random.randint(0, HEIGHT - 1)
            pos = (x, y)
            if pos not in self.snake and pos not in self.obstacles:
                return pos

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
                
            if self.state == "MENU":
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN and self.username.strip():
                        self.personal_best = db.get_personal_best(self.username)
                        self.reset_game()
                        self.state = "PLAYING"
                    elif event.key == pygame.K_BACKSPACE:
                        self.username = self.username[:-1]
                    elif event.unicode.isprintable():
                        self.username += event.unicode
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.check_menu_clicks(event.pos)

            elif self.state == "PLAYING":
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and self.direction != (0, 1): self.direction = (0, -1)
                    elif event.key == pygame.K_DOWN and self.direction != (0, -1): self.direction = (0, 1)
                    elif event.key == pygame.K_LEFT and self.direction != (1, 0): self.direction = (-1, 0)
                    elif event.key == pygame.K_RIGHT and self.direction != (-1, 0): self.direction = (1, 0)

            elif self.state in ["GAME_OVER", "LEADERBOARD", "SETTINGS"]:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    self.state = "MENU"
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.check_other_clicks(event.pos)

    def check_menu_clicks(self, pos):
        # Простая проверка кликов по координатам (упрощенно для примера)
        if 200 <= pos[1] <= 240: # Таблица лидеров
            self.state = "LEADERBOARD"
        elif 260 <= pos[1] <= 300: # Настройки
            self.state = "SETTINGS"

    def check_other_clicks(self, pos):
        if self.state == "GAME_OVER":
            if 300 <= pos[1] <= 340: # Retry
                self.reset_game()
                self.state = "PLAYING"
            elif 360 <= pos[1] <= 400: # Menu
                self.state = "MENU"
        elif self.state == "SETTINGS":
            if 150 <= pos[1] <= 190: self.settings["grid"] = not self.settings["grid"]
            elif 210 <= pos[1] <= 250:
                # Меняем цвет по кругу
                colors = [GREEN, BLUE, PURPLE, WHITE]
                try: idx = colors.index(tuple(self.settings["snake_color"]))
                except: idx = 0
                self.settings["snake_color"] = colors[(idx + 1) % len(colors)]
            elif 350 <= pos[1] <= 390:
                self.save_settings()
                self.state = "MENU"

    def update(self):
        if self.state != "PLAYING": return

        current_time = pygame.time.get_ticks()
        
        # Очистка просроченной еды и бонусов
        self.food = [f for f in self.food if f[2] == 0 or f[2] > current_time]
        self.powerups = [p for p in self.powerups if p[2] > current_time]
        
        if not self.food: self.generate_food()
        self.generate_powerup()

        # Сброс эффекта бонуса
        if self.active_powerup and current_time > self.powerup_end_time:
            self.active_powerup = None
            self.speed = INITIAL_FPS + (self.level * 2)

        # Движение
        head_x, head_y = self.snake[0]
        new_head = (head_x + self.direction[0], head_y + self.direction[1])

        # Столкновения
        wall_collision = (new_head[0] < 0 or new_head[0] >= WIDTH or new_head[1] < 0 or new_head[1] >= HEIGHT)
        self_collision = new_head in self.snake
        obstacle_collision = new_head in self.obstacles

        if wall_collision or self_collision or obstacle_collision:
            if self.shield_active:
                self.shield_active = False
                # Проходим сквозь стену если щит
                if wall_collision:
                    new_head = (new_head[0] % WIDTH, new_head[1] % HEIGHT)
                elif self_collision or obstacle_collision:
                    return # Игнорируем ход
            else:
                self.game_over()
                return

        self.snake.insert(0, new_head)
        ate_food = False

        # Проверка еды
        for i, f in enumerate(self.food):
            if new_head == f[0]:
                ate_food = True
                if f[1] == 'special': self.score += 3
                elif f[1] == 'poison':
                    self.snake.pop()
                    if len(self.snake) > 1: self.snake.pop()
                    if len(self.snake) <= 1:
                        self.game_over()
                        return
                else: self.score += 1
                
                self.food.pop(i)
                self.check_level_up()
                break

        # Проверка бонусов
        for i, p in enumerate(self.powerups):
            if new_head == p[0]:
                ptype = p[1]
                self.active_powerup = ptype
                self.powerup_end_time = current_time + 5000
                if ptype == 'speed': self.speed += 5
                elif ptype == 'slow': self.speed = max(5, self.speed - 5)
                elif ptype == 'shield': self.shield_active = True
                self.powerups.pop(i)
                break

        if not ate_food:
            self.snake.pop()

    def check_level_up(self):
        new_level = (self.score // 5) + 1
        if new_level > self.level:
            self.level = new_level
            if not self.active_powerup:
                self.speed = INITIAL_FPS + (self.level * 2)
            self.generate_obstacles()

    def game_over(self):
        self.state = "GAME_OVER"
        db.save_score(self.username, self.score, self.level)

    def draw_text(self, text, font, color, x, y, center=False):
        surface = font.render(text, True, color)
        rect = surface.get_rect()
        if center: rect.center = (x, y)
        else: rect.topleft = (x, y)
        self.screen.blit(surface, rect)

    def draw(self):
        self.screen.fill(BACKGROUND_COLOR)

        if self.state == "MENU":
            self.draw_text("SNAKE GAME", self.big_font, GREEN, SCREEN_WIDTH//2, 80, center=True)
            self.draw_text(f"Username: {self.username}_", self.font, WHITE, SCREEN_WIDTH//2, 150, center=True)
            self.draw_text("Press ENTER to Play", self.font, GOLD, SCREEN_WIDTH//2, 180, center=True)
            
            self.draw_text("[ Click to open Leaderboard ]", self.font, BLUE, SCREEN_WIDTH//2, 220, center=True)
            self.draw_text("[ Click to open Settings ]", self.font, GRAY, SCREEN_WIDTH//2, 280, center=True)

        elif self.state == "PLAYING":
            if self.settings.get("grid"):
                for x in range(0, SCREEN_WIDTH, CELL_SIZE):
                    pygame.draw.line(self.screen, (50, 50, 60), (x, 0), (x, SCREEN_HEIGHT))
                for y in range(0, SCREEN_HEIGHT, CELL_SIZE):
                    pygame.draw.line(self.screen, (50, 50, 60), (0, y), (SCREEN_WIDTH, y))

            # Стены
            for obs in self.obstacles:
                rect = pygame.Rect(obs[0]*CELL_SIZE, obs[1]*CELL_SIZE, CELL_SIZE, CELL_SIZE)
                pygame.draw.rect(self.screen, GRAY, rect)

            # Еда
            for f in self.food:
                color = RED if f[1] == 'normal' else GOLD if f[1] == 'special' else DARK_RED
                rect = pygame.Rect(f[0][0]*CELL_SIZE, f[0][1]*CELL_SIZE, CELL_SIZE, CELL_SIZE)
                pygame.draw.rect(self.screen, color, rect)

            # Бонусы
            for p in self.powerups:
                color = BLUE if p[1] == 'speed' else CYAN if p[1] == 'slow' else PURPLE
                pygame.draw.circle(self.screen, color, (p[0][0]*CELL_SIZE + CELL_SIZE//2, p[0][1]*CELL_SIZE + CELL_SIZE//2), CELL_SIZE//2 - 2)

            # Змейка
            snake_color = tuple(self.settings.get("snake_color", GREEN))
            for i, segment in enumerate(self.snake):
                rect = pygame.Rect(segment[0]*CELL_SIZE, segment[1]*CELL_SIZE, CELL_SIZE-1, CELL_SIZE-1)
                pygame.draw.rect(self.screen, snake_color if not self.shield_active else PURPLE, rect)

            # Интерфейс
            self.draw_text(f"User: {self.username} | Score: {self.score} | Lvl: {self.level} | Best: {max(self.score, self.personal_best)}", self.font, WHITE, 10, 10)

        elif self.state == "GAME_OVER":
            self.draw_text("GAME OVER", self.big_font, RED, SCREEN_WIDTH//2, 100, center=True)
            self.draw_text(f"Score: {self.score}   Level: {self.level}", self.font, WHITE, SCREEN_WIDTH//2, 180, center=True)
            self.draw_text("[ Click here to Retry ]", self.font, GREEN, SCREEN_WIDTH//2, 320, center=True)
            self.draw_text("[ Click here for Menu ]", self.font, GRAY, SCREEN_WIDTH//2, 380, center=True)

        elif self.state == "LEADERBOARD":
            self.draw_text("TOP 10 PLAYERS", self.big_font, GOLD, SCREEN_WIDTH//2, 50, center=True)
            top = db.get_top_10()
            y = 120
            for i, row in enumerate(top):
                self.draw_text(f"{i+1}. {row[0]} - Score: {row[1]} (Lvl {row[2]})", self.font, WHITE, 50, y)
                y += 30
            self.draw_text("Press ESC to return", self.font, GRAY, SCREEN_WIDTH//2, SCREEN_HEIGHT - 30, center=True)

        elif self.state == "SETTINGS":
            self.draw_text("SETTINGS", self.big_font, WHITE, SCREEN_WIDTH//2, 50, center=True)
            self.draw_text(f"1. Grid Overlay: {'ON' if self.settings.get('grid') else 'OFF'} (Click to toggle)", self.font, WHITE, 50, 150)
            self.draw_text(f"2. Snake Color (Click to change)", self.font, tuple(self.settings.get('snake_color', GREEN)), 50, 210)
            self.draw_text("[ Click to Save & Back ]", self.font, GREEN, SCREEN_WIDTH//2, 370, center=True)

        pygame.display.flip()

    def run(self):
        while True:
            self.handle_events()
            self.update()
            self.draw()
            # Если игра не идет, держим стабильные 15 FPS для меню, иначе скорость змейки
            self.clock.tick(self.speed if self.state == "PLAYING" else 15)