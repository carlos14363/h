cantpre = int(input("ingrese el total de preguntas: "))
correctas = int(input("cuantas preguntas estan correctas: "))
if correctas<=cantpre:
    calificacion = (correctas/cantpre)*10
else:
    print("invalido")
print(f"la calificacion es: {calificacion:.2f}")
