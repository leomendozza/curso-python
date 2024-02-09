def hola(nombre, apellido="mendoza"): #parametro (dato) (parametro="" es un parameto opcional)
    print("hola mundo")
    print(f"bienvenido {nombre} {apellido}")
   
    
hola("leo", "mendoza") #ya no es parametro, es un argumento
hola("leonardo", "mendoza")









hola(apellido="mendoza", nombre="leonardo") #orden de paremetros