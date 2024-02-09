def get_product(**datos): #para guardar varios parametros en uno solo **
    print(datos["id"], datos={"name"})



 #tengo que poner el nombre del parametro obligatoriamente
get_product(id="id",
            name="iphone", 
            des="esto es un iphone") 