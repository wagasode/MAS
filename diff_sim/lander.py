# --- 逆噴射する着陸線のシミュレーション --- #

import numpy as np
import matplotlib.pyplot as plt

F = 1.5     # 逆噴射の加速度
G = 9.80665

def retro_fire(t, tf):
    if t >= tf:
        return -F * G
    else:
        return 0.0

t = 0.0
h = 0.01

v = float(input("初速度v0を入力："))
x0 = float(input("初期高度x0を入力："))
tf = float(input("逆噴射開始時刻tfを入力："))
x = x0
print(f"Time: {t:.3f}  x: {x:.7f}  v: {v:.7f}")
t_list = [t]
x_list = [x]

while (x>0) and (x<=x0):
    t += h
    v += (G + retro_fire(t, tf)) * h
    x -= v * h
    print(f"Time: {t:.3f}  x: {x:.7f}  v: {v:.7f}")
    t_list.append(t)
    x_list.append(x)

plt.plot(t_list, x_list)
plt.show()
