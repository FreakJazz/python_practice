# Diccionario para almacenar tareas
tareas = []

# Función para agregar tareas
def agregar_tarea(nombre, prioridad):
    tarea = {"nombre": nombre, "prioridad": prioridad, "hecha": False}
    tareas.append(tarea)

# Función para mostrar todas las tareas
def mostrar_tareas():
    if not tareas:
        print("No hay tareas.")
        return
    
    for i, t in enumerate(tareas):
        estado = "✅" if t["hecha"] else "❌"
        print(f"{i+1}. {t['nombre']} (Prioridad: {t['prioridad']}) - {estado}")

# Función para marcar una tarea como hecha
def marcar_como_hecha(indice):
    try:
        tareas[indice]["hecha"] = True
    except IndexError:
        print("Índice fuera de rango")

# Programa principal
def menu():
    while True:
        print("\n1. Agregar tarea")
        print("2. Ver tareas")
        print("3. Marcar como hecha")
        print("4. Salir")

        try:
            opcion = int(input("Elige una opción: "))
        except ValueError:
            print("Ingresa un número válido.")
            continue

        if opcion == 1:
            nombre = input("Nombre de la tarea: ")
            prioridad = input("Prioridad (alta, media, baja): ")
            agregar_tarea(nombre, prioridad)
        elif opcion == 2:
            mostrar_tareas()
        elif opcion == 3:
            try:
                num = int(input("Número de la tarea a marcar: ")) - 1
                marcar_como_hecha(num)
            except ValueError:
                print("Número inválido.")
        elif opcion == 4:
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida.")

# Ejecutar el programa
if __name__ == "__main__":
    menu()
