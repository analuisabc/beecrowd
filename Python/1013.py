import math
A, B, C = input().split()
A = int(A)
B = int(B)
C = int(C)
m1 = (A + B + abs(A - B)) / 2
mf = (m1 + C + abs(m1 - C)) / 2
print("{} eh o maior".format(int(mf)))