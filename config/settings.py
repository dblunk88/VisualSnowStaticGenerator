from config import colors

# Display Settings
screen_fps_limit = True
screen_fps = 60

# Screenshot Settings
screenshot_pics = True
screenshots_directory = "E:\\screenshots"
image_format = "png"
screenshot_frames = 14400
screen_width = 1920
screen_height = 1080
fps = 60
prepopulate_frames = 50

# TODO: Eventually break this up into individual settings for different methods
# Method: Inflate - Deflate
pixel_creation_min = 0
pixel_creation_max = 250
max_pixel_width_min = 15
max_pixel_width_max = 25

# Method: Populate Entire Screen
# Matrix settings
random_chance = True
x_rand_min = 15
x_rand_max = 65
y_rand_min = 15
y_rand_max = 65
# Circle Settings
circle_color = [colors.WHITE,colors.BLACK]
circle_min = 10
circle_max = 20
random_color_chance = 1
