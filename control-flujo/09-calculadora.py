print("Bienvenido a la calculadora")
print("Para salir escribe salir")
print("Las operaciones que puedes usar son la suma, resta, mult, y div")

resultado = ""
while True:
    if not resultado:
        resultado = input("ingrese el numero: ")
        if resultado.lower() == "salir":
            break
        resultado = int(resultado)
    op = input ("ingresa la operacion: ")
    if op.lower() == "salir":
        break
    n2 = input("ingrese el segundo numero: ")
    if n2.lower() == "salir":
        break
    n2 = int(n2)
    
    if op.lower() == "suma":
        resultado += n2
    elif op.lower() == "resta":
        resultado -= n2
    elif op.lower() == "mult":
        resultado *= n2
    elif op.lower() == "div":
        resultado /= n2
    else:
        print("la operacion no es valida")
        break
    
    print(F"el resultado es {resultado}")