


while True:
    print("Altura del rombo: ")
    altura = int(input())
    if altura % 2 == 1:  
        break
    
for i in range(1, altura + 1, 2):
 
    for j in range(1, (altura - i) // 2 + 1):
        print(" ", end="")
    

    for j in range(1, i + 1):
        print("*", end="")
    
    print("") 

for i in range(altura - 2, 0, -2):

    for j in range(1, (altura - i) // 2 + 1):
        print(" ", end="")   
    for j in range(1, i + 1):
        print("*", end="")
    
    print("") 


