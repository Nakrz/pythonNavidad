

IGV = 0
monto = 0
print("05. CALCULAR IGV SEGUN EL MONTO DE COMPRA")
print("INGRESE PRECIO : S/")
precio=int(input())
print("INGRESE CANTIDAD : ")
cant=int(input())
monto = (precio * cant)

if (monto > 100):
    IGV = monto * 0.18
    
print("")
print("TOTAL               : S/.",monto)
print("IGV 18%             : S/.",IGV)
print("TOTAL A PAGAR       : S/.",(monto + IGV))


