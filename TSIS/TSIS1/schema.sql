-- Таблица групп
CREATE TABLE IF NOT EXISTS groups (
    id   SERIAL PRIMARY KEY,
    name VARCHAR(50) UNIQUE NOT NULL
);

-- Начальные данные для групп
INSERT INTO groups (name) VALUES ('Family'), ('Work'), ('Friend'), ('Other') ON CONFLICT DO NOTHING;

-- Основная таблица контактов (с добавленными полями)
CREATE TABLE IF NOT EXISTS contacts (
    id       SERIAL PRIMARY KEY,
    name     VARCHAR(100) NOT NULL UNIQUE,
    email    VARCHAR(100),
    birthday DATE,
    group_id INTEGER REFERENCES groups(id) ON DELETE SET NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Таблица для телефонов (связь 1-ко-многим)
CREATE TABLE IF NOT EXISTS phones (
    id         SERIAL PRIMARY KEY,
    contact_id INTEGER REFERENCES contacts(id) ON DELETE CASCADE,
    phone      VARCHAR(20)  NOT NULL,
    type       VARCHAR(10)  CHECK (type IN ('home', 'work', 'mobile'))
);