import math
import sys
a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])
d = b**2 - 4 * a * c
if d < 0:
    print("Корней нет")
elif d > 0:
    x1 = (-b + math.sqrt(d))/(2*a)
    x2 = (-b - math.sqrt(d))/(2*a)
    print(int(x1))
    print(int(x2))
else:
    x1 = (-b + math.sqrt(d)) / (2 * a)
    print(int(x1))
