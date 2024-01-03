
boni = 0
sueldoF = 0

print("09. CALCULAR EL SUELDO FINAL")
print("Ingrese Nombre   :")
nom = input()
print("Sueldo Basico    : S/.")
sueldoB = int(input())
print("Numero de Hijos  : ")
hijos = int(input())

if (hijos > 0):
    boni = sueldoB * 0.7
    
sueldoF = sueldoB + boni

print("")
print("BONIFICACION : S/. ",boni)
print("SUELDO FINAL : S/. ",sueldoF)
