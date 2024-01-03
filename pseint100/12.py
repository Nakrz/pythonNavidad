
print("NUMERO A : ")
A = int(input())
print("NUMERO B : ")
B = int(input())

if (A < B):
    for N in range (A+1, B-1 + 1):
        print(N)
else:
    for N in range (B+1, A-1 + 1):
        print (N)
            