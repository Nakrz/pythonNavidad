
print("04. CALCULAR BONIFICACION")
print("")
print("INGRESE MONTO DE VENTA : $")
venta = int(input())
if (venta > 2000):
    print("BONIFICACION 10% : $.", (venta*0.10))
else:
    print("BONIFICACION 50% : $.", (venta*0.50))