capi = float(input("ingresa la capital inicial: "))
tasa = float(input("ingresa la tasas de interes anual (en %): "))
periodo = float(input("ingresa el numero de periodo en años: "))
tasaded = tasa/100
cf = capi*(1+tasaded*periodo)
ic = capi*(1+tasaded)**periodo
print(f"capital con interes simple: {cf:.2f}")
print(f"capital con interes compuesto: {ic:.2f}")