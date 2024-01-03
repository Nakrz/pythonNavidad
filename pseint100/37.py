


M = [[0] * 20 for _ in range(20)]

print("MOSTRAR EL TRIANGULO DE PASCAL")
print("INGRESE DIMENSION [MENOS O IGUAL A 20]")
N = int(input())

for IZQ in range(1, N):
    for DER in range(1, N):
        M[IZQ][DER] = 0

for IZQ in range(1, N):
    M[IZQ][1] = 1

for DER in range(1, N):
    M[DER][DER] = 1

for IZQ in range(2, N):
    for DER in range(2, N):
        M[IZQ][DER] = M[IZQ - 1][DER] + M[IZQ - 1][DER - 1]

for IZQ in range(1, N + 1):
    ESPACIOS = ""
    for E in range(1, N - IZQ + 1):
        ESPACIOS += " "
    print(ESPACIOS, end="")
    for DER in range(1, IZQ + 1):
        VAL = M[IZQ - 1][DER - 1]
        if VAL != 0:
            print(VAL, end=" ")
    print()