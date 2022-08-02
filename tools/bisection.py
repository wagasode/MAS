# --- 二分法による方程式の解の計算 --- #

# --- global変数 --- #
A = 2         # 方程式の定数項　f(x)=x^2-a
LIMIT = 1e-20 # 終了条件

# --- f()関数 --- #
def f(x):
    return x**2 - A

# --- 初期設定 --- #
xp = float(input("二分法の上限値の初期値を入力："))
xn = float(input("二分法の下限値の初期値を入力："))

# --- 繰り返し処理 --- #
while (xp - xn) * (xp - xn) > LIMIT:
    xmid = (xp + xn) / 2
    if f(xmid) > 0:
        xp = xmid
    else:
        xn = xmid
    print(f"xn: {xn:.15f} - xp: {xp:.15f}")
print(f"xp - xn の自乗{(xp-xn)*(xp-xn)}が閾値{1e-20}を下回ったため処理を終了")
