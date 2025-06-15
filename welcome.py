# 1. Importación de módulos
import math

# 2. Definición de funciones
def bienvenida():
    print("👋 ¡Hola! Bienvenidos a la clase magistral de Python en CONQUITO.")

def saludar(nombre: str):
    print(f"Hola, {nombre} 👋")

# 3. Definición de clase
class Persona:
    def __init__(self, nombre: str):
        self.nombre = nombre

    def presentarse(self):
        print(f"Mi nombre es {self.nombre}.")

# 4. Código principal
if __name__ == "__main__":
    bienvenida()
    saludar("Jazmin")

    persona = Persona("Juan")
    persona.presentarse()
