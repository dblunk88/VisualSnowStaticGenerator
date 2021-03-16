from config import settings

def check_events(canvas, pygame):
    for event in pygame.event.get():
        if not settings.screenshot_pics and event.type == pygame.VIDEORESIZE:
            update_window_size(pygame, canvas)
            return False
        if event.type == pygame.QUIT:
            return True

def update_window_size(pygame, canvas):
    canvas.screen_width,canvas.screen_height = pygame.display.get_surface().get_size()
    canvas.screen = pygame.Surface((canvas.screen_width,canvas.screen_height))