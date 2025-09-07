def calcular():
    try:
        a = float(input("Primer número: "))
        b = float(input("Segundo número: "))
        operacion = input("Operación (+, -, *, /, **, %): ")

        if operacion == "+":
            print(f"Resultado: {a + b}")
        elif operacion == "-":
            print(f"Resultado: {a - b}")
        elif operacion == "*":
            print(f"Resultado: {a * b}")
        elif operacion == "/":
            print(f"Resultado: {a / b}")
        elif operacion == "**":
            print(f"Resultado: {a ** b}")
        elif operacion == "%":
            print(f"Resultado: {a % b}")
        else:
            print("Operación no válida.")
    except Exception as e:
        print(f"Error: {e}")

repetir = "si"
while repetir == "si":
    calcular()
    repetir = input("¿Deseas realizar otra operación? (si/no): ").lower()