repetir = "si"
while repetir=="si":
 try:
  c = int(input("ingrese la capital inicial: "))
  i = int(input("ingrese la tasa de interes: "))/100
  n = int(input("ingrese el periodo: "))
  m = c*(1+i)**n
  print(f"el momto final es :{m}:.2f")
  repetir = input("desea hacer otro calculo? (si/no): ").lower()
 except ValueError:
  print("Error: ingrese valores numéricos válidos.")