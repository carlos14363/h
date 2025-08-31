import math
a= float(input("ingrese el 1er numero: "))
b = float(input("ingrese el 2do numero: "))
suma = a+b
resta = a-b
multiplicacion = a*b
poteciacion = a**b
modulo = a%b
if b !=0:
    division = a/b
else: 
    division = "indefinida"
if a >=0:
    raiz = math.sqrt(a)
else:
    raiz = "es un numero imaginario"
print("\n ---resultados ---")
print(f"suma: {a} + {b}= {suma}")
print(f"resta: {a} - {b} = {resta}")
print(f"multiplicacion: {a} * {b} = {multiplicacion}")
print(f"potenciacion: {a} ** {b} = {poteciacion}")
print(f"modulo: {a} % {b} = {modulo}")
print(f"divison: {a} / {b} = {division}")
print(f"raiz del 1er numero ({a}): {raiz}")