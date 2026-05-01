import psycopg2
from config import DB_CONFIG

def get_connection():
    """Создает и возвращает подключение к базе данных."""
    try:
        return psycopg2.connect(**DB_CONFIG)
    except Exception as e:
        print("Ошибка подключения к БД:", e)
        return None

def init_db():
    """Создает таблицы 'players' и 'game_sessions' в базе данных, если их еще нет."""
    conn = get_connection()
    if not conn: return
    with conn.cursor() as cur:
        cur.execute("""
        CREATE TABLE IF NOT EXISTS players (
            id SERIAL PRIMARY KEY,
            username VARCHAR(50) UNIQUE NOT NULL
        );
        CREATE TABLE IF NOT EXISTS game_sessions (
            id SERIAL PRIMARY KEY,
            player_id INTEGER REFERENCES players(id),
            score INTEGER NOT NULL,
            level_reached INTEGER NOT NULL,
            played_at TIMESTAMP DEFAULT NOW()
        );
        """)
        conn.commit()
    conn.close()

def save_score(username, score, level):
    """Сохраняет результат завершенной игры (очки и уровень) для конкретного игрока."""
    if not username: return
    conn = get_connection()
    if not conn: return
    with conn.cursor() as cur:
        # Добавляем игрока в базу, если его там еще нет
        cur.execute("INSERT INTO players (username) VALUES (%s) ON CONFLICT (username) DO NOTHING RETURNING id;", (username,))
        
        # Узнаем уникальный ID игрока
        cur.execute("SELECT id FROM players WHERE username = %s;", (username,))
        player_id = cur.fetchone()[0]
        
        # Сохраняем его результат (игровую сессию)
        cur.execute("INSERT INTO game_sessions (player_id, score, level_reached) VALUES (%s, %s, %s);", 
                    (player_id, score, level))
        conn.commit()
    conn.close()

def get_top_10():
    """Получает 10 лучших результатов за всё время для экрана Лидерборда."""
    conn = get_connection()
    if not conn: return []
    with conn.cursor() as cur:
        cur.execute("""
        SELECT p.username, g.score, g.level_reached, DATE(g.played_at) 
        FROM game_sessions g
        JOIN players p ON g.player_id = p.id
        ORDER BY g.score DESC LIMIT 10;
        """)
        res = cur.fetchall()
    conn.close()
    return res

def get_personal_best(username):
    """Находит максимальное количество очков (рекорд) конкретного игрока."""
    if not username: return 0
    conn = get_connection()
    if not conn: return 0
    with conn.cursor() as cur:
        cur.execute("""
        SELECT MAX(g.score) FROM game_sessions g
        JOIN players p ON g.player_id = p.id
        WHERE p.username = %s;
        """, (username,))
        res = cur.fetchone()
    conn.close()
    return res[0] if res and res[0] else 0