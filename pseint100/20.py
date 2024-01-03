import random



sw = 0
numA = random.randrange(1,20)

for i in range (1, 4):
    print("ENCUENTRE EL NUMERO [1 - 20] : ")
    num=int(input())
    if (num == numA):
        print("NUMERO ENCONTRADO")
        sw = 1
        i = 3
    else:
        if (num > numA):
            print("INGRESE UN NUMERO MENOR")
        else:
            print("INGRESE UN NUMERO MAYOR")
    
    print ("")

if (sw == 0):
    print("EL NUMERO A ENCONTRAR ERA : ",numA)
    
    