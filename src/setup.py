import platform
import shutil
import time
from pathlib import Path

import pygame

from config import colors
from config import settings


class Setup:
    def __init__(self):
        self.iterator_counter = 0

    pygame.init()
    if settings.screenshot_pics:
        try:
            Path(settings.screenshots_directory).mkdir(parents=True,exist_ok=False)
        except FileExistsError:
            shutil.rmtree(settings.screenshots_directory)
            time.sleep(3)
            Path(settings.screenshots_directory).mkdir(parents=True,exist_ok=False)
        prepopulate_frames = settings.prepopulate_frames
        screenshot_frames = settings.screenshot_frames
        screen_width = settings.screen_width
        screen_height = settings.screen_height
        fps = settings.fps
        WINDOW_SURFACE = pygame.HWSURFACE | pygame.DOUBLEBUF
        window = pygame.display.set_mode((settings.screen_width,settings.screen_height),WINDOW_SURFACE)
        screen = pygame.Surface((settings.screen_width,settings.screen_height))
        screen.fill(colors.BLACK)
        if platform.system() == "Windows":
            dir_separator = "\\"
        else:
            dir_separator = "/"
    else:
        info = pygame.display.Info()
        screen_width,screen_height = info.current_w,info.current_h
        pygame.display.set_caption("Visual Snow Generator")
        screen = pygame.Surface((screen_width,screen_height))
        screen.fill(colors.BLACK)
        WINDOW_SURFACE = pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RESIZABLE
        window = pygame.display.set_mode((screen_width,screen_height - 50),WINDOW_SURFACE)
