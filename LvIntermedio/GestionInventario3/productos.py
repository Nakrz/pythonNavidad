productos = []


def registroProductos ():
    global productos
    codigo = int(input("Ingrese el codigo del producto: "))
    nombre = input("Ingrese el nombre del producto: ")
    valorCompra = float(input("Ingrese el valor de compra del producto: "))
    valorVenta = float(input("Ingrese el valor de venta del producto: "))
    stockMinimo = int(input("Ingrese el numero de stock minimo del producto: "))
    stockMaximo = int(input("Ingrese el numero de stock maximo del producto: "))
    proveedorP = input("Ingrese el nombre del proveedor del producto: ")
    
    productos2 = {
        "codigo": codigo,
        "nombre": nombre,
        "valorCompra": valorCompra,
        "valorVenta": valorVenta,
        "stockMinimo": stockMinimo,
        "stockMaximo": stockMaximo,
        "stockActual": 0,
        "proveedorP": proveedorP
    }    
   
    productos.append(productos2)
    print("Producto registrado con Exito")
   

def visorProductos():
    global productos
    if not productos:
        print("")
        print("No hay productos registrados")
    else:
        print("")
        print("Lista de Productos Registrados: ")
        print("")
        for producto in productos:
            print("________________________")
            print("Codigo:", producto["codigo"])
            print("Nombre:", producto["nombre"])
            print("Valor de compra:", producto["valorCompra"])
            print("Valor de venta:", producto["valorVenta"])
            print("Stock minimo:", producto["stockMinimo"])
            print("Stock maximo:", producto["stockMaximo"])
            print("Stock actual disponible:", producto["stockActual"])
            print("Proveedor:", producto["proveedorP"])
            print("________________________")



def actualizarStock():
    global productos
    print("")
    codigo = input("Ingrese el codigo del producto para actualizar el stock: ")
    for producto in productos:
        if str(producto["codigo"]) == codigo:
            stockNuevo = int(input(f"Ingrese el nuevo stock para {producto['nombre']}: "))
            producto["stockActual"] = stockNuevo
            print(f"Stock actualizado para {producto['nombre']} ({producto['codigo']}) a {stockNuevo}.")
            return
    print("El producto ingresado no fue hallado")
    

    
def informeProductosCriticos():
    productosCriticos = [producto for producto in productos if producto["stockActual"] < producto["stockMinimo"]]
    if productosCriticos:
        print("")
        print("Productos con stock por debajo del limite minimo:")
        for producto in productosCriticos:
            print("Codigo:", producto["codigo"])
            print("Nombre:", producto["nombre"])
            print("Stock actual:", producto["stockActual"])
            print("Stock minimo:", producto["stockMinimo"])
            print("Stock maximo:", producto["stockMaximo"])
            print("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°")
    else:
        print("")
        print("No hay productos por debajo del limite minimo.")



def calcularGananciaPotencial():
    gananciaTol = 0
    for producto in productos:
        valorDiferencia = producto["valorVenta"] - producto["valorCompra"]
        gananciaPro = valorDiferencia * producto["stockActual"]
        gananciaTol = gananciaTol + gananciaPro
    
    print("")
    print(f"Ganancia potencial total: {gananciaTol} .$")