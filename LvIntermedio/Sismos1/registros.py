
import os


def registrarCiudad(ciudades):
    nombreCiudad = input("Ingrese el nombre de la ciudad: ")
    ciudades.append({"nombre": nombreCiudad, "sismos": []})
    print("Ciudad registrada exitosamente")
    

def registrarSismos(ciudades):
    os.system ('cls')
    while True:
        nombreCiudad = input("Ingrese el nombre de la ciudad: ")
        for ciudad in ciudades:
            if ciudad["nombre"].upper() == nombreCiudad.upper():
                    if len(ciudad["sismos"]) < 5:
                        os.system("cls")
                        print("Por favor ingrese la magnitud de la siguiente manera: (4.5, 3.9, 3.2) ")
                        magnitudSismo = float(input("Ingrese la magnitud del sismo: "))
                        ciudad["sismos"].append(magnitudSismo)
                        print("Sismo registrado en", nombreCiudad)
                    else:
                        print("Ya se han registrado 5 sismos para esta ciudad")
                    break
        else:
            print("La ciudad no ha sido registrada")    

            
        respuesta = input("¿Desea añadir otro sismo? S(si) o N (No)").upper()
        if respuesta != 'S':
            break
                   
      
                    

def sismosPorCiudad(ciudades):
    nombreCiudad = input("Ingrese el nombre de la ciudad: ")
    for ciudad in ciudades:
        if ciudad["nombre"].upper() == nombreCiudad.upper():
            print("Sismos en", nombreCiudad, ":", ciudad["sismos"])
            return
    print("Esta ciudad no ha sido registrada")
