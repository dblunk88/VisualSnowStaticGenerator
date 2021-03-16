from random import choice as randchoice
from random import randint
from config import settings
from src import circle_colors

def entire_screen(canvas, pygame):
    x_rand = randint(settings.x_rand_min,settings.x_rand_max)
    y_rand = randint(settings.x_rand_min,settings.x_rand_max)
    if settings.random_chance:
        # 50/50 chance of spawning
        choices = [True, False]
    for x in range(0,canvas.screen_width,x_rand):
        for y in range(0,canvas.screen_height,y_rand):
            if settings.random_chance:
                choice = randchoice(choices)
                if choice:
                    display_random_color(canvas, x,y, pygame)
            else:
                display_random_color(canvas,x,y, pygame)


def display_random_color(canvas, x, y, pygame):
    try:
        color = circle_colors.generateColor()
    except IndexError:
        color = circle_colors.random()
    pygame.draw.circle(surface=canvas.screen ,color=color,center=(x,y),radius=randint(settings.circle_min,settings.circle_max))