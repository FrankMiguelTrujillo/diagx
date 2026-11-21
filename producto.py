import numpy as np


class Producto:
    """Producto que se vende (pizza, bebida) con su receta de insumos."""

    MAX_RECETA = 10  # máximo de insumos que puede tener una receta

    # 1. Constructor
    def __init__(self, id_producto, nombre, categoria, precio):
        self.__id_producto = id_producto
        self.__nombre = nombre
        self.__categoria = categoria            # "Pizza" o "Bebida"
        self.__precio = precio
        self.__estado = "Activo"

        # Receta: dos vectores paralelos + contador.
        # En la posición i: insumos_receta[i] es el objeto Insumo
        # y cantidades_receta[i] es cuánto lleva de ese insumo.
        self.__insumos_receta = np.full(Producto.MAX_RECETA, None, dtype=object)
        self.__cantidades_receta = np.zeros(Producto.MAX_RECETA)
        self.__cont_receta = 0                  # cuántos insumos hay de verdad

    # 2. Getters
    def get_id_producto(self):
        return self.__id_producto

    def get_nombre(self):
        return self.__nombre

    def get_categoria(self):
        return self.__categoria

    def get_precio(self):
        return self.__precio

    def get_estado(self):
        return self.__estado

    def get_insumos_receta(self):
        return self.__insumos_receta

    def get_cantidades_receta(self):
        return self.__cantidades_receta

    def get_cont_receta(self):
        return self.__cont_receta

    # 2. Setters
    def set_nombre(self, nombre):
        # El nombre no puede estar vacío ni tener números
        digitos = "0123456789"
        tiene_texto = False      # ¿hay al menos un carácter que no sea espacio?
        tiene_numero = False     # ¿hay algún dígito?

        for c in nombre:
            if c != " ":
                tiene_texto = True
            for d in digitos:
                if c == d:
                    tiene_numero = True

        if tiene_texto == False or tiene_numero == True:
            print("Nombre inválido: no puede estar vacío ni contener números.")
        else:
            self.__nombre = nombre

    def set_categoria(self, categoria):
        self.__categoria = categoria

    def set_precio(self, precio):
        if precio > 0:
            self.__precio = precio
        else:
            print("Precio inválido: debe ser mayor que 0.")

    # 3. Agrega un insumo a la receta en la siguiente posición libre
    def agregar_insumo_receta(self, insumo, cantidad):
        if self.__cont_receta >= Producto.MAX_RECETA:
            print("La receta está llena, no se puede agregar más insumos.")
        elif cantidad <= 0:
            print("Cantidad inválida: debe ser positiva.")
        else:
            self.__insumos_receta[self.__cont_receta] = insumo   # guarda el OBJETO
            self.__cantidades_receta[self.__cont_receta] = cantidad
            self.__cont_receta += 1

    # 4. Recorre solo hasta el contador (después hay None)
    def mostrar_receta(self):
        for i in range(self.__cont_receta):
            insumo = self.__insumos_receta[i]
            cantidad = self.__cantidades_receta[i]
            print(f"{insumo.get_nombre()}: {cantidad:g} {insumo.get_unidad()}")

    # 5. Da de baja el producto
    def inactivar(self):
        self.__estado = "Inactivo"


# Prueba
harina = Insumo(1, "Harina", "gramos", 5000, 1000)
queso = Insumo(2, "Queso mozzarella", "gramos", 3000, 500)
salsa = Insumo(3, "Salsa de tomate", "ml", 2000, 400)

pizza = Producto(1, "Pizza Margarita", "Pizza", 28000)
pizza.agregar_insumo_receta(harina, 250)
pizza.agregar_insumo_receta(queso, 150)
pizza.agregar_insumo_receta(salsa, 80)
pizza.agregar_insumo_receta(queso, -5)        # debe rechazarse

pizza.mostrar_receta()

pizza.set_precio(-1000)                        # debe rechazarse
print(pizza.get_precio())                      # 28000
