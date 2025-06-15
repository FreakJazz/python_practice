def input_validado(prompt, opciones):
    opciones = [o.lower() for o in opciones]
    while True:
        respuesta = input(prompt).strip().lower()
        if respuesta in opciones:
            return respuesta
        else:
            print(f"Por favor responde con {', '.join(opciones)}.")

def pedir_datos_personales():
    print("\nPor favor, ingresa tus datos para completar el pedido.")
    nombre = input("Nombre completo: ").strip()
    telefono = input("Telefono de contacto: ").strip()
    direccion = input("Direccion para entrega o contacto: ").strip()
    return {
        "nombre": nombre,
        "telefono": telefono,
        "direccion": direccion
    }

def chatbot():
    nombre_negocio = "Tu Negocio Aqui"

    servicios = {
        "1": {
            "nombre": "Servicio 1",
            "preguntas": [
                "Pregunta 1 para Servicio 1 (responde si o no): ",
                "Pregunta 2 para Servicio 1 (responde si o no): "
            ],
            "respuestas_validas": [
                ["si", "no"],
                ["si", "no"]
            ]
        },
        "2": {
            "nombre": "Servicio 2",
            "preguntas": [
                "Pregunta 1 para Servicio 2 (escribe cualquier respuesta): ",
                "Pregunta 2 para Servicio 2 (elige opcion a, b o c): "
            ],
            "respuestas_validas": [
                None,
                ["a", "b", "c"]
            ]
        },
        "3": {
            "nombre": "Servicio 3",
            "preguntas": [
                "Pregunta 1 para Servicio 3 (elige rojo, verde o azul): ",
                "Pregunta 2 para Servicio 3 (responde si o no): "
            ],
            "respuestas_validas": [
                ["rojo", "verde", "azul"],
                ["si", "no"]
            ]
        }
    }

    historial_pedidos = []

    print(f"Bienvenido a {nombre_negocio}.\nAqui puedes solicitar diferentes servicios.\n")

    while True:
        print("Servicios disponibles:")
        for clave, servicio in servicios.items():
            print(f"{clave}. {servicio['nombre']}")

        opcion = input("Elige el numero del servicio que deseas (o escribe 'salir' para terminar): ").strip().lower()
        if opcion == "salir":
            break

        if opcion not in servicios:
            print("Opcion invalida. Intenta de nuevo.\n")
            continue

        servicio = servicios[opcion]
        print(f"\nHas seleccionado: {servicio['nombre']}")

        respuestas = []
        for i, pregunta in enumerate(servicio['preguntas']):
            respuestas_validas = servicio['respuestas_validas'][i]
            if respuestas_validas:
                respuesta = input_validado(pregunta, respuestas_validas)
            else:
                while True:
                    respuesta = input(pregunta).strip()
                    if respuesta:
                        break
                    else:
                        print("Por favor ingresa una respuesta valida.")
            respuestas.append(respuesta)

        confirmar = input_validado("Confirmas tu pedido? (si/no): ", ["si", "no"])
        if confirmar == "si":
            pedido = {
                "clave_servicio": opcion,
                "servicio": servicio['nombre'],
                "respuestas": respuestas
            }
            historial_pedidos.append(pedido)
            print(f"¡Gracias! Tu pedido ha sido registrado.\n")
        else:
            print("Pedido cancelado. Puedes elegir otro servicio o salir.\n")

        continuar = input_validado("Deseas agregar otro pedido? (si/no): ", ["si", "no"])
        if continuar == "no":
            break

    if historial_pedidos:
        datos_cliente = pedir_datos_personales()

        print("\n--- Resumen final de tus pedidos ---")
        for idx, pedido in enumerate(historial_pedidos, start=1):
            print(f"\nPedido {idx}:")
            print(f"Servicio: {pedido['servicio']}")
            preguntas_del_servicio = servicios[pedido['clave_servicio']]['preguntas']
            for i, resp in enumerate(pedido['respuestas']):
                print(f" - {preguntas_del_servicio[i]} {resp}")

        print("\nDatos del cliente:")
        for key, value in datos_cliente.items():
            print(f"{key.capitalize()}: {value}")

        print(f"\nGracias por elegir {nombre_negocio}. Nos pondremos en contacto contigo pronto.")
    else:
        print("No registraste ningun pedido. ¡Gracias por visitarnos!")

if __name__ == "__main__":
    chatbot()
