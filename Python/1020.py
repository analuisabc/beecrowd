n= int(input())
a = n / 365
ra = n%365
rm = ra%30
m = ra/30
d = rm%30
print("{} ano(s)".format(int(a)))
print("{} mes(es)".format(int(m)))
print("{} dia(s)".format(int(d)))