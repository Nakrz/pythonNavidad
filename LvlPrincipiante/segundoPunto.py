
print("********** CENTRO DE SALUD DE CAMPUSLANDS ***********")
print ("")
nombreEstudiante =input("Introduzca el nombre del estudiante: ")
edadEstudiante = input("Introduzca la edad del estudiante: ")
peso = int(input("Introduzca el peso del estudiante (kg): "))
altura = float(input("Introduzca la altura del estudiante (m2): "))
imc = (peso / altura ** 2 )


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
        
            
categoria = categoriaIMC(imc)   

print("Nombre: ",nombreEstudiante)
print("Edad: ",edadEstudiante)
print("Peso: ",peso,"kg")
print("Altura: ",altura, "cm")
print(f"IMC: {imc:.2f}")
print(f"Categoria IMC: {categoria}")
