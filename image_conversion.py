"""
引数でPATHを受け取り画像を白黒変換した画像と並べる
"""

import sys
from PIL import Image, ImageFilter
import image_common as ic
import sys_common as sc

sc.check_args(2)

img_path = sys.argv[1]
org_img = Image.open(img_path)

converted_img = org_img.convert('L').filter(ImageFilter.GaussianBlur())
# converted_img.show()

new_img = ic.get_concat_v(org_img, converted_img)
NEW_IMG_PATH = '.'.join(img_path.split(".")[0:-1]) + "_conv.jpg"
new_img.save(NEW_IMG_PATH, quantiles=95)
