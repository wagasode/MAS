import numpy as np
import matplotlib.pyplot as plt

# --- 自由落下のシミュレーション --- #
# --- 運動方程式を数値的に解く --- #

G = 9.80665

t = 0.0
h = 0.01

v = float(input("初速度v0を入力："))
x = float(input("初期高度x0を入力："))
print(f"Time:{t:.7f}, X={x:.7f}, V={v:.7f}")

t_list = [t]
x_list = [x]

while x >= 0:
    t += h
    v += G * h
    x -= v * h
    print(f"Time:{t:.7f}, X={x:.7f}, V={v:.7f}")
    t_list.append(t)
    x_list.append(x)

plt.plot(t_list, x_list)
plt.show()
