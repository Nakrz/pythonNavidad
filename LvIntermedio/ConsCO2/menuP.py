import os
import dependencias




def mostrarMenu():
    print("CALCULADOR DE CO2 POR DEPENDENCIA")
    print("")
    print("1. Registrar Dependencia")
    print("2. Registrar Consumo por Dependencia")
    print("3. Ver CO2 Producido")
    print("4. Dependencia que Produce Mayor CO2")
    print("5. Salir")





def principalMen():
    while True:
        mostrarMenu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            dependencias.registrarDependencia()
            os.system("pause")
            os.system("cls")
        elif opcion == "2":
            dependencias.consumoDependencia()
            os.system("pause")
            os.system("cls")
        elif opcion == "3":
            dependencias.CO2Producido()
            os.system("pause")
            os.system("cls")
        elif opcion == "4":
            dependencias.MayorCO2Producido()
            os.system("pause")
            os.system("cls")
        elif opcion == "5":
            break   

principalMen()