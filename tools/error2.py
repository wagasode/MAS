# 【丸め誤差】：有限桁数の２進数で実数を表現する際に発生する誤差

print(0.1)

# --- 0.1を100万回加算する --- #
x = 0.0
for i in range(1000000):
    x = x + 0.1

print(x)
