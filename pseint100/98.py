

print("MENU DE OPCIONES DE UN TRIANGULO")
print("------------------------------")
print("1. Area de un triangulo, dada la base y la altura")
print("2. Base de un ttriangulo, dada la altura y el area")
print("3. Altura de un triangulo, dada la base y el area")
print("Selecciona una opcion : ")

OPC = int(input())

if (OPC == 1):
    print("BASE: ")
    base = float(input())
    print("ALTURA: ")
    altura = float(input())

    area = (base * altura)/2
    print("EL AREA ES: ",area)
elif (OPC == 2):
    print("ALTURA: ")
    altura = float(input())
    print("AREA: ")
    area = float(input())

    base = (area * 2)/altura
    print("LA BASE ES: ",base)
elif (OPC == 3):
    print("BASE: ")
    base = float(input())
    print("AREA: ")
    area = float(input())

    altura = (area * 2)/base
    print("LA BASE ES: ",altura)

