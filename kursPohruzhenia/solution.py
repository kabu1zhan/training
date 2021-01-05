import sys
b = '#'
d = ' '
a = int(sys.argv[1])
if a > 0:
    for x in range(1, a+1):
        print(d * (a - x), b * x, sep='')
else:
    print("Введите число больше нуля")
