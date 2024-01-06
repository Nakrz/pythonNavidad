
def informeDeRiesgo(ciudades):
    for ciudad in ciudades:
        sismosPorCd = ciudad["sismos"]
        if sismosPorCd:
            ultimoSR = sismosPorCd[-1]
            if ultimoSR < 2.5:
                color = "Amarillo"
                riesgo = "Sin riesgo"
            elif 2.5 <= ultimoSR <= 4.5:
                color = "Naranja"
                riesgo = "Riesgo medio"
            else:
                color = "Rojo"
                riesgo = "Riesgo alto"
            print(f"{ciudad['nombre']} [{ultimoSR}] [{color}] [{riesgo}]")
