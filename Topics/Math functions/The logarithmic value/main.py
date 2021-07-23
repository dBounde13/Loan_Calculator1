import math

a, b = abs(int(input())), int(input())

if b > 1:
    print(round(math.log(a, b), 2))
else:
    print(round(math.log(a), 2))

