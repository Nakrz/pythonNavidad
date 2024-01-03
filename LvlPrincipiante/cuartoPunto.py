totalNumeros = 0
par = 0
impar = 0

menorDiez = 0
numVeinte = 0
mayorCien = 0

sumaPares = 0
sumaImpares = 0


while True: 
        digitos = int(input("Numero: "))
    

        totalNumeros = totalNumeros + 1
        
    
        if (digitos % 2) == 0:
            par = par + 1
            sumaPares = sumaPares + digitos
        else:
            impar += 1
            sumaImpares = sumaImpares + digitos
        
           
            
        if digitos < 10:
            menorDiez = menorDiez + 1
        if digitos >= 20 and digitos <= 50:
           numVeinte = numVeinte + 1      
        if digitos > 100:
          mayorCien = mayorCien + 1              
        
        
               
        if  digitos < 0:
            print ("Contador de numeros")
            print("a. Total de números ingresados: ", totalNumeros)
            print("b. Total de números pares ingresados: ", par)
            print("c. Total de numeros impares ingresados", impar)
            if par > 0:
                print(f"d. Promedio de números pares ingresados:  {sumaPares/par:.2f}")
            if impar > 0:
                print(f"e. Promedio de números impares ingresados:  {sumaImpares/impar:.2f}")
            print("f. Cantidad de numeros menores que 10: ", menorDiez)
            print("g. Cantidad de números que están entre 20 y 50: ", numVeinte)
            print("h. Cantidad de números que son mayores que 100: ", mayorCien)    
            break