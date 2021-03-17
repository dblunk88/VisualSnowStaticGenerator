from random import randint

from config import settings
from config import colors
from src import circle_colors


class Animations:
    def __init__(self, canvas, pygame):
        self.active_pixels = []
        self.moving_pixels = []
        self.canvas = canvas
        self.pygame = pygame
        for x in range(0,7000):
            self.moving_pixels.append([randint(0,canvas.screen_width),randint(0,canvas.screen_height),randint(5,10),
                                       circle_colors.random()])

    def inflate_deflate(self):
        canvas = self.canvas
        pygame = self.pygame
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

    def come_and_go(self):
        canvas = self.canvas
        pygame = self.pygame
        for x in range(0,randint(2500,3000)):
            pygame.draw.circle(surface=canvas.screen,color=colors.WHITE,center=(randint(0,canvas.screen_width),
                                                                                randint(0,canvas.screen_height)),
                               radius=randint(5,10))

    def move_around(self):
        canvas = self.canvas
        pygame = self.pygame
        moving_pixels = self.moving_pixels
        for counter in range(0,len(moving_pixels)):
            moving_pixels[counter][0] += int(randint(-5,5))
            if moving_pixels[counter][0] >= canvas.screen_width+10:
                moving_pixels[counter][0] -= 20
            elif moving_pixels[counter][0] <= 0:
                moving_pixels[counter][0] += 20
            x = moving_pixels[counter][0]
            moving_pixels[counter][1] += int(randint(-5,5))
            if moving_pixels[counter][1] >= canvas.screen_height+10:
                moving_pixels[counter][1] -= randint(8,10)
            elif moving_pixels[counter][1] <= 0:
                moving_pixels[counter][1] += randint(8,10)
            y = moving_pixels[counter][1]
            width = moving_pixels[counter][2]
            colors = [moving_pixels[counter][3][0] + randint(-5,5),
                      moving_pixels[counter][3][1] + randint(-5,5),
                      moving_pixels[counter][3][2] + randint(-5,5)]
            for counter in range(0, len(colors)):
                if colors[counter] <= 0:
                    colors[counter] += 15
                if colors[counter] >= 255:
                    colors[counter] -= 15
            moving_pixels[counter][3] = (colors[0],colors[1],colors[2])
            color = moving_pixels[counter][3]
            pygame.draw.circle(surface=canvas.screen,color=color,center=(x,y),
                               radius=width)
        self.moving_pixels = moving_pixels
