import os

dependencias = {}

def registrarDependencia():
    nombreDependencia = input("Ingrese el nombre de la dependencia: ").upper()
    dependencias[nombreDependencia] = {}
    print(f"La dependencia '{nombreDependencia}' ha sido registrada.")
    os.system("pause")
    os.system("cls")


def consumoDependencia():
    nombreDependencia = input("Ingrese el nombre de la dependencia: ").upper()
    
    
    if nombreDependencia in dependencias:
        dispositivo = input("Ingrese el nombre del dispositivo: ")
        potenciaDispositivo = float(input("Ingrese la potencia del dispositivo en vatios: "))
        tiempoUso = float(input("Ingrese el tiempo de uso del dispositivo en horas: "))
        conMensual = int(input("Ingrese el número de consumo mensual: "))
    
    factorEmiElectricidad =  0.126
    
    consumoCO2 = (potenciaDispositivo * tiempoUso * conMensual) / 1000  
    emisionesCO2 = conMensual * factorEmiElectricidad
    
    
    dependencias[nombreDependencia][dispositivo] = {
            'potencia': potenciaDispositivo,
            'tiempouso': tiempoUso,
            'consumomensual': conMensual,
            'consumoCO2': consumoCO2,
            'emisionesCO2': emisionesCO2
        }
      
        
    print("Registro de Consumo realizado")
    os.system("pause")
    os.system("cls ")



def CO2Producido():
    nombreDependencia = input("Ingrese el nombre de la dependencia: ").upper()
    
    
    if nombreDependencia in dependencias:
        totalCO2Dependencia = 0
        for dispositivo, valores in dependencias[nombreDependencia].items():
            consumoCO2 = (valores['potencia'] * valores['tiempouso'] * valores['consumomensual']) / 1000
            totalCO2Dependencia += consumoCO2
        
        print(f"La dependencia '{nombreDependencia}' ha producido un total de {totalCO2Dependencia:.2f} CO2.")
    else:
        print(f"La dependencia '{nombreDependencia}' no ha sido registrada.")
        
        
def MayorCO2Producido():
    mayorDependencia = None
    mayorEmisiones = 0

    for dependencia, dispositivos in dependencias.items():
        totalCO2Dependencia = sum(valores['consumoCO2'] for valores in dispositivos.values())
        if totalCO2Dependencia > mayorEmisiones:
            mayorEmisiones = totalCO2Dependencia
            mayorDependencia = dependencia

    if mayorDependencia:
        print(f"La dependencia que produce mayor CO2 es '{mayorDependencia}' con un total de {mayorEmisiones:.2f} CO2.")