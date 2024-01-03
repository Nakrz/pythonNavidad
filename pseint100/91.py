print("COSTO  : $ DE DESTINO")
print("[1] Estados Unidos - $0.13")
print("[2] Canadá - $0.11")
print("[5] América del Sur - $0.52")
print("[6] América Central - $0.99")
print("[8] México - $0.17")
print("[9] Europa - $0.17")
print("[10] Asía - $0.20")
print("[15] África - $0.59")
print("[20] Oceanía - $0.28")
print("INGRESE CLAVE DESTINO: ")
clave = int(input())
print("DURACIÓN DE LA LLAMADA :")
minutos = int(input())


if clave == 1:
    print ("COSTO  : $",minutos *0.13)
elif clave == 2:
    print ("COSTO  : $",minutos *0.11)
elif clave == 5:
    print ("COSTO  : $",minutos *0.52)
elif clave == 6:
    print ("COSTO  : $ ",minutos *0.99)
elif clave == 8:
    print ("COSTO  : $ ",minutos *0.17)
elif clave == 9:
    print ("COSTO  : $ ",minutos *0.17)
elif clave == 10:
    print ("COSTO  : $ ",minutos *0.20)
elif clave == 15:
    print ("COSTO  : $ ",minutos *0.59)
elif clave == 20:
    print ("COSTO  : $ ",minutos *0.28)
else:
    print(" !! Error en clave !! ")