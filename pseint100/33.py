a = 0
e = 0
i = 0
oo = 0
u = 0
vocal = ""

print("FRASE : ")
frase = input().upper()


for vocal in frase:
    if (vocal == "A" or vocal == "Á"):
        a = a + 1
    if (vocal == "E" or vocal == "É"):
        e = e + 1
    if (vocal == "I" or vocal == "Í"):
        i = i + 1
    if (vocal == "O" or vocal == "Ó"):
        oo = oo + 1
    if (vocal == "U" or vocal == "Ú"):
        u = u + 1    
        

print("A : ", a)
print("E : ", e)
print("I : ", i)
print("O : ", oo)
print("U : ", u)