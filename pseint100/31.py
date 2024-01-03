C = 0
S = 0
D = 0
L = 0
R = 0
M = 0

consonante = 0
refran = ""

print("Ingrese Refran : ")
ref = input()

for F in range(len(ref)):
    if ref[F] != " ":
        refran += ref[F]
        
for letra in refran.upper():
    if letra == "C":
        C = + 1
    elif letra == "S":
        S = + 1
    elif letra == "D":
        D = + 1
    elif letra == "L":
        L = + 1
    elif letra == "R":
        R = + 1
    elif letra == "M":
        M = + 1
    if letra not in "AEIOU":
        consonante += 1


print("CANTIDAD DE C :", C)
print("CANTIDAD DE S :", S)
print("CANTIDAD DE D :", D)
print("CANTIDAD DE L :", L)
print("CANTIDAD DE R :", R)
print("CANTIDAD DE M :", M)
print("CANTIDAD DE CONSONANTES:", consonante)


