import psycopg2
import json
from config import load_config

def get_db_connection():
    return psycopg2.connect(**load_config())

# --- 3.3 Import / Export ---
def export_to_json(filename="contacts.json"):
    """Экспорт всех контактов, их групп и телефонов в JSON файл"""
    try:
        with get_db_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    SELECT c.name, c.email, c.birthday, g.name, 
                           array_agg(p.phone || ':' || p.type) FILTER (WHERE p.phone IS NOT NULL)
                    FROM contacts c
                    LEFT JOIN groups g ON c.group_id = g.id
                    LEFT JOIN phones p ON c.id = p.contact_id
                    GROUP BY c.id, g.name
                """)
                data = []
                for row in cur.fetchall():
                    data.append({
                        "name": row[0], 
                        "email": row[1], 
                        "birthday": str(row[2]) if row[2] else None,
                        "group": row[3], 
                        "phones": row[4] or []
                    })
                with open(filename, "w", encoding='utf-8') as f:
                    json.dump(data, f, indent=4, ensure_ascii=False)
        print(f"Успешно экспортировано в {filename}")
    except Exception as e:
        print(f"Ошибка при экспорте: {e}")

def import_from_json(filename="contacts.json"):
    """Импорт контактов из JSON с обработкой дубликатов"""
    try:
        with open(filename, "r", encoding='utf-8') as f:
            contacts = json.load(f)
        
        with get_db_connection() as conn:
            with conn.cursor() as cur:
                for c in contacts:
                    cur.execute("SELECT id FROM contacts WHERE name = %s", (c['name'],))
                    if cur.fetchone():
                        choice = input(f"Контакт '{c['name']}' уже существует. Перезаписать? (y/n): ")
                        if choice.lower() != 'y': 
                            continue
                        cur.execute("DELETE FROM contacts WHERE name = %s", (c['name'],))

                    # Вставка базовой инфы
                    cur.execute(
                        "INSERT INTO contacts (name, email, birthday) VALUES (%s, %s, %s)",
                        (c['name'], c['email'], c['birthday'])
                    )
                    conn.commit()

                    # Привязка группы и телефонов через процедуры из 3.4
                    cur.execute("CALL move_to_group(%s, %s)", (c['name'], c['group']))
                    for p_entry in c['phones']:
                        if ':' in p_entry:
                            p_val, p_type = p_entry.split(':')
                            cur.execute("CALL add_phone(%s, %s, %s)", (c['name'], p_val, p_type))
            conn.commit()
        print("Импорт завершен успешно.")
    except FileNotFoundError:
        print(f"Файл {filename} не найден.")
    except Exception as e:
        print(f"Ошибка при импорте: {e}")

# --- 3.2 Advanced Console Search & Filter ---
def view_paginated():
    """Консольный интерфейс с постраничной навигацией (Task 3.2)"""
    page, limit = 1, 5
    while True:
        offset = (page - 1) * limit
        try:
            with get_db_connection() as conn:
                with conn.cursor() as cur:
                    cur.execute("SELECT * FROM get_contacts_paginated(%s, %s)", (limit, offset))
                    rows = cur.fetchall()
            
            print(f"\n--- Страница {page} ---")
            if not rows:
                print("   [Записей нет]")
            else:
                for r in rows: 
                    print(f"ID: {r[0]} | Имя: {r[1]} | Email: {r[2]} | Дата: {r[3]}")
            
            print("-" * 20)
            cmd = input("[n]ext (вперед), [p]rev (назад), [q]uit (выход): ").lower()
            
            if cmd == 'n':
                if len(rows) < limit:
                    print(">> Это последняя страница.")
                else:
                    page += 1
            elif cmd == 'p':
                if page > 1:
                    page -= 1
                else:
                    print(">> Это первая страница.")
            elif cmd == 'q':
                break
        except Exception as e:
            print(f"Ошибка пагинации: {e}")
            break

if __name__ == "__main__":
    # Главное меню для теста
    print("1. Показать контакты (Пагинация)")
    print("2. Экспорт в JSON")
    print("3. Импорт из JSON")
    ans = input("Выберите действие: ")
    
    if ans == '1': view_paginated()
    elif ans == '2': export_to_json()
    elif ans == '3': import_from_json()