repetir = "si"
while repetir=="si":
 try:
  num = int(input("ingrese un numero: "))
  cuadrado = num**2
  print(f"el cuadrado de {num} es :{cuadrado}")
  repetir = input("desea ingresar otro numero? (si/no): ").lower()
 except ValueError: 
  print("error, ingrese un numero")