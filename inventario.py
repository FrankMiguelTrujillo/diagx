import numpy as np


class Inventario:
    """Guarda todos los insumos y controla las existencias."""

    MAX_INSUMOS = 50  # máximo de insumos que puede tener el inventario

    # Constructor: vector vacío de objetos + contador
    def __init__(self):
        self.__insumos = np.full(Inventario.MAX_INSUMOS, None, dtype=object)
        self.__cont_insumos = 0

    # 1. Agrega un insumo si hay espacio y su id no está repetido
    def agregar_insumo(self, insumo):
        if self.__cont_insumos >= Inventario.MAX_INSUMOS:
            print("El inventario está lleno, no se puede agregar el insumo.")
        elif self.buscar_insumo(insumo.get_id_insumo()) != None:
            print(f"Ya existe un insumo con id {insumo.get_id_insumo()}, no se agregó.")
        else:
            self.__insumos[self.__cont_insumos] = insumo
            self.__cont_insumos += 1

    # 2. Búsqueda lineal hasta el contador: devuelve el objeto o None
    def buscar_insumo(self, id_insumo):
        for i in range(self.__cont_insumos):
            if self.__insumos[i].get_id_insumo() == id_insumo:
                return self.__insumos[i]
        return None

    # 3. Tabla con todos los insumos
    def mostrar_insumos(self):
        print(f"{'ID':<4}{'Nombre':<20}{'Cantidad':>10}  {'Unidad':<8}{'Mínimo':>8}  {'Estado':<10}")
        for i in range(self.__cont_insumos):
            ins = self.__insumos[i]
            print(f"{ins.get_id_insumo():<4}{ins.get_nombre():<20}"
                  f"{ins.get_cantidad_disponible():>10g}  {ins.get_unidad():<8}"
                  f"{ins.get_stock_minimo():>8g}  {ins.get_estado():<10}")

    # 4. Solo los activos que necesitan reposición
    def mostrar_alertas_stock(self):
        hay_alertas = False
        for i in range(self.__cont_insumos):
            ins = self.__insumos[i]
            if ins.get_estado() == "Activo" and ins.necesita_reposicion() == True:
                print(f"ALERTA: {ins.get_nombre()} tiene {ins.get_cantidad_disponible():g} "
                      f"{ins.get_unidad()} (mínimo {ins.get_stock_minimo():g})")
                hay_alertas = True
        if hay_alertas == False:
            print("No hay insumos que necesiten reposición.")

    # 5. ¿Alcanzan los insumos para preparar 'cantidad' unidades del producto?
    #    Usa bandera para mostrar TODOS los que faltan, no solo el primero.
    def verificar_disponibilidad(self, producto, cantidad):
        insumos = producto.get_insumos_receta()
        cantidades = producto.get_cantidades_receta()
        disponible = True

        for i in range(producto.get_cont_receta()):
            necesario = cantidades[i] * cantidad
            if insumos[i].get_cantidad_disponible() < necesario:
                print(f"No alcanza {insumos[i].get_nombre()}: se necesitan {necesario:g} "
                      f"{insumos[i].get_unidad()} y hay {insumos[i].get_cantidad_disponible():g}")
                disponible = False

        return disponible

    # 6. Descuenta de cada insumo lo que lleva la receta por la cantidad pedida
    def descontar_producto(self, producto, cantidad):
        # Primero se verifica, para no descontar a medias
        if self.verificar_disponibilidad(producto, cantidad) == False:
            print("No se descontó nada.")
            return False

        insumos = producto.get_insumos_receta()
        cantidades = producto.get_cantidades_receta()
        for i in range(producto.get_cont_receta()):
            necesario = cantidades[i] * cantidad
            insumos[i].descontar_existencia(necesario)
        return True


# Prueba (usa harina, queso, salsa y pizza de la celda de Producto)
inv = Inventario()
inv.agregar_insumo(harina)
inv.agregar_insumo(queso)
inv.agregar_insumo(salsa)
inv.agregar_insumo(harina)                        # debe rechazarse (id repetido)

print(inv.verificar_disponibilidad(pizza, 2))     # True
inv.descontar_producto(pizza, 2)
inv.mostrar_insumos()                             # harina 4500, queso 2700, salsa 1840

print(inv.verificar_disponibilidad(pizza, 30))    # False
inv.mostrar_alertas_stock()                       # ninguno todavía
