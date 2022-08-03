import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# --- 自由落下のシミュレーション --- #
# --- 運動方程式を数値的に解く --- #

G = 9.80665

t = 0.0
h = 0.01

def f(x, t):
    return [x[1], -G]

v = float(input("初速度v0を入力："))
x = float(input("初期高度x0を入力："))
print(f"[Time]: {t:.2f}  [x]: {x:.2f}  [v]: {v:.2f}")
x0 = [x, v]
t = np.arange(0, 4.53, 0.01)
x = odeint(f, x0, t)
print(x)

# TODO: 2次配列の縦方向リスト
# plt.plot()
# plt.show()
