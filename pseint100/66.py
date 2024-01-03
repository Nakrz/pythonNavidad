

print("Altura del Triangulo : ")
alt = int(input())
print("Ingrese un Caracter : ")
caract = input()

for i in range (1, alt + 1):
    
    for j in range (1, (alt-i)):
        print(" ", end=" ")
    
    
    for j in range (1, ((i*2)-1)):
        print (caract, end=" ")
        
    print ("")
        