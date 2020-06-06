import moviepy.editor as mpy
import gizeh as gz

VIDEO_SIZE = (1920, 1080)
WHITE = (255, 255, 255)
DURATION = 5
KIDS_PIC = "./assets/cyberscooty-two-kids.png"
TEACHER_PIC = "./assets/teacher.png"

if __name__ == '__main__':
    kids_pic = mpy.ImageClip(KIDS_PIC). \
        set_position((15,900)).resize(width=200)

    teacher_pic = mpy.ImageClip(KIDS_PIC). \
        set_position((1900,900)).resize(width=200)

    video = mpy.CompositeVideoClip(
        [
            kids_pic,
            teacher_pic
        ],
        size=VIDEO_SIZE).\
        on_color(
            color=WHITE,
            col_opacity=1).set_duration(DURATION)

    video.write_videofile('sample.mp4', fps=10)
