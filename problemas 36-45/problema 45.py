def realizar_operacion(op):
    while True:
        try:
            a = float(input("Primer número: "))
            b = float(input("Segundo número: "))

            if op == "+":
                print(f"Resultado: {a + b}")
            elif op == "-":
                print(f"Resultado: {a - b}")
            elif op == "*":
                print(f"Resultado: {a * b}")
            elif op == "/":
                print(f"Resultado: {a / b}")
            elif op == "**":
                print(f"Resultado: {a ** b}")
            elif op == "%":
                print(f"Resultado: {a % b}")
            else:
                print("Operación no válida.")
        except Exception as e:
            print(f"Error: {e}")

        repetir_op = input("¿Deseas repetir esta operación? (si/no): ").lower()
        if repetir_op != "si":
            break

while True:
    operacion = input("Elige operación (+, -, *, /, **, %): ")
    realizar_operacion(operacion)

    continuar = input("¿Deseas realizar otra operación distinta? (si/no): ").lower()
    if continuar != "si":
        print("fin.")
        break