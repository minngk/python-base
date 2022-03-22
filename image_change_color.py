# 引数でPATHを受け取り画像を色変換したものと並べる
# 参考：https://pillow.readthedocs.io/en/stable/handbook/tutorial.html#processing-individual-bands

from PIL import Image
import sys


def get_concat_v(img1, img2):
    dst = Image.new('RGB', (img1.width, img1.height + img2.height))
    dst.paste(img1, (0, 0))
    dst.paste(img2, (0, img1.height))
    return dst


def resize_to_width(img, width):
    height = round(width*img.height/img.width)
    return img.resize((width, height))


if len(sys.argv) != 2:
    print("引数は1つ指定してください")
    exit()

img_path = sys.argv[1]
org_img = resize_to_width(Image.open(img_path), 128)
new_img = org_img.copy()

for i in range(3):
    # split the image into individual bands
    source = org_img.split()

    # select regions where red is less than 100
    mask = source[(2-i)].point(lambda i: i < 100 and 255)

    # process the green band
    out = source[i].point(lambda i: i * 0.7)

    # paste the processed band back, but only where red was < 100
    source[i].paste(out, None, mask)

    # build a new multiband image
    converted_img = Image.merge(org_img.mode, source)

    new_img = get_concat_v(new_img, converted_img)

new_img_path = '.'.join(img_path.split(".")[0:-1]) + "_change_color.jpg"
new_img.save(new_img_path, quantiles=95)
