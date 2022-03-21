# 引数でPATHを受け取り画像を白黒変換した画像と並べる

from PIL import Image, ImageFilter
import sys

def get_concat_v(img1, img2):
    dst = Image.new('RGB', (img1.width, img1.height + img2.height))
    dst.paste(img1, (0,0))
    dst.paste(img2, (0, img1.height))
    return dst

if len(sys.argv) != 2:
    print("引数は1つ指定してください")
    exit()

img_path = sys.argv[1]
org_img = Image.open(img_path)

converted_img = org_img.convert('L').filter(ImageFilter.GaussianBlur())
# converted_img.show()

new_img = get_concat_v(org_img, converted_img)
new_img_path = '.'.join(img_path.split(".")[0:-1]) + "_conv.jpg"
new_img.save(new_img_path, quantiles=95)