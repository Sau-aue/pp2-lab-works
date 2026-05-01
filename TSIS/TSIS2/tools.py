import pygame

def flood_fill(surface, x, y, new_color):
    """
    Алгоритм заливки области одним цветом.
    Использует стек (очередь), чтобы программа не 'вылетала' от большой нагрузки.
    """
    # Получаем цвет пикселя, на который нажали
    target_color = surface.get_at((x, y))
    
    # Если цвет уже совпадает с выбранным — ничего не делаем
    if target_color == new_color:
        return
    
    pixels_to_fill = [(x, y)]
    width, height = surface.get_size()

    while pixels_to_fill:
        cx, cy = pixels_to_fill.pop()
        
        # Проверяем, совпадает ли текущий пиксель с цветом мишени
        if surface.get_at((cx, cy)) == target_color:
            surface.set_at((cx, cy), new_color)
            
            # Добавляем соседние пиксели в список на проверку (влево, вправо, вверх, вниз)
            if cx > 0: pixels_to_fill.append((cx - 1, cy))
            if cx < width - 1: pixels_to_fill.append((cx + 1, cy))
            if cy > 0: pixels_to_fill.append((cx, cy - 1))
            if cy < height - 1: pixels_to_fill.append((cx, cy + 1))

def draw_pencil(surf, last_pos, current_pos, width, color):
    """Рисует линию между двумя точками для плавного эффекта кисти."""
    pygame.draw.line(surf, color, last_pos, current_pos, width)

def render_text(surf, text, pos, font, color):
    """Отрисовывает текст на указанной поверхности."""
    txt_surf = font.render(text, True, color)
    surf.blit(txt_surf, pos)