import informes
import registros
import os

def menuPrincipal():
    ciudades = []
    while True:
        print("Centro de prevención de sismos de Colombia:")
        print("")
        print("1. Registrar Ciudad")
        print("2. Registrar Sismo")
        print("3. Buscar Sismos por Ciudad")
        print("4. Informe de Riesgo")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            registros.registrarCiudad(ciudades)
            os.system("pause")
            os.system("cls")
        elif opcion == "2":
            registros.registrarSismos(ciudades)
            os.system("pause")
            os.system("cls")
        elif opcion == "3":
            registros.sismosPorCiudad(ciudades)
            os.system("pause")
            os.system("cls")
        elif opcion == "4":
            informes.informeDeRiesgo(ciudades)
            os.system("pause")
            os.system("cls")
        elif opcion == "5":
            print("Saliendo...")
            break
        else:
            print("Opcion invalida, selecciona una opcion correcta [1,2,3,4,5]")

def prevencionSismosCol():
    menuPrincipal()
    
prevencionSismosCol()