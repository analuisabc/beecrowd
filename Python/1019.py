
n = int(input())
hora = n // 60**2
n = n - hora * 60**2

min = n // 60
n = n - min*60

seg = n

print('{}:{}:{}'.format(hora, min, seg))
