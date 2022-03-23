"""
システムに関する共通関数
"""
import sys


def check_args(num):
    """
    引数の数をチェック
    """
    if len(sys.args) != num:
        print("引数は"+(num-1)+"つ指定してください")
        sys.exit()
