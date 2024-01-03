
tv_h = 0
tv_m = 0
muj = 0



print("CANTIDAD DE EMPLEADOS : ")
empleados = int(input())
print("")


for cont in range (1,empleados + 1):
    print("EMPLEADO Nro ",cont,"/",empleados)
    print("NOMBRE :")
    nombre=input()
    print("GENERO (H/M) :")
    genero=input().upper()
    print("VENTAS :")
    ventas=int(input())
    print("")
    
    
    if (genero == "H"):
        tv_h = tv_h + ventas
    else:
        tv_m = tv_m + ventas
        muj = muj + 1
        
print("TOTAL DE VENTAS HOMBRES : ",tv_h)
print("TOTAL DE VENTAS MUJERES : ",tv_m)
print("")
print("PORCENTAJE DE MUJERES   : ",(muj * 100/empleados)),"%"