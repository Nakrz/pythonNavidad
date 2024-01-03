print("INGRESE CANTIDAD A COMPRAR : ")
cantidad=int(input())

if cantidad >= 1 and cantidad <= 3:
    costo = 15
elif cantidad >= 4 and cantidad <= 8:
    costo = 11
else:
    costo = 10

print("COSTO POR TECLADO : S/.",costo)
print("TOTAL A PAGAR     : S/.",costo*cantidad)