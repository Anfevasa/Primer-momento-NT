productos = []
ventas = []

def registrar_producto():
    id = input("Ingrese ID del producto: ")
    nombre = input("Ingrese nombre del producto: ")
    precio = float(input("Ingrese precio del producto: "))
    cantidad = int(input("Ingrese cantidad del producto: "))
    producto = {"id": id, "nombre": nombre, "precio": precio, "cantidad": cantidad}
    productos.append(producto)
    print("Producto registrado con éxito.")

def hacer_venta():
    id = input("Ingrese ID del producto a vender: ")
    cantidad_vender = int(input("Ingrese cantidad a vender: "))
    for producto in productos:
        if producto["id"] == id:
            if producto["cantidad"] >= cantidad_vender:
                producto["cantidad"] -= cantidad_vender
                venta = {"id": id, "cantidad": cantidad_vender}
                ventas.append(venta)
                print("Venta realizada con éxito.")
            else:
                print("No hay suficiente cantidad en stock.")
            break
    else:
        print("Producto no encontrado.")

def mostrar_total_ventas():
    total = 0
    for venta in ventas:
        for producto in productos:
            if producto["id"] == venta["id"]:
                total += producto["precio"] * venta["cantidad"]
    print(f"Total de ventas: ${total:.2f}")

def mostrar_stock():
    if productos:
        print("Stock de productos:")
        for producto in productos:
            print(f"ID: {producto['id']}, Nombre: {producto['nombre']}, Precio: ${producto['precio']:.2f}, Cantidad: {producto['cantidad']}")
    else:
        print("No hay productos registrados.")

def menu():
    while True:
        print("1. Registrar producto")
        print("2. Hacer venta")
        print("3. Mostrar total de ventas")
        print("4. Mostrar stock")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            registrar_producto()
        elif opcion == "2":
            hacer_venta()
        elif opcion == "3":
            mostrar_total_ventas()
        elif opcion == "4":
            mostrar_stock()
        elif opcion == "5":
            print("Saliendo...")
            break
        else:
            print("Opción no válida.")

menu()
