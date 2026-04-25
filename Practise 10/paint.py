import pygame

def drawLineBetween(surface, start, end, width, color):
    """Draws a smooth line between two points using overlapping circles."""
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    
    # If the mouse didn't move, just draw a single circle
    if iterations == 0:
        pygame.draw.circle(surface, color, start, width)
        return

    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(surface, color, (x, y), width)

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Pygame Paint Application")
    clock = pygame.time.Clock()
    
    # Create a persistent canvas to draw on
    canvas = pygame.Surface((640, 480))
    canvas.fill((0, 0, 0)) 
    
    radius = 15
    tool = 'brush' # Options: 'brush', 'rect', 'circle', 'eraser'
    color = (0, 0, 255) 
    
    drawing = False
    start_pos = (0, 0)
    last_pos = (0, 0)
    
    # Color dictionary for easy switching
    colors = {
        pygame.K_r: (255, 0, 0),    # Red
        pygame.K_g: (0, 255, 0),    # Green
        pygame.K_b: (0, 0, 255),    # Blue
        pygame.K_y: (255, 255, 0),  # Yellow
        pygame.K_w: (255, 255, 255) # White
    }
    
    while True:
        pressed = pygame.key.get_pressed()
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return
                
                # --- Color Selection ---
                if event.key in colors:
                    color = colors[event.key]
                    
                # --- Tool Selection ---
                if event.key == pygame.K_1:
                    tool = 'brush'
                elif event.key == pygame.K_2:
                    tool = 'rect'
                elif event.key == pygame.K_3:
                    tool = 'circle'
                elif event.key == pygame.K_4:
                    tool = 'eraser'
                    
                # --- Radius Adjustment (Keyboard fallback) ---
                if event.key == pygame.K_UP:
                    radius = min(200, radius + 2)
                if event.key == pygame.K_DOWN:
                    radius = max(1, radius - 2)

            # --- Radius Adjustment (Mouse Wheel) ---
            if event.type == pygame.MOUSEWHEEL:
                if event.y > 0:
                    radius = min(200, radius + 2)
                elif event.y < 0:
                    radius = max(1, radius - 2)
                    
            # --- Mouse Down: Start Drawing/Shapes ---
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: # Left click
                    drawing = True
                    start_pos = event.pos
                    last_pos = event.pos
                    
            # --- Mouse Up: Commit Shapes to Canvas ---
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1 and drawing:
                    drawing = False
                    
                    if tool == 'rect':
                        rect = pygame.Rect(start_pos[0], start_pos[1], event.pos[0] - start_pos[0], event.pos[1] - start_pos[1])
                        rect.normalize() # Prevents negative dimensions if dragged backwards
                        pygame.draw.rect(canvas, color, rect, radius)
                        
                    elif tool == 'circle':
                        dx = event.pos[0] - start_pos[0]
                        dy = event.pos[1] - start_pos[1]
                        r = int((dx**2 + dy**2)**0.5)
                        # Ensure thickness isn't greater than radius to prevent Pygame errors
                        pygame.draw.circle(canvas, color, start_pos, r, min(r, radius)) 
            
            # --- Mouse Motion: Draw Brush/Eraser or Preview Shapes ---
            if event.type == pygame.MOUSEMOTION:
                if drawing:
                    if tool == 'brush':
                        drawLineBetween(canvas, last_pos, event.pos, radius, color)
                        last_pos = event.pos
                    elif tool == 'eraser':
                        # Eraser simply draws with the background color
                        drawLineBetween(canvas, last_pos, event.pos, radius, (0, 0, 0))
                        last_pos = event.pos
        
        # 1. Draw the persistent canvas to the screen
        screen.blit(canvas, (0, 0))
        
        # 2. Draw live previews for shapes while dragging
        if drawing:
            mouse_pos = pygame.mouse.get_pos()
            if tool == 'rect':
                rect = pygame.Rect(start_pos[0], start_pos[1], mouse_pos[0] - start_pos[0], mouse_pos[1] - start_pos[1])
                rect.normalize()
                pygame.draw.rect(screen, color, rect, radius)
            elif tool == 'circle':
                dx = mouse_pos[0] - start_pos[0]
                dy = mouse_pos[1] - start_pos[1]
                r = int((dx**2 + dy**2)**0.5)
                pygame.draw.circle(screen, color, start_pos, r, min(r, radius))
        
        # 3. Draw a cursor outline so the user can see their current brush size
        mouse_pos = pygame.mouse.get_pos()
        cursor_color = (150, 150, 150) if tool == 'eraser' else color
        pygame.draw.circle(screen, cursor_color, mouse_pos, radius, 1)

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()