animal = "chanchito feliz"
print(animal.upper()) #mayuscula
print(animal.lower()) #miniscula
print(animal.capitalize()) #Primera letra de la primer palabra en mayusq
print(animal.title()) #la primera letra de cada palabra en mayusq
print(animal.strip()) #remueve los espacios en blaco a la izq y derecha
print(animal.lstrip()) 
print(animal.rstrip())
print(animal.find("to")) #busca una cadena de caracteres
print(animal.replace("nch", "j")) #busca una cadena de caracteres y las reemplaza por lo q quiera
print("nch" in animal) #si la cadena se encuentra devuelve un boleano frue o false
print("nch" not in animal) #si no se encuentra devuelve true o false