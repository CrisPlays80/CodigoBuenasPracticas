from producto import Producto as pr
from os import system

def mostrar_menu() -> None:
    print("\nMenu de opciones:")
    print("1. Agregar producto")
    print("2. Quitar producto")
    print("3. Mostrar inventario")
    print("4. Agregar stock")
    print("5. Quitar stock")
    print("6. Actualizar el precio de producto")
    print("7. Mostrar stock de un producto")
    print("8. Salir")

def agregar_producto(inventario: list) -> None:
    nombre = input("Ingrese el nombre del producto: ")
    cantidad = int(input("Ingrese la cantidad inicial: "))
    precio = float(input("Ingrese el precio por unidad: "))
    inventario.append(pr(nombre, precio, cantidad))
    print("Producto agregado exitosamente.")

def quitar_producto(inventario: list) -> None:
    if len(inventario) == 0:
        print("El inventario está vacío.")
    else:
        nombre = input("Ingrese el nombre del producto a eliminar: ")
        for i, producto in enumerate(inventario):
            if producto.nombre_producto == nombre:
                inventario.pop(i)
                print(f"Producto {nombre} eliminado exitosamente.")
                return
        print("Producto no encontrado.")

def ver_inventario(inventario: list) -> None:
    suma = 0
    if len(inventario) == 0:
        print("El inventario está vacío.")
    else:
        for i in inventario:
            print(f"Producto: {i.nombre_producto}")
            print(f"Cantidad: {i.cantidad}")
            print(f"Precio: ${i.precio:.2f}")
            print("--------------------")
            suma += i.precio * i.cantidad
        print(f"Total en inventario: ${suma:.2f}")


def agregar_stock(inventario: list) -> None:
    nombre = input("Ingrese el nombre del producto: ")
    cantidad = int(input("Ingrese la cantidad a agregar: "))
    for producto in inventario:
        if producto.nombre_producto == nombre:
            producto.agregar_stock(cantidad)
            print(f"Stock agregado exitosamente al producto {nombre}.")
            return
    print("Producto no encontrado.")

def quitar_stock(inventario: list) -> None:
    nombre = input("Ingrese el nombre del producto: ")
    cantidad = int(input("Ingrese la cantidad a quitar: "))
    for producto in inventario:
        if producto.nombre_producto == nombre:
            producto.quitar_stock(cantidad)
            print(f"Stock quitado exitosamente del producto {nombre}.")
            return
    print("Producto no encontrado.")

def actualizar_precio(inventario: list) -> None:
    nombre = input("Ingrese el nombre del producto: ")
    nuevo_precio = float(input("Ingrese el nuevo precio: "))
    for producto in inventario:
        if producto.nombre_producto == nombre:
            producto.actualizar_precio(nuevo_precio)
            print(f"Precio actualizado exitosamente del producto {nombre}.")
            return
    print("Producto no encontrado.")

def mostrar_stock_producto(inventario: list) -> None:
    nombre = input("Ingrese el nombre del producto: ")
    for producto in inventario:
        if producto.nombre_producto == nombre:
            producto.ver_stock()
            return
    print("Producto no encontrado.")

def controlInventario() -> None:
    inventario = []
    while True:
        system("cls")
        mostrar_menu()
        opcion = int(input("Ingrese una opción: "))
        match(opcion):
            case 1:
                agregar_producto(inventario)
                input("Presione enter para continuar...")
            case 2:
                quitar_producto(inventario)
                input("Presione enter para continuar...")
            case 3:
                ver_inventario(inventario)
                input("Presione enter para continuar...")
            case 4:
                agregar_stock(inventario)
                input("Presione enter para continuar...")
            case 5:
                quitar_stock(inventario)
                input("Presione enter para continuar...")
            case 6:
                actualizar_precio(inventario)
                input("Presione enter para continuar...")
            case 7:
                mostrar_stock_producto(inventario)
                input("Presione enter para continuar...")
            case 8:
                print("Gracias por utilizar el programa.")
                break
            case _:
                print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    controlInventario()