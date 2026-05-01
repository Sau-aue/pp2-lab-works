-- Процедура добавления телефона
CREATE OR REPLACE PROCEDURE add_phone(p_contact_name VARCHAR, p_phone VARCHAR, p_type VARCHAR)
LANGUAGE plpgsql AS $$
DECLARE
    v_id INT;
BEGIN
    SELECT id INTO v_id FROM contacts WHERE name = p_contact_name;
    IF v_id IS NOT NULL THEN
        INSERT INTO phones (contact_id, phone, type) VALUES (v_id, p_phone, p_type);
    END IF;
END;
$$;

-- Процедура перемещения в группу (создает группу, если её нет)
CREATE OR REPLACE PROCEDURE move_to_group(p_contact_name VARCHAR, p_group_name VARCHAR)
LANGUAGE plpgsql AS $$
DECLARE
    v_group_id INT;
BEGIN
    INSERT INTO groups (name) VALUES (p_group_name) ON CONFLICT (name) DO NOTHING;
    SELECT id INTO v_group_id FROM groups WHERE name = p_group_name;
    UPDATE contacts SET group_id = v_group_id WHERE name = p_contact_name;
END;
$$;

-- Функция расширенного поиска (по имени, email и всем телефонам)
CREATE OR REPLACE FUNCTION search_contacts_ext(p_query TEXT)
RETURNS TABLE(contact_name VARCHAR, email VARCHAR, phone_list TEXT) 
LANGUAGE plpgsql AS $$
BEGIN
    RETURN QUERY
    SELECT c.name, c.email, string_agg(p.phone, ', ')
    FROM contacts c
    LEFT JOIN phones p ON c.id = p.contact_id
    WHERE c.name ILIKE '%' || p_query || '%'
       OR c.email ILIKE '%' || p_query || '%'
       OR p.phone ILIKE '%' || p_query || '%'
    GROUP BY c.id;
END;
$$;

-- Функция пагинации (замена Practice 8)
CREATE OR REPLACE FUNCTION get_contacts_paginated(p_limit INT, p_offset INT)
RETURNS TABLE(id INT, name VARCHAR, email VARCHAR, birthday DATE) 
LANGUAGE plpgsql AS $$
BEGIN
    RETURN QUERY
    SELECT c.id, c.name, c.email, c.birthday
    FROM contacts c
    ORDER BY c.name
    LIMIT p_limit
    OFFSET p_offset;
END;
$$;