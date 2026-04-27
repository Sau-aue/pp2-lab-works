import pygame
import math

def drawLineBetween(surface, start, end, width, color):
    """Рисует плавную линию между двумя точками, заполняя пространство кругами."""
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    
    if iterations == 0:
        pygame.draw.circle(surface, color, start, width)
        return

    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(surface, color, (x, y), width)

def draw_shape(surface, tool, start_pos, end_pos, color, radius):
    """Вспомогательная функция для отрисовки сложных фигур."""
    dx = end_pos[0] - start_pos[0]
    dy = end_pos[1] - start_pos[1]

    if tool == 'square':
        # Квадрат: находим сторону как максимальное смещение и выравниваем
        side = max(abs(dx), abs(dy))
        s_x = start_pos[0] if dx > 0 else start_pos[0] - side
        s_y = start_pos[1] if dy > 0 else start_pos[1] - side
        rect = pygame.Rect(s_x, s_y, side, side)
        pygame.draw.rect(surface, color, rect, radius)

    elif tool == 'right_triangle':
        # Прямоугольный треугольник: (x1, y1), (x1, y2), (x2, y2)
        points = [start_pos, (start_pos[0], end_pos[1]), end_pos]
        pygame.draw.polygon(surface, color, points, radius)

    elif tool == 'equilateral_triangle':
        # Равносторонний треугольник: основание по горизонтали, вершина по центру
        height = dy
        base_half = abs(height) / math.sqrt(3)
        p1 = (start_pos[0], start_pos[1]) # Вершина
        p2 = (start_pos[0] - base_half, start_pos[1] + height)
        p3 = (start_pos[0] + base_half, start_pos[1] + height)
        pygame.draw.polygon(surface, color, [p1, p2, p3], radius)

    elif tool == 'rhombus':
        # Ромб: соединяем середины сторон описывающего прямоугольника
        mid_top = (start_pos[0] + dx // 2, start_pos[1])
        mid_bottom = (start_pos[0] + dx // 2, end_pos[1])
        mid_left = (start_pos[0], start_pos[1] + dy // 2)
        mid_right = (end_pos[0], start_pos[1] + dy // 2)
        pygame.draw.polygon(surface, color, [mid_top, mid_right, mid_bottom, mid_left], radius)

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Pygame Paint Pro")
    clock = pygame.time.Clock()
    
    canvas = pygame.Surface((640, 480))
    canvas.fill((0, 0, 0)) 
    
    radius = 5
    tool = 'brush' 
    color = (0, 0, 255) 
    drawing = False
    start_pos = (0, 0)
    last_pos = (0, 0)
    
    colors = {
        pygame.K_r: (255, 0, 0), pygame.K_g: (0, 255, 0),
        pygame.K_b: (0, 0, 255), pygame.K_y: (255, 255, 0),
        pygame.K_w: (255, 255, 255)
    }
    
    while True:
        mouse_pos = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
            if event.type == pygame.KEYDOWN:
                # Выбор инструментов
                if event.key == pygame.K_1: tool = 'brush'
                elif event.key == pygame.K_2: tool = 'rect'
                elif event.key == pygame.K_3: tool = 'circle'
                elif event.key == pygame.K_4: tool = 'eraser'
                elif event.key == pygame.K_5: tool = 'square'
                elif event.key == pygame.K_6: tool = 'right_triangle'
                elif event.key == pygame.K_7: tool = 'equilateral_triangle'
                elif event.key == pygame.K_8: tool = 'rhombus'
                
                if event.key in colors:
                    color = colors[event.key]

            if event.type == pygame.MOUSEWHEEL:
                radius = max(1, min(200, radius + event.y * 2))
                    
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    drawing = True
                    start_pos = event.pos
                    last_pos = event.pos
            
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1 and drawing:
                    drawing = False
                    # Фиксация фигур на основном холсте
                    if tool in ['square', 'right_triangle', 'equilateral_triangle', 'rhombus']:
                        draw_shape(canvas, tool, start_pos, event.pos, color, radius)
                    elif tool == 'rect':
                        r = pygame.Rect(start_pos, (event.pos[0]-start_pos[0], event.pos[1]-start_pos[1]))
                        r.normalize()
                        pygame.draw.rect(canvas, color, r, radius)
                    elif tool == 'circle':
                        r = int(math.hypot(event.pos[0]-start_pos[0], event.pos[1]-start_pos[1]))
                        pygame.draw.circle(canvas, color, start_pos, r, min(r, radius))
            
            if event.type == pygame.MOUSEMOTION:
                if drawing:
                    if tool == 'brush':
                        drawLineBetween(canvas, last_pos, event.pos, radius, color)
                        last_pos = event.pos
                    elif tool == 'eraser':
                        drawLineBetween(canvas, last_pos, event.pos, radius, (0, 0, 0))
                        last_pos = event.pos
        
        # Отрисовка
        screen.blit(canvas, (0, 0))
        
        # Предпросмотр (пока кнопка мыши зажата)
        if drawing:
            if tool in ['square', 'right_triangle', 'equilateral_triangle', 'rhombus']:
                draw_shape(screen, tool, start_pos, mouse_pos, color, radius)
            elif tool == 'rect':
                r = pygame.Rect(start_pos, (mouse_pos[0]-start_pos[0], mouse_pos[1]-start_pos[1]))
                r.normalize()
                pygame.draw.rect(screen, color, r, radius)
            elif tool == 'circle':
                r = int(math.hypot(mouse_pos[0]-start_pos[0], mouse_pos[1]-start_pos[1]))
                pygame.draw.circle(screen, color, start_pos, r, min(r, radius))
        
        # Указатель размера кисти
        pygame.draw.circle(screen, (150, 150, 150), mouse_pos, radius, 1)

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()