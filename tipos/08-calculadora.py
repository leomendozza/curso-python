n1 = input("Ingrese primer numero")
n2 = input("Ingrese segundo numero")

n1 = int(n1)
n2 = int(n2)

suma = n1 + n2
resta = n1 - n2
mult = n1 * n2
div = n1 / n2

mensaje = f"""
Para los numeros {n1} y {n2},
el resultado de la sumas es {suma}.
el resultado de la resta es {resta}.
el resultado de la multiplicacion es {mult}
el resultado de la division es {div}
"""
print(mensaje)