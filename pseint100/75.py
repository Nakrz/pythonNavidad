

print("MONTO DE COMPRA : S/. ")
monto = int(input())

if (monto >= 350):
    desct = monto * 0.35
    print("DESCUENTO ES DE 35% : S/.",desct)
else:
    desct = monto * 0.10
    print("DESCUENTO ES DE 10 : S/.",desct)
    
    
print("MONTO A PAGAR : S/.", (monto - desct))