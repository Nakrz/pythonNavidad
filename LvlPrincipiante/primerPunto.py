
print("Bienvenido, por favor ingrese los numeros que desea sumar")
digito1 = int(input("Ingrese el primer numero: "))
digito2 = int(input("Ingrese el siguiente numero: "))
digito3 = int(input("Ingrese el ultimo numero: "))

resultadoSuma = (digito1 + digito2 + digito3)

if resultadoSuma <0:
    print("Operacion incorrecta, por favor introduzca numeros positivos")
else:
    print("El resultado de la suma de los numeros ingresados es:",resultadoSuma)


