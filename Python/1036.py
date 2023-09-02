d = input().split()
a, b, c = d
a = float(a)
b = float(b)
c = float(c)
delta = (b*b) - 4*a*c
if (a == 0.0 or delta < 0):
    print("Impossivel calcular")
else:
    r1 = ((-1)*b + (delta**(1/2)))/(2*a)
    r2 = ((-1)*b - (delta**(1/2)))/(2*a)
    print("R1 = %.5lf"%r1)
    print("R2 = %.5lf"%r2)