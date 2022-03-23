'''
引数でPATHを受け取り画像を色変換したものと並べる
参考：https://pillow.readthedocs.io/en/stable/handbook/tutorial.html#processing-individual-bands
'''

import sys
from PIL import Image
import image_common as ic
import sys_common as sc

sc.check_args(2)

img_path = sys.argv[1]
org_img = ic.resize_to_width(Image.open(img_path), 128)
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

    new_img = ic.get_concat_v(new_img, converted_img)

NEW_IMG_PATH = '.'.join(img_path.split(".")[0:-1]) + "_change_color.jpg"
new_img.save(NEW_IMG_PATH, quantiles=95)
