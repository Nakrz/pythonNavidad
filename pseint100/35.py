
num = 0
val = 1
contador = 1


print("MUESTRA GRAFICA DE NUMEROS COMO TRIANGULO.")
while (num < 3):
    print("INGRESE NUMERO")
    num = int(input())
print("")


for x in range(1, num + 1):
    for y in range(num - x):
        print(" ", end="")
    
    for z in range(x * 2 - 1):
        print(val, end="")
        val = (val + 1) % 10
    print("")
