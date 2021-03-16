from random import randint
from config import settings

def random():
    color = (randint(0,255),randint(0,255),randint(0,255))
    return color

def generateColor():
    color = settings.circle_color[randint(0,len(settings.circle_color)) + settings.random_color_chance]
    return color