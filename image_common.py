"""
画像を操作する共通メソッド
"""
from PIL import Image


def resize_to_width(img, width):
    """
    指定幅に合わせて画像をリサイズ
    """
    height = round(width*img.height/img.width)
    return img.resize((width, height))


def get_concat_v(img1, img2):
    """
    2つの画像を縦に並べて1つの画像を生成
    """
    dst = Image.new('RGB', (img1.width, img1.height + img2.height))
    dst.paste(img1, (0, 0))
    dst.paste(img2, (0, img1.height))
    return dst
