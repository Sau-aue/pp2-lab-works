import pygame
import math
import datetime
# Импортируем наши функции из соседнего файла
from tools import flood_fill, draw_pencil, render_text

# Инициализация Pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pygame Paint Pro (Modular)")
clock = pygame.time.Clock()

# Настройки
font_main = pygame.font.SysFont("Arial", 20)
canvas = pygame.Surface((800, 600))
canvas.fill((0, 0, 0)) # Черный холст

# Состояние программы
color = (255, 255, 255)
radius = 5
tool = 'pencil'
drawing = False
start_pos = (0, 0)
last_pos = (0, 0)

# Для текста
text_input = ""
text_pos = (0, 0)
typing = False

running = True
while running:
    mouse_pos = pygame.mouse.get_pos()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # КЛАВИАТУРА
        if event.type == pygame.KEYDOWN:
            # Смена размера (F1, F2, F3)
            if event.key == pygame.K_F1: radius = 2
            elif event.key == pygame.K_F2: radius = 5
            elif event.key == pygame.K_F3: radius = 10
            
            # Инструменты (1-7)
            if not typing:
                if event.key == pygame.K_1: tool = 'pencil'
                elif event.key == pygame.K_2: tool = 'line'
                elif event.key == pygame.K_3: tool = 'rect'
                elif event.key == pygame.K_4: tool = 'circle'
                elif event.key == pygame.K_5: tool = 'fill'
                elif event.key == pygame.K_6: tool = 'text'
                elif event.key == pygame.K_7: tool = 'eraser'

            # Сохранение Ctrl + S
            if event.key == pygame.K_s and (pygame.key.get_mods() & pygame.KMOD_CTRL):
                name = f"paint_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
                pygame.image.save(canvas, name)

            # Ввод текста
            if typing:
                if event.key == pygame.K_RETURN:
                    render_text(canvas, text_input, text_pos, font_main, color)
                    typing = False
                    text_input = ""
                elif event.key == pygame.K_ESCAPE:
                    typing = False
                elif event.key == pygame.K_BACKSPACE:
                    text_input = text_input[:-1]
                else:
                    text_input += event.unicode

        # МЫШЬ
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if tool == 'fill':
                    flood_fill(canvas, *event.pos, color)
                elif tool == 'text':
                    typing = True
                    text_pos = event.pos
                    text_input = ""
                else:
                    drawing = True
                    start_pos = last_pos = event.pos

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1 and drawing:
                drawing = False
                # Фиксация фигур на холсте
                if tool == 'line':
                    pygame.draw.line(canvas, color, start_pos, event.pos, radius)
                elif tool == 'rect':
                    r = pygame.Rect(start_pos, (event.pos[0]-start_pos[0], event.pos[1]-start_pos[1]))
                    r.normalize()
                    pygame.draw.rect(canvas, color, r, radius)
                elif tool == 'circle':
                    r = int(math.hypot(event.pos[0]-start_pos[0], event.pos[1]-start_pos[1]))
                    pygame.draw.circle(canvas, color, start_pos, r, radius)

        if event.type == pygame.MOUSEMOTION:
            if drawing:
                if tool == 'pencil':
                    draw_pencil(canvas, last_pos, event.pos, radius, color)
                    last_pos = event.pos
                elif tool == 'eraser':
                    draw_pencil(canvas, last_pos, event.pos, radius, (0,0,0))
                    last_pos = event.pos

    # Отрисовка на экран
    screen.fill((40, 40, 40))
    screen.blit(canvas, (0, 0))

    # Предпросмотр (то, что мы видим, пока тянем мышь)
    if drawing:
        if tool == 'line':
            pygame.draw.line(screen, color, start_pos, mouse_pos, radius)
        elif tool == 'rect':
            r = pygame.Rect(start_pos, (mouse_pos[0]-start_pos[0], mouse_pos[1]-start_pos[1]))
            r.normalize()
            pygame.draw.rect(screen, color, r, radius)
        elif tool == 'circle':
            r = int(math.hypot(mouse_pos[0]-start_pos[0], mouse_pos[1]-start_pos[1]))
            pygame.draw.circle(screen, color, start_pos, r, radius)

    if typing:
        render_text(screen, text_input + "|", text_pos, font_main, color)

    # Маленький индикатор кисти под курсором
    pygame.draw.circle(screen, (200, 200, 200), mouse_pos, radius, 1)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()