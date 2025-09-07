while True:
    try:
        repetir = input("¿Desea continuar? (si): ").strip().lower()
        if repetir == "si":
            print("Continuando")
        else:
            print("Fin del programa.")
            break
    except Exception:
        print("Error inesperado. Cerrando programa.")
        break