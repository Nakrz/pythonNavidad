fact = 1
print("FACTORIAL A CALCULAR : ")
num = int(input())
print("")
print("SERIE DEL FACTORIAL : ")
for x in range (1, num + 1):
    print(num + 1 - x, " ")
    fact = fact * x
    
print ("")
print("EL FACTORIAL ES : ", fact )
print ("")
