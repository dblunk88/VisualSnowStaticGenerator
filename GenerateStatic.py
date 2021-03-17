import os

import pygame

from config import settings
from src import animations
from src import capture
from src import screen
from src import canvas_setup
from src import user_events

os.environ['SDL_VIDEO_CENTERED'] = '1'


def run():
    if settings.screen_fps_limit:
        clock = pygame.time.Clock()
    done = False
    canvas = canvas_setup.Setup()
    animate = animations.Animations(canvas, pygame)
    while not done:
        canvas.screen.fill(settings.colors.BLACK)
        # Checking if the user did something
        done = user_events.check_events(canvas,pygame)

        # Populating screen
        # populate.entire_screen(canvas,pygame)



        # Animate: Come and go
        # animate.come_and_go()

        # Animate: Inflate Deflate
        # animate.inflate_deflate()

        # Animate: Move around
        # animate.move_around()

        # Animate: VR Static
        animate.VR_Static()

        # Update Screen
        screen.update(canvas,pygame)
        if settings.screen_fps_limit:
            clock.tick(settings.screen_fps)

        # Take screenshots if in screenshot mode
        if settings.screenshot_pics:
            # TODO: break loop once video conversion starts
            capture.screenshot(canvas,pygame)
    pygame.quit()


if __name__ == "__main__":
    run()
