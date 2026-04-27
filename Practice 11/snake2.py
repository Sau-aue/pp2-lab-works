import pygame
import random
import sys

# Настройки экрана и игры
CELL_SIZE = 20
WIDTH, HEIGHT = 20, 20  # Размер поля в клетках
SCREEN_WIDTH = WIDTH * CELL_SIZE
SCREEN_HEIGHT = HEIGHT * CELL_SIZE
FPS = 10  # Начальная скорость

# Цвета
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)       # Обычная еда
GOLD = (255, 215, 0)     # Редкая еда (желтый/золотой)
BACKBROUND_COLOR = (40, 40, 50)

class SnakeGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Improved Snake")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Arial", 18)
        
        # Состояние змейки
        self.snake = [(10, 10),(10,11)]
        self.direction = (0, -1)  # Начинаем движение вверх
        self.score = 0
        self.level = 1
        self.speed = FPS
        
        # Данные о еде
        self.food_pos = None      # Позиция (x, y)
        self.food_type = None     # Тип ('normal' или 'special')
        self.food_expiry = 0      # Время (в мс), когда еда исчезнет
        self.generate_food()
        
        self.game_over = False

    def generate_food(self):
        """Генерирует новую еду с разным весом и временем жизни"""
        while True:
            x = random.randint(0, WIDTH - 1)
            y = random.randint(0, HEIGHT - 1)
            # Проверяем, чтобы еда не появилась внутри змейки
            if (x, y) not in self.snake:
                self.food_pos = (x, y)
                break
        
        # Шанс 50% на появление "золотой" еды
        if random.random() < 0.5: # 0.0-1.0
            self.food_type = 'special'
            # Золотая еда живет 4 секунды (4000 миллисекунд)
            self.food_expiry = pygame.time.get_ticks() + 4000
        else:
            self.food_type = 'normal'
            # Обычная еда живет 8 секунд
            self.food_expiry = pygame.time.get_ticks() + 8000

    def update(self):
        """Обновление логики игры"""
        if self.game_over:
            return

        # Проверка таймера еды: если текущее время больше времени истечения — удаляем еду
        current_time = pygame.time.get_ticks()
        if current_time > self.food_expiry:
            self.generate_food() # Создаем новую еду, если старая исчезла

        # Рассчитываем новую позицию головы
        head_x, head_y = self.snake[0]
        new_head = (head_x + self.direction[0], head_y + self.direction[1])

        # 1. Столкновение со стенами
        if (new_head[0] < 0 or new_head[0] >= WIDTH or 
            new_head[1] < 0 or new_head[1] >= HEIGHT):
            self.game_over = True
            return

        # 2. Столкновение с самим собой
        if new_head in self.snake:
            self.game_over = True
            return

        self.snake.insert(0, new_head)

        # 3. Проверка поедания еды
        if new_head == self.food_pos:
            # Начисляем очки в зависимости от типа
            if self.food_type == 'special':
                self.score += 3
            else:
                self.score += 1
            
            # Повышение уровня и скорости за каждые 5 очков
            self.level = (self.score // 5) + 1
            self.speed = FPS + (self.level * 2)
            
            # Создаем новую еду сразу после поедания
            self.generate_food()
        else:
            # Если не съели, убираем хвост (движение)
            self.snake.pop()

    def draw(self):
        """Отрисовка графики"""
        self.screen.fill(BACKBROUND_COLOR)
        
        # Рисуем змейку
        for segment in self.snake:
            rect = pygame.Rect(segment[0] * CELL_SIZE, segment[1] * CELL_SIZE, CELL_SIZE - 1, CELL_SIZE - 1)
            pygame.draw.rect(self.screen, GREEN, rect)

        # Рисуем еду (цвет зависит от типа)
        color = GOLD if self.food_type == 'special' else RED
        food_rect = pygame.Rect(self.food_pos[0] * CELL_SIZE, self.food_pos[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(self.screen, color, food_rect)

        # Отображение счета, уровня и таймера (в секундах)
        time_left = max(0, (self.food_expiry - pygame.time.get_ticks()) // 1000)
        info_text = self.font.render(f"Score: {self.score}  Lvl: {self.level}  Food disappears in: {time_left}s", True, WHITE)
        self.screen.blit(info_text, (10, 10))

        pygame.display.flip()

    def run(self):
        """Главный цикл игры"""
        while not self.game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_over = True
                
                # Обработка нажатий клавиш (с защитой от разворота на 180 градусов)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and self.direction != (0, 1):
                        self.direction = (0, -1)
                    elif event.key == pygame.K_DOWN and self.direction != (0, -1):
                        self.direction = (1, 0) # Исправлено направление (ошибка в исходном коде была тут)
                        self.direction = (0, 1)
                    elif event.key == pygame.K_LEFT and self.direction != (1, 0):
                        self.direction = (-1, 0)
                    elif event.key == pygame.K_RIGHT and self.direction != (-1, 0):
                        self.direction = (1, 0)

            self.update()
            self.draw()
            self.clock.tick(self.speed)

        print(f"ИГРА ОКОНЧЕНА! Ваши очки: {self.score}, Уровень: {self.level}")
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = SnakeGame()
    game.run()