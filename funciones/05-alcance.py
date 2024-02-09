saludo = "hola global"#mala practica definir parametros glogales



def saludar():
    global  saludo
    saludo = "hola mundo"
      
def saludoLeo():
    saludo = "hola leo"
    print(saludo)
      
print(saludo)
print(saludo)
