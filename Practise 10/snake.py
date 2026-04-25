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
RED = (255, 0, 0)
BLACK = (0, 0, 0)

class SnakeGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Arial", 18)
        
        # Начальное состояние змейки
        self.snake = [(10, 10), (10, 11), (10, 12)]
        self.direction = (0, -1)  # Вверх
        self.score = 0
        self.level = 1
        self.speed = FPS
        self.food = self.generate_food()
        self.game_over = False

    def generate_food(self):
        """Генерирует позицию еды, чтобы она не попала на змейку или стену"""
        while True:
            x = random.randint(0, WIDTH - 1)
            y = random.randint(0, HEIGHT - 1)
            if (x, y) not in self.snake:
                return (x, y)

    def update(self):
        """Логика движения и проверок"""
        if self.game_over:
            return

        # Новая голова змейки
        head_x, head_y = self.snake[0]
        new_head = (head_x + self.direction[0], head_y + self.direction[1])

        # 1. Проверка столкновения с границами (wall collision)
        if (new_head[0] < 0 or new_head[0] >= WIDTH or 
            new_head[1] < 0 or new_head[1] >= HEIGHT):
            self.game_over = True
            return

        # 2. Проверка столкновения с собой
        if new_head in self.snake:
            self.game_over = True
            return

        self.snake.insert(0, new_head)

        # 3. Проверка поедания еды
        if new_head == self.food:
            self.score += 1
            self.food = self.generate_food()
            # Повышение уровня каждые 3 очка
            if self.score % 3 == 0:
                self.level += 1
                self.speed += 2 # Увеличиваем скорость (FPS)
        else:
            self.snake.pop() # Удаляем хвост, если ничего не съели

    def draw(self):
        """Отрисовка всех элементов"""
        self.screen.fill(BLACK)
        
        # Рисуем змейку
        for segment in self.snake:
            rect = pygame.Rect(segment[0] * CELL_SIZE, segment[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(self.screen, GREEN, rect)

        # Рисуем еду
        food_rect = pygame.Rect(self.food[0] * CELL_SIZE, self.food[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(self.screen, RED, food_rect)

        # Вывод текста (Score и Level)
        score_text = self.font.render(f"Score: {self.score}  Level: {self.level}", True, WHITE)
        self.screen.blit(score_text, (10, 10))

        pygame.display.flip()

    def run(self):
        """Основной игровой цикл"""
        while not self.game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                # Управление
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and self.direction != (0, 1):
                        self.direction = (0, -1)
                    elif event.key == pygame.K_DOWN and self.direction != (0, -1):
                        self.direction = (0, 1)
                    elif event.key == pygame.K_LEFT and self.direction != (1, 0):
                        self.direction = (-1, 0)
                    elif event.key == pygame.K_RIGHT and self.direction != (-1, 0):
                        self.direction = (1, 0)

            self.update()
            self.draw()
            self.clock.tick(self.speed) # Контроль скорости

        print(f"Игра окончена! Очки: {self.score}, Уровень: {self.level}")
        pygame.quit()

if __name__ == "__main__":
    game = SnakeGame()
    game.run()