

print("Ingrese Nota 1 : ")
N1= int(input())
print("Ingrese Nota 2 : ")
N2= int(input())
print("Ingrese Nota 3 : ")
N3= int(input())

prom = round((N1+N2+N3)/3)

if prom >= 0 and prom <= 10:
    print("NIVEL MALO")
elif prom >= 11 and prom <= 13:
    print("NIVEL REGULAR")
elif prom >= 14 and prom <= 16:
    print("NIVEL BUENO")
elif prom >= 17 and prom <= 20:
    print("NIVEL MUY BUENO")
    
    