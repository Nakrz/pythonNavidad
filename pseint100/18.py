

tem = ""
print("INGRESE NUMERO : ")
num = input() 

tem = num[::-1] 

print("")
print("NUMERO INGRESADO : ", num)
print("NUMERO CAMBIADO  :", tem)
print("")

if num == tem:
    print("SI ES UN NUMERO CAPICUA")
else:
    print("NO ES UN NUMERO CAPICUA")

