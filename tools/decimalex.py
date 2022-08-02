# --- decimal Moduleを利用した10進数表現 --- #

from decimal import *

print(Decimal("0.1"))

# --- Decimal(0.1)を100万回加算 --- #
x = Decimal("0.0")
for i in range(100000):
    x += Decimal("0.1")
print(x)
