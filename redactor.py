from PIL import Image, ImageDraw
m = Image.open("image redarctor/a.jpg").convert('LA')
# m.load()

xz = 9
yz = 24

# palette = [[255, 255, 255], [0, 0, 255], [255, 0, 0], [255, 0, 255],
#           [0, 255, 0], [0, 255, 255], [255, 255, 0], [0, 0, 0]]
global h
h = 0
ascii = ['.', ',', '-', '~', ':', ';', '=', '!', '*', '#', '$', '@']
f = open("image redarctor/Result.txt", "w")


def recognize(stepx, stepy):  # 349 2
    # 4x4
    global tup
    a = []  # 16
    y = 0 + (yz*stepy)  # 2
    x = 0 + (xz*stepx)  # 349
    tup = []
    r1 = 0
    b1 = 0
    c1 = 0
    #print("Position", 4*stepx, ':', 4*stepx+4, 4*stepy, ':', 4*stepy+4)
    for i in range(0, xz*yz):
        b = rgb_i.getpixel((x, y))
        a.append(b)

        if x > (3 + (xz*stepx)):
            y += 1
            x = 0
        r1 += int(a[i][0])
        b1 += int(a[i][1])
        c1 += int(a[i][2])

    tup.append(r1//(xz*yz))
    tup.append(b1//(xz*yz))
    tup.append(c1//(xz*yz))
    # print(tup)


def draw_(cvb):

    j = 0
    yy = 0
    for i in range(0,  res_xs * res_ys):
        if j == res_xs:

            yy += 1
            j = 0
            f.write('\n')
        recognize(j, yy)

        res_img.putpixel(
            (j, yy), (tup[0], tup[1], tup[2]))
        ascii_check(cvb)
        j += 1


def ascii_check(cvb):
    global h
    avg = (tup[0]+tup[1] + tup[2])/cvb
    symbol = int((avg // len(ascii))//1.85)
    if symbol > 11:
        symbol = 11

    f.write(ascii[symbol])
    h += 1

    # print(ascii[symbol])


or_xs = m.size[0]
or_ys = m.size[1]

res_xs = or_xs // xz
res_ys = or_ys // yz

res_img = Image.new("RGB", (res_xs, res_ys))

rgb_i = m.convert("RGB")


draw_(5)


res_img.save("image redarctor/result.png")
f.close()
print(h)
