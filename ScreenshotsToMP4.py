# TODO: Automate this via subprocess or similarly if in screenshot mode
#ffmpeg -r 24 -f image2 -s 1920x1080 -i %d.png -vcodec libx264 -crf 15 static.mp4