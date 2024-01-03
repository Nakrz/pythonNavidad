import productos
import os

while True:
    print("")
    print("GESTION DE INVENTARIO")
    print("")
    print("1. Registrar Producto")
    print("2. Mostrar Productos")
    print("3. Actualizar Stock")
    print("4. Informe de Productos Criticos")
    print("5. Calculo de Ganancia Potencial")
    print("6. Salir")

    opcion = input("Seleccione una opcion: ")

    if opcion == "1":
        productos.registroProductos()
        os.system("pause")
        os.system("cls")
    elif opcion == "2":
        productos.visorProductos()
        os.system("pause")
        os.system("cls")
    elif opcion == "3":
        productos.actualizarStock()
        os.system("pause")
        os.system("cls")
    elif opcion == "4":
        productos.informeProductosCriticos()
        os.system("pause")
        os.system("cls")
    elif opcion == "5":
        productos.calcularGananciaPotencial()
        os.system("pause")
        os.system("cls")
    elif opcion == "6":
        break
    else:
        print("Opcion no valida, por favor seleccione una opcion valida [1,2,3,4,5,6].")


