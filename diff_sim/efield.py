# --- 電界中の荷電粒子のシミュレーション --- #

import math
import matplotlib.pyplot as plt
import numpy as np

Q          = (((0.0, 0.0), 3.0), ((0.0, 0.0), 0.0))
TIME_LIMIT = 20.0
R_LIMIT    = 0.1
H          = 0.01

t = 0.0
for qi in Q:
    plt.plot(qi[0][0], qi[0][1], ".")

vx = float(input("初速度v0xを入力："))
vy = float(input("初速度v0yを入力："))
x  = float(input("初期位置xを入力："))
y  = float(input("初期位置yを入力："))

print(f"[Time]: {t:.3f}  [x, y]: ({x:.2f}, {y:.2f})  [vx, vy]:({vx:.2f}, {vy:.2f})")

x_list = [x]
y_list = [y]

while t < TIME_LIMIT:
    t = t + H
    rmin = float("inf")
    for qi in Q:
        rx = qi[0][0] - x
        ry = qi[0][0] - y
        r  = math.sqrt(rx**2 + ry**2)
        if r < rmin:
            rmin = r
        vx += (rx / r / r / r * qi[1]) * H
        vy += (ry / r / r / r * qi[1]) * H
    x += vx * H
    y += vy * H
    print(f"[Time]: {t:.3f}  [x, y]: ({x:.2f}, {y:.2f})  [vx, vy]:({vx:.2f}, {vy:.2f})")
    x_list.append(x)
    y_list.append(y)
    if rmin < R_LIMIT:
        break

plt.plot(x_list, y_list)
plt.show()
