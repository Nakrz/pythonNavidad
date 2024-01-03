
sumaP = 0
sumaI = 0

print ("INGRESE NUMERO : ")
num = int(input())

for x in range (1, num + 1):
    if x % 2 == 0:
        sumaP = sumaP + x
    else:
        sumaI = sumaI + x
        
print("Suma de pares   : " , sumaP)
print("Suma de impares : ",  sumaI)