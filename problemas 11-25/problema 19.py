nom = input("ingrese nombre del alumno: ")
boleta = int(input("ingrse numero de boleta: "))
cal1 = float(input("ingrse calificacion 1: "))
cal2 = float(input("ingrse calificacion 2: "))
cal3 = float(input("ingrse calificacion 3: "))
cal4 = float(input("ingrse calificacion 4: "))
cal5 = float(input("ingrse calificacion 5: "))
prom = (cal1+cal2+cal3+cal4+cal5)/5
print(f"el alumno: {nom} con la boleta: {boleta} tiene un promedio de: {prom}")