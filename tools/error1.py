# --- 計算誤差の例題 --- #
# 【桁落ち誤差】：値のほぼ等しい数値同士の減算など、有効数字が損なわれることにより発生する誤差

import math

# --- 通常の減算と、分子を有理化する方法 --- #
def calc_res(x):
    res1 = math.sqrt(x + 1) - math.sqrt(x)
    res2 = 1 / (math.sqrt(x + 1) + math.sqrt(x))
    return res1, res2

# --- 結果出力 --- #
def print_result(normal, rational):
    print(f"通常の計算方法　　　　　：{normal}")
    print(f"分子を有理化した計算方法：{rational}")
    print("-"*10)

# --- main実行部 --- #
x_list = [1e15, 1e16]

for x in x_list:
    print(f"x={str(x)}の場合")
    res1, res2 = calc_res(x)
    print_result(res1, res2)
