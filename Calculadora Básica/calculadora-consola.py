print("########## Calculadora Básica en Python 🧮 ##########")

while True:
    print("\nOpciones: ")
    print("\t1. Suma")
    print("\t2. Resta")
    print("\t3. Multiplicación")
    print("\t4. División")
    print("\t5. Salir")

    try:
        operacion = int(input("Elige una operación (1-5): "))

        if operacion == 5:
            print("Gracias por usar la calculadora, adios! 👋")
            break

        if operacion < 1 or operacion > 5:
            print("Opción no válida. Por favor, elige una opción entre 1 y 5.")
            continue
    
        num1 = float(input("Introduce el primer número: "))
        num2 = float(input("Introduce el segundo número: "))

        if operacion == 1:
            resultado = num1 + num2
            print(f"La suma es: {resultado}")
        elif operacion == 2:
            resultado = num1 - num2
            print(f"La resta es: {resultado}")
        elif operacion == 3:
            resultado = num1 * num2
            print(f"La multiplicación es: {resultado}")
        elif operacion == 4:
            if num2 != 0:
                resultado = num1 / num2
                print(f"La división es: {resultado}")
            else:
                print("✖️ Error: No se puede dividir entre 0.")

    except ValueError:
        print("⚠️ Entrada no válida. Por favor, introduce un número")