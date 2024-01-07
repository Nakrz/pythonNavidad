from jugadoresp import jugadoresPorCateg



def calcularPuntosFavor(puntosRealizados, puntosRecibidos, ganadorPart):
    puntosFavor = puntosRealizados - puntosRecibidos
    if ganadorPart:
        puntosFavor = puntosFavor + 2  
    return puntosFavor



def puntajesPartidos():
    
    print("INTRODUCIR PUNTAJES")
    idJugador1 = int(input("ID del Jugador 1: "))
    idJugador2 = int(input("ID del Jugador 2: "))
    
    nombreJugador1 = ""
    nombreJugador2 = ""
    
    jugador1Encontrado = False
    jugador2Encontrado = False

    for categoria, jugadores in jugadoresPorCateg.items():
        for jugador in jugadores:
            if jugador['id'] == idJugador1:
                nombreJugador1 = jugador['nombre']
                jugador1Encontrado = True
            elif jugador['id'] == idJugador2:
                nombreJugador2 = jugador['nombre']
                jugador2Encontrado = True

    if not jugador1Encontrado or not jugador2Encontrado:
        print("Uno o ambos IDs de jugadores no estan registrados")
        return

    for categoria, jugadores in jugadoresPorCateg.items():
        for jugador in jugadores:
            if jugador['id'] == idJugador1:
                nombreJugador1 = jugador['nombre']
            elif jugador['id'] == idJugador2:
                nombreJugador2 = jugador['nombre']

    setsGanados1 = int(input(f"Sets ganados por {nombreJugador1}: "))
    setsGanados2 = int(input(f"Sets ganados por {nombreJugador2}: "))
    puntosRealizados1 = int(input(f"Puntos realizados por {nombreJugador1}: "))
    puntosRecibidos1 = int(input(f"Puntos recibidos por {nombreJugador1}: "))
    puntosRealizados2 = int(input(f"Puntos realizados por {nombreJugador2}: "))
    puntosRecibidos2 = int(input(f"Puntos recibidos por {nombreJugador2}: "))



    puntosFavor1 = calcularPuntosFavor(puntosRealizados1, puntosRecibidos1, setsGanados1 > setsGanados2)
    puntosFavor2 = calcularPuntosFavor(puntosRealizados2, puntosRecibidos2, setsGanados2 > setsGanados1)



    for categoria, jugadores in jugadoresPorCateg.items():
        for jugador in jugadores:
            if jugador['id'] == idJugador1:
                jugador['partidos ganados'] = setsGanados1 if setsGanados1 > setsGanados2 else 0
                jugador['partidos perdidos'] = setsGanados2 if setsGanados2 > setsGanados1 else 0
                jugador['puntos a favor'] = puntosFavor1
                jugador['total puntos'] = puntosFavor1
                
                
            elif jugador['id'] == idJugador2:
                jugador['partidos ganados'] = setsGanados2 if setsGanados2 > setsGanados1 else 0
                jugador['partidos perdidos'] = setsGanados1 if setsGanados1 > setsGanados2 else 0
                jugador['puntos a favor'] = puntosFavor2
                jugador['total puntos'] = puntosFavor2


def mostrarPuntajes():
    print("")
    print("VISOR DE PUNTAJES")
    print("")
    print("Id    Jugador  PG   PP   PA   TP")
    for categoria, jugadores in jugadoresPorCateg.items():
        for jugador in jugadores:
            idJugador = jugador['id']
            nombre = jugador['nombre']

            partidosGanados = jugador.get('partidos ganados', 0)
            partidosPerdidos = jugador.get('partidos perdidos', 0)
            puntosAFavor = jugador.get('puntos a favor', 0)
            totalPuntos = jugador.get('total puntos', 0)

            print(f"{idJugador:<5}{nombre:<10}{partidosGanados:<5}{partidosPerdidos:<5}{puntosAFavor:<5}{totalPuntos}")


def ganadorPorCategoria():
    print("")
    print("Ganador por Categoria")
    print("")
    for categoria, jugadores in jugadoresPorCateg.items():
        totalPuntos = -1
        ganador = None
        for jugador in jugadores:
            if 'total puntos' in jugador and jugador['total puntos'] > totalPuntos:
                totalPuntos = jugador['total puntos']
                ganador = jugador['nombre']
        if ganador:
            print(f"Categoria: {categoria} -> Ganador: {ganador}")
        else:
            print(f"No se encontro jugadores en la categoria {categoria}")