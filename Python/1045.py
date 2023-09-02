a,b,c = list(map(float,input().split()))
if(a < b): #ordenando
    aux = a
    a = b
    b = aux
if(b < c):
    aux = b
    b = c
    c = aux
if(a < b):
    aux = a
    a = b
    b = aux
if (a >= (b+c)):
    print ("NAO FORMA TRIANGULO")
else:
    if (a**2 == ((b**2)+(c**2))):
        print ("TRIANGULO RETANGULO")
    elif (a**2 > ((b**2)+(c**2))):
        print ("TRIANGULO OBTUSANGULO")
    elif (a**2 < ((b**2)+(c**2))):
        print ("TRIANGULO ACUTANGULO")

    if(a == b and b == c):
        print("TRIANGULO EQUILATERO")
    elif(a == b or b == c):
        print("TRIANGULO ISOSCELES")