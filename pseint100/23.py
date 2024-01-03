suma = 0
print("INGRESE LA CANTIDAD DE NOTAS : ")
n = int(input())
for cont in range (1, n + 1):
    print("NOTA ",cont," : ")
    nota = int(input())
    suma = suma + nota
    
print ("PROMEDIO :", (suma/n))