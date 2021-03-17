import subprocess
from os import chdir
from os import getcwd
from config import settings

def convert():
    chdir(settings.screenshots_directory)
    print(getcwd())
    # Needs to have ffmpeg installed
    cmd = "ffmpeg -r {} -f image2 -s 1920x1080 -i %d.png -vcodec libx264 -crf 15 static.mp4 -y".format(
        settings.fps
    )
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,universal_newlines=True)
    for line in process.stdout:
        print(line)
    print("Done")