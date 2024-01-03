

import os

print("********** CENTRO DE SALUD DE CAMPUSLANDS ***********")
print("")

def datosEstudiantes ():
    estudiantes = []
    for est in range (20):
        nombreEstudiante = input(f"Nombre del estudiante {est+1}: ")
        edadEstudiante = input("Introduzca la edad del estudiante: ")
        peso = int(input("Introduzca el peso del estudiante (kg): "))
        altura = float(input("Introduzca la altura del estudiante (m2): "))
        imc = (peso / altura ** 2 )
        categoria = categoriaIMC(imc)
        estudiantes.append({"Nombre": nombreEstudiante, "Edad": edadEstudiante, "Peso": peso, "Altura": altura, "IMC": imc, "Categoria IMC": categoria})    
    return estudiantes



def categoriaIMC (imc):
    if imc >= 18.5 and imc <= 24.9:
        return ("Normal")
        
    elif imc >= 25 and imc <= 29.9:
        return("Sobrepeso")
        
    elif imc >= 30 and imc <= 34.9:
        return("Obesidad I")
        
    elif imc >= 35 and imc <= 39.9:
        return("Obesidad II")
        
    elif imc >= 40:
        return("Obesidad III")


estudiantes = datosEstudiantes()
os.system('cls')


contadorIMC = {'Normal': 0, 'Sobrepeso': 0, 'Obesidad I': 0, 'Obesidad II': 0, 'Obesidad III': 0}

for estudiante in estudiantes:
    categoria = estudiante["Categoria IMC"]
    contadorIMC[categoria] = + 1
    
print("Numero de estudiantes por categoria de IMC: ")
print("")

for categoria, contador in contadorIMC.items():
    print(f"{categoria}: {contador}")
