contraseña = input("Crea una contraseña: ")
intentos = 0
confirmacion = ""
while confirmacion != contraseña and intentos < 3:
    confirmacion = input("Confirma tu contraseña: ")
    intentos += 1
if confirmacion == contraseña:
    print("Contraseña correcta.")
else:
    print("haz llegado al limite de intentos.")