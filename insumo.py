class Insumo:
    """Representa un insumo del inventario (harina, huevos, etc.)."""

    # 1. Constructor: guarda los datos iniciales del insumo
    def __init__(self, id_insumo, nombre, unidad, cantidad_disponible, stock_minimo):
        self.__id_insumo = id_insumo
        self.__nombre = nombre
        self.__unidad = unidad                      # ej: "gramos", "unidades"
        self.__cantidad_disponible = cantidad_disponible
        self.__stock_minimo = stock_minimo
        self.__estado = "Activo"                    # siempre empieza activo

    # 2. Getters (para leer los atributos privados desde afuera)
    def get_id_insumo(self):
        return self.__id_insumo

    def get_nombre(self):
        return self.__nombre

    def get_unidad(self):
        return self.__unidad

    def get_cantidad_disponible(self):
        return self.__cantidad_disponible

    def get_stock_minimo(self):
        return self.__stock_minimo

    def get_estado(self):
        return self.__estado

    # 2. Setters (solo nombre y stock mínimo se pueden cambiar)
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_stock_minimo(self, stock_minimo):
        self.__stock_minimo = stock_minimo

    # 3. Suma existencia solo si la cantidad es positiva
    def agregar_existencia(self, cantidad):
        if cantidad > 0:
            self.__cantidad_disponible += cantidad

    # 4. Resta solo si hay suficiente; avisa con True/False si se pudo
    def descontar_existencia(self, cantidad):
        if cantidad <= self.__cantidad_disponible:
            self.__cantidad_disponible -= cantidad
            return True
        return False

    # 5. True si ya llegó (o bajó) al stock mínimo
    def necesita_reposicion(self):
        return self.__cantidad_disponible <= self.__stock_minimo

    # 6. Da de baja el insumo
    def inactivar(self):
        self.__estado = "Inactivo"


# Prueba rápida
harina = Insumo(1, "Harina", "gramos", 1000, 200)
harina.agregar_existencia(500)            # 1500
print(harina.descontar_existencia(1400))  # True  -> quedan 100
print(harina.descontar_existencia(500))   # False -> siguen 100
print(harina.necesita_reposicion())       # True  (100 <= 200)
harina.inactivar()
print(harina.get_estado())                # Inactivo
