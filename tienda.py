import CodigoBuenasPracticas.producto as pr
from os import system

def main():
    inventario = []
    while True:
        system("cls")
        print("\nMenu de opciones:")
        print("1. Agregar producto")
        print("2. Quitar producto")
        print("3. Mostrar inventario")
        print("4. Salir")
        opcion = int(input("Ingrese una opción: "))
        match(opcion):
            case 1:
                nombre = input("Ingrese el nombre del producto: ")
                cantidad = int(input("Ingrese la cantidad inicial: "))
                precio = float(input("Ingrese el precio por unidad: "))
                inventario.append(pr.Producto(nombre, cantidad, precio))
                print("Producto agregado exitosamente.")
                input("Presione enter para continuar...")
            case 2:
                if len(inventario) == 0:
                    print("El inventario está vacío.")
                else:
                    nombre = input("Ingrese el nombre del producto a eliminar: ")
                    for i, producto in enumerate(inventario):
                        if producto.nombre_producto == nombre:
                            inventario.pop(i)
                            print(f"Producto {nombre} eliminado exitosamente.")
                            input("Presione enter para continuar...")
                            break
                        else:
                            print("Producto no encontrado.")
            case 3:
                for i in inventario:
                    print(f"Producto: {i.nombre_producto}")
                    print(f"Cantidad: {i.cantidad}")
                    print(f"Precio: ${i.precio:.2f}")
                    print("--------------------")
                input("Presione enter para continuar...")
            case 4:
                print("Gracias por utilizar el programa.")
                break

main()