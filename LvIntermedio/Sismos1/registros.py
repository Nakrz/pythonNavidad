
def registrarCiudad(ciudades):
    nombreCiudad = input("Ingrese el nombre de la ciudad: ")
    ciudades.append({"nombre": nombreCiudad, "sismos": []})
    print("Ciudad registrada exitosamente")
    

def registrarSismos(ciudades):
    nombreCiudad = input("Ingrese el nombre de la ciudad: ")
    for ciudad in ciudades:
        if ciudad["nombre"].upper() == nombreCiudad.upper():
            print("Por favor ingrese la magnitud de la siguiente manera: (4.5, 3.9, 3.2) ")
            magnitudSismo = float(input("Ingrese la magnitud del sismo: "))
            ciudad["sismos"].append(magnitudSismo)
            print("Sismo registrado en", nombreCiudad)
            return
    print("Ciudad no encontrada")
    
def sismosPorCiudad(ciudades):
    nombreCiudad = input("Ingrese el nombre de la ciudad: ")
    for ciudad in ciudades:
        if ciudad["nombre"].upper() == nombreCiudad.upper():
            print("Sismos en", nombreCiudad, ":", ciudad["sismos"])
            return
    print("Ciudad no encontrada")