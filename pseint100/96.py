

print("Cantidad a comprar : ")
cantidad=int(input())

if cantidad >= 1 and cantidad <= 3:
    costo = 15
elif cantidad >= 4 and cantidad <= 8:
    costo = 11
else:
    costo = 10

print("Costo por teclado : S/.",costo)
print("Total a Pagar : S/.",costo*cantidad)

