jugadoresPorCateg = {
    "Novato": [],
    "Intermedio": [],
    "Avanzado": []
}


def categoriaJugadores(edad):
    if edad >= 15 and edad <= 16:
        return "Novato"
    elif edad >= 17 and edad <= 20:
        return "Intermedio"
    elif edad > 20:
        return "Avanzado"

def registrarJugador():
    
    print("REGISTRO DE JUGADORES POR CATEGORIA")
    print("")
    
    idJugador = int(input("Ingrese el Id del Jugador: "))
    for jugadores in jugadoresPorCateg.values():
        for jugador in jugadores:
            if jugador['id'] == idJugador:
                print("Este ID ya esta siendo utilizado por otro jugador, ingresa otro...")
                return registrarJugador()
            
    nombre = input("Ingrese el Nombre del Jugador: ")
    edad = int(input("Ingrese la Edad del Jugador: "))
    categoria = categoriaJugadores(edad)
    
    jugadoresPorCateg[categoria].append({"id":idJugador,"nombre": nombre, "edad": edad})
    print("Jugador registrado en la categoria", categoria)
    
    
def verificacionDeInicio():
    global jugadoresPorCateg

    for categoria, jugadores in jugadoresPorCateg.items():
        if len(jugadores) >= 3:
            return True
    return False

def iniciarPartidos():
    jugadores = jugadoresPorCateg.get("Novato", []) + jugadoresPorCateg.get("Intermedio", []) + jugadoresPorCateg.get("Avanzado", [])
    
    
    
    
    if verificacionDeInicio():
        for jugador in jugadores:
            print("")
            print(f"ID: {jugador['id']}, Nombre: {jugador['nombre']}, Edad: {jugador['edad']}")
            print("")
        print("El limite minimo de jugadores ha sido alcanzado, ahora los partidos pueden comenzar")
    else:
        print("No se pueden iniciar los partidos, aun faltan jugadores en algunas categorias")
    

iniciarPartidos()