from random import randint

from config import settings
from config import colors
from src import circle_colors


class Animations:
    def __init__(self):
        self.active_pixels = []

    def inflate_deflate(self,canvas,pygame):
        active_pixels = self.active_pixels
        for counter in range(randint(settings.pixel_creation_min,settings.pixel_creation_max)):
            active_pixels.append([randint(0,canvas.screen_width),  # x
                                       randint(0,canvas.screen_height),  # y
                                       0,  # starting width
                                       circle_colors.random(),  # color
                                       True])  # inflate mode
        updated_active_pixels = active_pixels.copy()
        for counter in range(0,len(active_pixels)):
            x = active_pixels[counter][0]
            y = active_pixels[counter][1]
            width = active_pixels[counter][2]
            color = active_pixels[counter][3]
            grow = active_pixels[counter][4]
            if width >= randint(settings.max_pixel_width_min,settings.max_pixel_width_max) and grow:
                active_pixels[counter][4] = False
            elif not grow and width <= 0:
                del updated_active_pixels[counter]
                continue
            if grow:
                active_pixels[counter][2] = active_pixels[counter][2] + 1
                pygame.draw.circle(surface=canvas.screen,color=color,center=(x,y),
                                   radius=width)
            elif not grow:
                active_pixels[counter][2] = active_pixels[counter][2] - 1
                pygame.draw.circle(surface=canvas.screen,color=color,center=(x,y),
                                   radius=width)
        self.active_pixels = updated_active_pixels

    def come_and_go(self,canvas,pygame):
        for x in range(0,randint(2500,3000)):
            pygame.draw.circle(surface=canvas.screen,color=colors.WHITE,center=(randint(0,canvas.screen_width),
                                                                                randint(0,canvas.screen_height)),
                               radius=randint(5,10))
