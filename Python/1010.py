p1 = input().split()
p2 = input().split()
np1 = int(p1[1])
vp1 = float(p1[2])
np2 = int(p2[1])
vp2 = float(p2[2])
print('VALOR A PAGAR: R$ {:.2f}'.format(np1 * vp1 + np2 * vp2))