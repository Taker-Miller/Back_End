def menu():
    opcion = "a"
    while opcion != "d":
        print("que desea cotizar?: ")
        print("1- fiesta gala")
        print("2- fiesta cumpleaños")
        print("d para detener programa")
        opcion = input("ingrese una opcion: ")
        if opcion =="1" or opcion =="2":
            cotizar_fiesta(int(opcion))
        
        elif opcion.lower()=="d":
            print("adios")

        else:
            print("la opcion ingresada no es valida")

def cotizar_fiesta(opcion:int):
    if opcion==1:
        cotizar_fiesta_gala()
    else:
        cotizar_fiesta_cum()


def cotizar_fiesta_gala():
    pass


def cotizar_fiesta_cum():
    pass

menu()