total = 0
while total <= 100000:
    try:
        abono = float(input("¿Cantidad a abonar?: "))
        if abono < 0:
            print("Error: no se aceptan cantidades negativas.")
        else:
            total += abono
            print(f"Total acumulado: ${total:.2f}")
    except ValueError:
        print("Entrada inválida. Intenta de nuevo.")
print("¡Meta alcanzada!")