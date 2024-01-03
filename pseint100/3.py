import os

total = 0
desc = 0


for cont in range (1,10):
    consumo = int(input(f"CONSUMO {cont} : $"))
    total = total + consumo
    
if (total > 50):
    desc = total *0.07
os.system("cls")

print("CONSUMO TOTAL : $",total)
print("DESCUENTO : $",desc)
print("PAGO TOTAL : $",total-desc)
    