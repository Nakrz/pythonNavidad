print("NUMERO 1 : ")
num1=int(input())
print("NUMERO 2 : ")
num2=int(input())
print("OPERADOR :")
print("[1 +][2 -][3 x][4 /] : ")
operador=int(input())

if operador == 1:
    print("SUMA:",num1+num2)
elif operador == 2:
    print("RESTA: ",num1-num2)
elif operador == 3:
    print("MULTIPLICACION:",num1*num2)
elif operador == 4:
    print("DIVISION : ",num1/num2)
else:
    print("OPERADOR INCORRECTO")