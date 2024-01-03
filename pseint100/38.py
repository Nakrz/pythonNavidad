

r = 0
v = 0
a = 0
print("CANTIDAD DE PERSONAS : ")
n = int(input())
for i in range(1, n + 1):
    print("PERSONA Nro.",i," ")
    c = ""
    while (c != "ROJO" and c != "VERDE" and c != "AZUL"):
        print("[ROJO - VERDE - AZUL]: ")
        c = input().upper()
        print("[ROJO - VERDE - AZUL]: ")
    if ( c == "ROJO"):
        r = r + 1
    elif (c == "VERDE"):
        v = v + 1
    else:
        a = a + 1
    print("")
    if (r > v and r > a):
        Mcolor = "ROJO"
    elif (v > r and v > a):
        Mcolor = "VERDE"
    else:
        Mcolor = "AZUL"
print("CANTIDAD DE COLOR ROJO  : ", r)
print("CANTIDAD DE COLOR VERDE : ", v)
print("CANTIDAD DE COLOR AZUL  : ", a)
print("EL COLOR MAS ESCOGIDO ES : ", Mcolor)