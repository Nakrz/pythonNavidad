

diax = 21
mesx = 10
aniox = 2023
edad = 0

for x in range(1, 10,1):
    dni = input("DNI: ")
    print("")
    dia = int(input("DÍA DE NACIMIENTO : "))
    print("")
    mes = int(input("MES DE NACIMIENTO : "))
    print("")
    anio = int(input("AÑO DE NACIMIENTO : "))
    print("")
    genero = input("GÉNERO (H/M) : ")
    print("")
    print("fecha actual: ",diax,"/",mesx,"/",aniox)
    edad = aniox - anio
    if (mes > mesx ):
        edad = edad -1
    elif (mes == mesx and dia > diax):
        edad = edad -1
    print("EDAD: ",edad, " AÑOS")
    if (edad>=8):
        print("RECIBE TABLET")
        print("")
    elif (edad == 6):
        if(genero == "H"):
            print("RECIBE CARRITO")
    else:
        print("RECIBE MUÑECA")
    