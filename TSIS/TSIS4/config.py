CELL_SIZE = 20
WIDTH, HEIGHT = 30, 20  
SCREEN_WIDTH = WIDTH * CELL_SIZE
SCREEN_HEIGHT = HEIGHT * CELL_SIZE
INITIAL_FPS = 10

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)         # Обычная еда
GOLD = (255, 215, 0)      # Золотая еда
DARK_RED = (139, 0, 0)    # Яд
BLUE = (50, 150, 255)     # Ускорение (Speed)
CYAN = (0, 255, 255)      # Замедление (Slow)
PURPLE = (148, 0, 211)    # Щит (Shield)
GRAY = (100, 100, 100)    # Препятствия
BACKGROUND_COLOR = (40, 40, 50)

# Настройки базы данных PostgreSQL
DB_CONFIG = {
    "dbname": "snake_db",
    "user": "postgres",
    "password": "123", # ВПИШИ СВОЙ ПАРОЛЬ
    "host": "localhost",
    "port": "5432"
}