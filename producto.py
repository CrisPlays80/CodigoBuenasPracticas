class Producto:
    def __init__(self, nombre_producto, precio, cantidad):
        self.nombre_producto = nombre_producto.lower()
        self.precio = precio
        self.cantidad = cantidad

    def agregar_stock(self, cantidad):
        self.cantidad += cantidad
        print(f"Se agregaron {cantidad} unidades de {self.nombre_producto} al stock.")

    def quitar_stock(self, cantidad):
        if not self.cantidad:
            self.cantidad -= cantidad
            print(f"Se quitaron {cantidad} unidades de {self.nombre_producto} del stock.")
        else:
            print(f"No hay suficiente stock de {self.nombre_producto} para quitarlo.")
    
    def actualizar_precio(self, nuevo_precio):
        self.precio = nuevo_precio
        print(f"El precio de {self.nombre_producto} se actualizó a {self.precio}.")
    
    def ver_stock(self):
        print(f"El stock de {self.nombre_producto} es {self.cantidad} y el precio por unidad es de {self.precio}.")
    