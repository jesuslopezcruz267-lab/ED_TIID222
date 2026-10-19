# Ejercicio 1. Colas (FIFO: el primero que entra es el primero que sale)

def mostrar_menu():
    print("\n===== MENÚ COLA =====")
    print("1. Insertar cola")
    print("2. Borrar en cola")
    print("3. Listar cola")
    print("4. Salir")


def insertar(cola):
    try:
        numero = int(input("Ingresa un número: "))
        cola.append(numero)          # entra por el final
        print(f"Se insertó {numero} en la cola.")
    except ValueError:
        print("Error: debes ingresar un número entero.")


def borrar(cola):
    if len(cola) == 0:
        print("La cola está vacía, no hay nada que borrar.")
    else:
        eliminado = cola.pop(0)      # sale por el frente (primer elemento)
        print(f"Se eliminó el primer elemento de la cola: {eliminado}")


def listar(cola):
    if len(cola) == 0:
        print("La cola está vacía.")
    else:
        print("Elementos de la cola (frente -> final):")
        for posicion, elemento in enumerate(cola, start=1):
            print(f"  {posicion}. {elemento}")


def ejecutar_programa():
    cola = []
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
            insertar(cola)
        elif opcion == 2:
            borrar(cola)
        elif opcion == 3:
            listar(cola)
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