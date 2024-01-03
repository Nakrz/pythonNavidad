

print("Ingrese numero de 3 cifras :")
num = int(input())

c1 = (num - (num%100)) / 100
r1 = num % 100
c2 = (r1 - (r1 %10)) / 10
r2 = r1 % 10

if (num == ((r2 * 100)+(c2*10) + c1 )):
    print("NUMERO CAPICUA")
else:
    print("NO ES CAPICUA")


