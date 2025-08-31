pv = int(input("ingrese el precio de venta: "))
cv = int(input("ingrese la cantidad vendida: "))
cf = int(input("ingrese el costo fijo: "))
cvp = int(input("ingrse el costo variable por venta: "))
it = pv*cv
cvt = cvp*cv
ct = cf+cvt 
bf =it-ct
print("\n--- resultados de beneficio ---")
print(f"ingreso totales: $ {it:,.2f}")
print(f"costos totales: $ {ct:,.2f}")
print(f"benefici total: $ {bf:,.2f}")