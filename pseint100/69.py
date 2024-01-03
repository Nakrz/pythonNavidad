
print("MOSTRAR EL PORCENTAJE DE ALUMNOS APROBADOS")
print("")
print("INGRESE CANTIDAD DE ALUMNOS APROBADOS : ")
apro = int(input())
print("INGRESE CANTIDAD DE ALUMNOS DESAPROBADOS : ")
desa = int(input())
print("")


porA = (apro*100)/(apro+desa)
porD = (desa*100)/(apro+desa)

print("APROBADOS : ", (round(porA*100)/100)), "%"
print("DESAPROBADOS : ", (round(porD*100)/100)), "%"