# --- sympy Moduleを利用して方程式の解を計算 --- #

from sympy import *

# --- main実行部 --- #
var("x")
equation = Eq(x**3 + 2*x**2 + (-5)*x + (-6), 0)
answer = solve(equation)
print(answer)
