import time
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

def agregar_producto(inventario: list, nombres: list) -> None:
    try:
        nombre = input("Ingrese el nombre del producto: ")
        if nombre in nombres:
            print("El producto ya existe en el inventario.")
            return
        cantidad = int(input("Ingrese la cantidad inicial: "))
        precio = float(input("Ingrese el precio por unidad: "))
        inventario.append(pr(nombre, precio, cantidad))
        nombres.append(nombre)
        print("Producto agregado exitosamente.")
    except ValueError:
        print("Error: Por favor, ingrese un valor numérico válido para cantidad y precio.")
    except Exception as e:
        print(f"Error inesperado: {e}")

def quitar_producto(inventario: list, nombres: list) -> None:
    if len(inventario) == 0:
        print("El inventario está vacío.")
    else:
        try:
            nombre = input("Ingrese el nombre del producto a eliminar: ").lower()
            for i, producto in enumerate(inventario):
                if producto.nombre_producto.lower() == nombre:
                    inventario.pop(i)
                    nombres.remove(nombre)
                    print(f"Producto {nombre} eliminado exitosamente.")
                    return
            print("Producto no encontrado.")
        except ValueError:
            print("Error: El producto no se pudo eliminar.")
        except Exception as e:
            print(f"Error inesperado: {e}")

def ver_inventario(inventario: list) -> None:
    try:
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
    except Exception as e:
        print(f"Error al mostrar el inventario: {e}")

def agregar_stock(inventario: list) -> None:
    try:
        nombre = input("Ingrese el nombre del producto: ").lower()
        cantidad = int(input("Ingrese la cantidad a agregar: "))
        for producto in inventario:
            if producto.nombre_producto.lower() == nombre:
                producto.agregar_stock(cantidad)
                print("Stock agregado exitosamente.")
                return
        print("Producto no encontrado.")
    except ValueError:
        print("Error: Por favor, ingrese un valor numérico válido para la cantidad.")
    except Exception as e:
        print(f"Error inesperado: {e}")

def quitar_stock(inventario: list) -> None:
    try:
        nombre = input("Ingrese el nombre del producto: ").lower()
        cantidad = int(input("Ingrese la cantidad a quitar: "))
        for producto in inventario:
            if producto.nombre_producto.lower() == nombre:
                producto.quitar_stock(cantidad)
                print("Stock reducido exitosamente.")
                return
        print("Producto no encontrado.")
    except ValueError:
        print("Error: Por favor, ingrese un valor numérico válido para la cantidad.")
    except Exception as e:
        print(f"Error inesperado: {e}")

def actualizar_precio(inventario: list) -> None:
    try:
        nombre = input("Ingrese el nombre del producto: ").lower()
        nuevo_precio = float(input("Ingrese el nuevo precio: "))
        for producto in inventario:
            if producto.nombre_producto.lower() == nombre:
                producto.actualizar_precio(nuevo_precio)
                print("Precio actualizado exitosamente.")
                return
        print("Producto no encontrado.")
    except ValueError:
        print("Error: Por favor, ingrese un valor numérico válido para el precio.")
    except Exception as e:
        print(f"Error inesperado: {e}")

def mostrar_stock_producto(inventario: list) -> None:
    try:
        nombre = input("Ingrese el nombre del producto: ").lower()
        for producto in inventario:
            if producto.nombre_producto.lower() == nombre:
                producto.ver_stock()
                return
        print("Producto no encontrado.")
    except Exception as e:
        print(f"Error al mostrar el stock del producto: {e}")

def controlInventario() -> None:
    inventario = []
    nombres = []
    while True:
        system("cls")
        mostrar_menu()
        try:
            opcion = int(input("Ingrese una opción: "))
        except ValueError:
            print("Opción inválida. Intente de nuevo. Espere")
            time.sleep(1.5)
            continue

        try:
            match(opcion):
                case 1:
                    agregar_producto(inventario, nombres)
                    input("Presione enter para continuar...")
                    time.sleep(0.5)
                case 2:
                    quitar_producto(inventario, nombres)
                    input("Presione enter para continuar...")
                    time.sleep(0.5)
                case 3:
                    ver_inventario(inventario)
                    input("Presione enter para continuar...")
                    time.sleep(0.5)
                case 4:
                    agregar_stock(inventario)
                    input("Presione enter para continuar...")
                    time.sleep(0.5)
                case 5:
                    quitar_stock(inventario)
                    input("Presione enter para continuar...")
                    time.sleep(0.5)
                case 6:
                    actualizar_precio(inventario)
                    input("Presione enter para continuar...")
                    time.sleep(0.5)
                case 7:
                    mostrar_stock_producto(inventario)
                    input("Presione enter para continuar...")
                    time.sleep(0.5)
                case 8:
                    print("Gracias por utilizar el programa.")
                    break
                case _:
                    print("Opción no encontrada en el menú. Intente de nuevo.")
                    time.sleep(1)
        except Exception as e:
            print(f"Error inesperado: {e}")
            time.sleep(1.5)

if __name__ == "__main__":
    controlInventario()
