



xpro = 0

for cont in range (1,6):
    print("NOMBRE: ")
    nom= input()
    print("PROMEDIO: ")
    pro = int(input())
    if xpro < pro:
        xpro = pro
        xnom = nom
    
print("ALUMNO CON MAYOR NOTA: ", xnom)
print("PROMEDIO             :  ", xpro)