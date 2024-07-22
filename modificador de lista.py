
def modificador_de_lista():
    #Esqueleto del programa, aqui la funcion toma el archivo de la direccion ingresada y lo convierte en una lista para ser modificado
    #Asegurarse de que la direccion de la variable "archivo" sea correcta
    eltexto=""
    archivo="Desktop/juegos por jugar prueba.txt"
    with open (archivo, "r") as file1:
        juego=file1.read()
    juegos=juego.split("\n")

    #Funcion que se encarga de añadir elementos a la lista
    #Luego de ingresar el elemento deseado, se le preguntara al usuario si desea ingresar mas elementos, en caso de que no, la funcion continuara
    #Si el usuario añade un elemento igual a un elemento de la lista, la funcion no agregara ese elemento y le pedira al usuario reingresar un elemento
    #Luego la funcion ordenara la lista alfabeticamente
    #Luego la funcion verificara si uno de los elementos de la lista esta vacio, en caso de que si, lo borrara
    #Luego la funcion escribira sobre el archivo original y el usuario volvera al menu principal
    def añadir_juego(lista, lista_nueva):
        respuesta="si"
        while respuesta=="si":
            adiccion=input("Escriba el juego que desea añadir: ")
            for i in lista:
                while adiccion==i:
                    adiccion=input("Este juego ya existe en la lista, añada otro juego: ")
            lista.append(adiccion)
            respuesta=input("Desea añadir un juego mas a la lista? ")
        lista.sort()
        for i in lista:
            if i=="":
                lista.remove("")
        for i in lista:
            lista_nueva=lista_nueva+i+"\n"
        with open(archivo, "w") as file1:
            file1.write(lista_nueva)
        print("Su lista esta ordenada y guardada\n")
        return modificador_de_lista()

    #Funcion que quita elementos de la lista
    #Luego de ingresar un elemento a eliminar, se le preguntara al usuario si desea quitar mas elementos, en caso de que no, la funcion continuara
    #(no añadido aun) Si el usuario ingresa un elemento que no se encuentra en la lista, la funcion le pedira que ingrese nuevamente un elemento
    #Luego la funcion ordenara la lista alfabeticamente
    #Luego la funcion escribira sobre el archivo original y el usuario volvera al menu principal
    def quitar_juego(lista, lista_nueva):
        respuesta="si"
        while respuesta=="si":
            quitar=input("Escriba el juego que desee quitar: ")
            while quitar not in lista:
                quitar=input("No existe ese elemento en la lista, intentelo nuevamente: ")
            lista.remove(quitar)
            respuesta=input("Desea quitar un juego mas de la lista? ")
        lista.sort()
        for i in lista:
            lista_nueva=lista_nueva+i+"\n"
        with open(archivo, "w") as file1:
            file1.write(lista_nueva)
        print("Su lista esta ordenada y guardada\n")
        return modificador_de_lista()

    #Funcion que muestra los elementos del archivo, puede mostrar cuantos elementos hay o cuales son esos elementos
    #(no añadido aun)En caso de introducir una opcion no valida, se le pedira al usuario que vuelva a ingresar una opcion valida
    #Luego de realizar su funcion, la funcion devolvera al usuario al menu principal
    def revisar_lista(lista, lista_nueva):
        opcion2=input("Desea saber cuantos juegos tiene o cuales juegos son?\n1:Cuantos juegos son.\n2:Cuales juegos son\n")
        if opcion2=="1":
            print("Actualmente tiene ", len(lista), " juegos en la lista\n")
        else:
            if opcion2=="2":
                for i in lista:
                    lista_nueva=lista_nueva+i+"\n"
                print("Estos son los juegos que hay en la lista:\n", lista_nueva)
        return modificador_de_lista()

    #Funcion que envia al usuario a las demas funciones a realizar la accion elegida
    #Luego de que las funcion elegida haya hecho su funcion, el usuario volvera a esta funcion hasta que decida salir
    #En caso de introduccir una opcion no valida, se le pedira al usuario volver a ingresar una opcion valida
    def opciones(opcion):
        if opcion == "1":
            return añadir_juego(juegos, eltexto)
        elif opcion == "2":
            return quitar_juego(juegos, eltexto)
        elif opcion == "3":
            return revisar_lista(juegos, eltexto)
        elif opcion == "4":
            print("nos vemos")
        else:
            opcion=input("Introdujo una opcion no valida, intente otra vez\n")
            return opciones(opcion)


    #Menu principal del programa, desde aqui, el usuario puede elegir si quiere añadir, quitar o contar los elementos que hay en la lista
    #Luego la opcion introducida ira a la funcion "opciones"
    opcion=input("Bienvenido, eliga una opcion para modificar la lista:\n1:Añadir un juego a la lista\n2:Quitar un juego de la lista\n3:Revisar la lista\n4:Salir\n")
    opciones(opcion)
            

modificador_de_lista()