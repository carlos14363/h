print("ingresa las coordenadas del 1er punto (x1,y2): ")
x1 = float(input("X1: "))
y1 = float(input("y1: "))
print("\ningresa las coordenadas del 2do punto (x2,y2): ")
x2 = float(input("X2: "))
y2 = float(input("y2: "))
if x2-x1==0: 
    print("\npendiente indefinida")
    print("la ecuacion de la recta es x =",x1)
else:
    m = (x2-x1)/(y2-y1)
b = y1-m*x1
print(f"la pendiente es: {m:.2f}")
print(f"la ecuacion de la recta es: y={m:.2f}x + {b:.2f}")