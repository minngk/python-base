# 引数でPATHを受け取り画像を白黒変換する

from PIL import Image, ImageFilter
import sys

if len(sys.argv) != 2:
    print("引数は1つ指定してください")
    exit()

img_path = sys.argv[1]
org_img = Image.open(img_path)

converted_img = org_img.convert('L').filter(ImageFilter.GaussianBlur())
# converted_img.show()

converted_img_path = '.'.join(img_path.split(".")[0:-1]) + "_conv.jpg"
converted_img.save(converted_img_path, quantiles=95)