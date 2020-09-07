# A script to generate the frames for a timer.
import cv2
from PIL import Image, ImageDraw, ImageFont
import math
import os


SECONDS = 300
DIMS = (1920, 1080)
FPS = 24
COLORS = [(222, 31, 72), (222, 31, 208)] # outer, inner
FONT_SIZE = 512


def generate_gradient(x, y, innerColor, outerColor):
    """Generates a gradient image.
        Gradient code adapted from https://stackoverflow.com/questions/30608035/plot-circular-gradients-using-pil-in-python

        Args:
            x (int): x-dimension.
            y (int): y-dimension.
            innerColor (array of 3 ints, RGB): the color on the inside of the gradient.
            outerColor (array of 3 ints, RGB): the color on the outside of the gradient.

        Returns:
            An instance of PIL.Image of dimensions provided with a gradient of the given color.
    """

    image = Image.new("RGB", (x, y))

    for x_c in range(x):
        for y_c in range(y):
            # Calculate and normalize distance from center
            distanceToCenter = math.sqrt((x_c - x / 2) ** 2 + (y_c - y / 2) ** 2)
            distanceToCenter = float(distanceToCenter) / (math.sqrt(2) * x / 2)

            # Calculate r, g, and b values
            r = outerColor[0] * distanceToCenter + innerColor[0] * (1 - distanceToCenter)
            g = outerColor[1] * distanceToCenter + innerColor[1] * (1 - distanceToCenter)
            b = outerColor[2] * distanceToCenter + innerColor[2] * (1 - distanceToCenter)

            # Place the pixel
            image.putpixel((x_c, y_c), (int(r), int(g), int(b)))

    return image


def generate_frame(frame, x, y, image):
    show_time = SECONDS - frame // FPS
    
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("Bebas-Regular.otf", FONT_SIZE)

    timestr = f"{int(show_time // 60)}:{int(show_time % 60):02d}"
    text_dims = font.getsize(timestr)

    draw.text((x // 2 - text_dims[0] // 2, y // 2 - text_dims[1] // 2 - 10), timestr, (255, 255, 255), font=font)

    image.save(f"frames/{frame}.jpg")


if __name__ == "__main__":
    image = generate_gradient(DIMS[0], DIMS[1], COLORS[1], COLORS[0])
    for frame in range(0, SECONDS * FPS + 1, 24):
        generate_frame(frame, DIMS[0], DIMS[1], image.copy())

    #video = cv2.VideoWriter("output.avi", 0, 1, (DIMS[0], DIMS[1]))
    #for frame in range(SECONDS * FPS):
    #    video.write(cv2.imread(os.path.join("frames/", f"{frame}.jpg")))

    #cv2.destroyAllWindows()
    #video.release()