# Ejercicio 2. Pilas (LIFO: el último que entra es el primero que sale)

def mostrar_menu():
    print("\n===== MENÚ PILA =====")
    print("1. Insertar en pila")
    print("2. Borrar en pila")
    print("3. Listar pila")
    print("4. Salir")


def insertar(pila):
    try:
        numero = int(input("Ingresa un número: "))
        pila.append(numero)          # se apila en la cima
        print(f"Se agregó {numero} a la pila.")
    except ValueError:
        print("Error: debes ingresar un número entero.")


def borrar(pila):
    if len(pila) == 0:
        print("La pila está vacía, no hay nada que quitar.")
    else:
        eliminado = pila.pop()       # se quita el de la cima (último elemento)
        print(f"Se quitó el elemento de la cima de la pila: {eliminado}")


def listar(pila):
    if len(pila) == 0:
        print("La pila está vacía.")
    else:
        print("Elementos de la pila (cima -> base):")
        for elemento in reversed(pila):
            print(f"  | {elemento} |")
        print("  -------")


def ejecutar_programa():
    pila = []
    opcion = 0
    while opcion != 4:
        mostrar_menu()
        try:
            opcion = int(input("Elige una opción: "))
        except ValueError:
            print("Opción inválida, escribe un número del 1 al 4.")
            opcion = 0
            continue

        if opcion == 1:
            insertar(pila)
        elif opcion == 2:
            borrar(pila)
        elif opcion == 3:
            listar(pila)
        elif opcion == 4:
            print("Saliendo del programa...")
        else:
            print("Opción inválida, escribe un número del 1 al 4.")


# Ciclo principal: pregunta si se desea ejecutar nuevamente el programa
repetir = "s"
while repetir.lower() == "s":
    ejecutar_programa()
    repetir = input("\n¿Deseas ejecutar nuevamente el programa? (s/n): ")
print("Programa finalizado.")