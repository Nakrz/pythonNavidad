

print("VALOR DE N : ")
n = int(input())
suma = 1
d = 3
if (n > 1):
    print(suma, " + ")
    for i in range (2, n + 1):
        if (i == n):
            print (i, "/", d)
        else:
            print (i,"/",d," + ")
        suma = suma + (i/d)
        d = d + 2
        
print ("")
print ("La suma es : ", suma)

