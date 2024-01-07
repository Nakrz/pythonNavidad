import os
from jugadoresp import registrarJugador, verificacionDeInicio, iniciarPartidos
from partidosp import puntajesPartidos, mostrarPuntajes, ganadorPorCategoria



def menuPrograma():
    while True:
        print("")
        print("TORNEO DE TENIS DE MESA")
        print("")
        print("1. Registro de Jugador por Categoria")
        print("2. Verificacion de Jugadores registrados")
        print("3. Ingresar Puntuaciones")
        print("4. Visor de Puntajes")
        print("5. Ganador por Categoria")
        print("6. Salir")
        opcion = input("Seleccione una opcioon: ")

        if opcion == "1":
            registrarJugador()
            os.system("pause")
            os.system("cls")
        elif opcion == "2":
            iniciarPartidos()
            os.system("pause")
            os.system("cls")
            pass  
        elif opcion == "3":
            puntajesPartidos()
            os.system("pause")
            os.system("cls")
            pass  
        elif opcion == "4":
            mostrarPuntajes()
            os.system("pause")
            os.system("cls")
            pass  
        elif opcion == "5":
            ganadorPorCategoria()
            os.system("pause")
            os.system("cls")
        elif opcion == "6":
            print("Saliendo del progama....")
            break

menuPrograma()
