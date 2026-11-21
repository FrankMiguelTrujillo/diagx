class Persona:
    """Clase padre: datos comunes de clientes y usuarios."""

    # Constructor: inicializa vacío y asigna con los setters (así valida)
    def __init__(self, id_persona, nombre, telefono):
        self.__id = id_persona
        self.__nombre = ""
        self.__telefono = ""
        self.set_nombre(nombre)
        self.set_telefono(telefono)
        self.__estado = "Activo"

    # Getters
    def get_id(self):
        return self.__id

    def get_nombre(self):
        return self.__nombre

    def get_telefono(self):
        return self.__telefono

    def get_estado(self):
        return self.__estado

    # Setters
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

    def set_telefono(self, telefono):
        # Solo dígitos y exactamente 10 caracteres
        digitos = "0123456789"
        cantidad = 0             # cuántos caracteres tiene (contados a mano)
        todo_digitos = True      # se vuelve False si aparece algo que no sea dígito

        for c in telefono:
            cantidad += 1
            es_digito = False
            for d in digitos:
                if c == d:
                    es_digito = True
            if es_digito == False:
                todo_digitos = False

        if todo_digitos == False or cantidad != 10:
            print("Teléfono inválido: debe tener exactamente 10 dígitos.")
        else:
            self.__telefono = telefono

    def inactivar(self):
        self.__estado = "Inactivo"


class Cliente(Persona):
    """Cliente de la pizzería: es una Persona con dirección."""

    def __init__(self, id_persona, nombre, telefono, direccion):
        super().__init__(id_persona, nombre, telefono)   # crea lo heredado
        self.__direccion = ""
        self.set_direccion(direccion)

    def get_direccion(self):
        return self.__direccion

    def set_direccion(self, direccion):
        # No puede estar vacía ni ser solo espacios
        tiene_texto = False
        for c in direccion:
            if c != " ":
                tiene_texto = True

        if tiene_texto == False:
            print("Dirección inválida: no puede estar vacía.")
        else:
            self.__direccion = direccion


class Usuario(Persona):
    """Usuario del sistema: es una Persona con un rol."""

    def __init__(self, id_persona, nombre, telefono, rol):
        super().__init__(id_persona, nombre, telefono)   # crea lo heredado
        self.__rol = ""
        self.set_rol(rol)

    def get_rol(self):
        return self.__rol

    def set_rol(self, rol):
        if rol == "Cajero" or rol == "Mesero" or rol == "Administrador":
            self.__rol = rol
        else:
            print("Rol inválido: debe ser 'Cajero', 'Mesero' o 'Administrador'.")


# Prueba
c = Cliente(1, "Laura Gómez", "3001234567", "Calle 10 # 5-20")
print(c.get_nombre(), c.get_telefono(), c.get_direccion())   # métodos heredados + propio

c.set_telefono("300-123")        # debe rechazarse
c.set_telefono("30012345")       # debe rechazarse (8 dígitos)
print(c.get_telefono())          # 3001234567 (no cambió)

u = Usuario(1, "Carlos Ruiz", "3109876543", "Cajero")
u.set_rol("Gerente")             # debe rechazarse
print(u.get_rol())               # Cajero

c.inactivar()
print(c.get_estado())            # Inactivo  (método heredado de Persona)
