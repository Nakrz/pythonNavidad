sueldoBase = 0
num_hijos = 0
dias_no_laborables = 0
sueldo_final=0


print("CALCULAR EL SUELDO FINAL DE UN EMPLEADO")
print("")
print("Ingrese Sueldo Base : $")
sueldoBase = int(input())
print("Ingrese Numero de Hijos : $")
num_hijos = int(input())
print("Ingrese Dias no Laborables Trabajados : $")
dias_no_laborables = int(input())

sueldo_final = sueldoBase +(num_hijos*100)+(dias_no_laborables*25)


print("")
print("SUELDO FINAL : $ ",sueldo_final)