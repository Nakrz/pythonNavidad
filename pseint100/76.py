
print("INGRESE NUMERO 01 : ")
n1 = int(input())
print("INGRESE NUMERO 02 : ")
n2 = int(input())
print("INGRESE NUMERO 03 : ")
n3 = int(input())


if (n1 > n2):
    medio = n1
    xtem = n2
else:
    medio = n2
    xtem = n1

if (medio > n3):
    medio = n3
if (medio < xtem):
    medio = xtem

print("EL NUMERO MEDIO ES: ",medio)