
def informeDeRiesgo(ciudades):
    for ciudad in ciudades:
        sismos_ciudad = ciudad["sismos"]
        if sismos_ciudad:
            promedio = sum(sismos_ciudad) / len(sismos_ciudad)
            if promedio < 2.5:
                color = "Amarillo"
                riesgo = "Sin riesgo"
            elif 2.5 <= promedio <= 4.5:
                color = "Naranja"
                riesgo = "Riesgo medio"
            else:
                color = "Rojo"
                riesgo = "Riesgo alto"
            print(f"{ciudad['nombre']} [{promedio}] [{color}] [{riesgo}]")