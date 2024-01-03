


print("CANTIDAD DE SEGUNDOS : ")
xseg = int(input())

hor = int(xseg/3600)
min = int((xseg - (hor * 3600))/60)
seg = int(xseg - ((hor*3600)+ (min * 60)))

print("HORAS    :",hor)
print("MINUTOS    :",min)
print("SEGUNDOS    :",seg)