# 【情報落ち】：絶対値が大きく異なる数値同士の演算において絶対値の小さい数値の影響が演算結果に反映されないことにより発生する誤差

# --- 初期設定 --- #
x = 1e10
y = 1e-8
temp = 0.0

# --- y(=1e-8)をx(=1e10)に1000万回加算する --- #
for i in range(10000000):
    x = x + y
print(x)

# --- y(=1e-8)を1000万回加算し、それをx(1e10)に加える --- #
for i in range(10000000):
    temp += y
x = 1e10
x += temp
print(x)
