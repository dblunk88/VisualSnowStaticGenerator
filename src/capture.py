import sys

from config import settings


def screenshot(canvas,pygame):
    if canvas.iterator_counter < canvas.prepopulate_frames:
        canvas.iterator_counter = canvas.iterator_counter + 1
        print("Prepopulating Frame {}/{}\t{}%"
              .format(canvas.iterator_counter,settings.prepopulate_frames,
                      "%.2f" % ((canvas.iterator_counter / settings.prepopulate_frames) * 100)))
    elif canvas.iterator_counter < canvas.screenshot_frames + settings.prepopulate_frames:
        current_frame_iteration = canvas.iterator_counter - canvas.prepopulate_frames + 1
        print("Generating Frame {}/{}\t{}%\t{} seconds".format(current_frame_iteration,canvas.screenshot_frames,
                                                               "%.2f" % ((
                                                                                     current_frame_iteration / canvas.screenshot_frames) * 100),
                                                               "%.4f" % (current_frame_iteration / canvas.fps)))
        sys.stdout.flush()
        pygame.image.save(canvas.screen,settings.screenshots_directory + canvas.dir_separator + "{}.{}"
                          .format(current_frame_iteration,settings.image_format))
        canvas.iterator_counter = canvas.iterator_counter + 1
    elif canvas.iterator_counter >= canvas.screenshot_frames:
        pygame.quit()
        exit(0)
