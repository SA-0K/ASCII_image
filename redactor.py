from PIL import Image

filename = "a.jpg"

m = Image.open(f"imageRedarctor/{filename}").convert('LA')
f = open("imageRedarctor/Result.txt", "w")

final_x_resolution = 9
final_y_resolution = int(2.66 * final_x_resolution)  # any value
contrast = .1

ascii = ['.', ',', '-', '~', ':', ';', '=', '!', '*', '#', '$', '@']


def brightness_determination(stepx, stepy):

    y = final_y_resolution*stepy
    x = final_x_resolution*stepx
    brightness_sum = 0

    for i in range(0, final_x_resolution * final_y_resolution):
        #      (3 or final_x_resolution + ...
        if x > (final_x_resolution + (final_x_resolution * stepx)):
            y += 1
            x = 0
        # add brightness of red colour (R,g,b) to brightness_sum
        brightness_sum += rgb_i.getpixel((x, y))[0]

    return (brightness_sum // (final_x_resolution * final_y_resolution))


def draw_():

    stepx = 0
    stepy = 0
    for i in range(0,  resolution_x * resolution_y):
        if stepx == resolution_x:
            stepy += 1
            stepx = 0
            f.write('\n')

        # determinate average brightness of a group of pixels
        ascii_check(brightness_determination(stepx, stepy))
        stepx += 1


def ascii_check(brightness):
    avg = brightness/contrast
    symbol_number = int((avg // len(ascii))//1.85)  # convert [0;255] to [0;11]
    if symbol_number > len(ascii)-1:
        symbol_number = len(ascii)-1

    f.write(ascii[symbol_number])


resolution_x = m.size[0] // final_x_resolution
resolution_y = m.size[1] // final_y_resolution

res_img = Image.new("RGB", (resolution_x, resolution_y))
rgb_i = m.convert("RGB")


draw_()
f.close()
