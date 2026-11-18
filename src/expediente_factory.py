from abc import ABC, abstractmethod

# 1. Interfaz común para todos los expedientes
class Expediente(ABC):
    @abstractmethod
    def mostrar_detalles(self):
        pass

# 2. Clases Concretas según la especie
class PerroExpediente(Expediente):
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.tipo = "Perro"
        self.vacunas = []

    def mostrar_detalles(self):
        return f"[EXPEDIENTE CANINO] Nombre: {self.nombre}, Edad: {self.edad} años. Requiere control de vacunas y chip."

class GatoExpediente(Expediente):
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.tipo = "Gato"
        self.prueba_fiv_felv = False

    def mostrar_detalles(self):
        return f"[EXPEDIENTE FELINO] Nombre: {self.nombre}, Edad: {self.edad} años. Requiere prueba FIV/FeLV y desparasitación."

class FaunaSilvestreExpediente(Expediente):
    def __init__(self, especie_silvestre, zona_rescate):
        self.especie_silvestre = especie_silvestre
        self.zona_rescate = zona_rescate
        self.tipo = "Fauna Silvestre"

    def mostrar_detalles(self):
        return f"[EXPEDIENTE SILVESTRE] Especie: {self.especie_silvestre}, Zona: {self.zona_rescate}. Requiere evaluación de rehabilitación y posible liberación."

# 3. Fábrica Abstracta (Creator)
class ExpedienteFactory(ABC):
    @abstractmethod
    def crear_expediente(self, *args, **kwargs) -> Expediente:
        pass

# 4. Fábricas Concretas
class PerroFactory(ExpedienteFactory):
    def crear_expediente(self, nombre, edad):
        return PerroExpediente(nombre, edad)

class GatoFactory(ExpedienteFactory):
    def crear_expediente(self, nombre, edad):
        return GatoExpediente(nombre, edad)

class FaunaSilvestreFactory(ExpedienteFactory):
    def crear_expediente(self, especie_silvestre, zona_rescate):
        return FaunaSilvestreExpediente(especie_silvestre, zona_rescate)


if __name__ == "__main__":
    # Creación mediante fábricas específicas sin acoplar el código cliente
    fabrica_perros = PerroFactory()
    expediente_perro = fabrica_perros.crear_expediente("Firulais", 2)

    fabrica_gatos = GatoFactory()
    expediente_gato = fabrica_gatos.crear_expediente("Michi", 1)

    fabrica_silvestre = FaunaSilvestreFactory()
    expediente_ave = fabrica_silvestre.crear_expediente("Lechuza común", "Parque Metropolitano")

    # Mostrar resultados
    print(expediente_perro.mostrar_detalles())
    print(expediente_gato.mostrar_detalles())
    print(expediente_ave.mostrar_detalles())
