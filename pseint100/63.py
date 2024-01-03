

print("")
print("costo de la Casa : S/.")
costo = int(input())
print("Valor del IVA     : %. ")
iva = int(input())
print("")
TotPagar = costo + (costo*(iva/100))
print("IVA DE ",iva,"%     :S/.",(costo*(iva/100)))
print("TOTAL A PAGAR       :",TotPagar)