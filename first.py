global lista
lista = list()

#version 0.1

on_lamp = "      .\n .    |    ,\n  \   '   /\n   ` ,-. '\n--- (   ) ---\n     \ /\n    _|=|_\n   |_____|"
off_lamp = "     ,-.\n    (   )\n     \ /\n    _|=|_\n   |_____|"


titulo_0 = "Welcome to"
titulo_1 = "**THE LAMP**"

print(

)

print(titulo_0)
print(titulo_1)

print(

)


#Comienzo de la aplicacion (terminado)
def startApp():
    print(

    )
    print("**Empezó la aplicación**")

    print(
        
    )

    op_1 = "0"
        
    while op_1 != "3":
        print("Que quieres hacer?")
        print("1. Encender la lampara")
        print("2. No encender la lampara")
        print("3. Volver hacia atras")
        op_1 = input("Digite su opción: ")
        print(
        
        )
        print("**********************************************")

        if op_1 == "1":
            
            print(on_lamp)
            print(

            )
            print("**********************************************")
        elif op_1 == "2":
            print(

            )
            print(off_lamp)
        
            print(
                
            )
            print("**********************************************")
        elif op_1 == "3":
            print(

            )
            print("GOING BACK TO THE FUTURE")
            
        else:
            print(

            )
            print("No se ha ingresado un digito valido")
            print(

            )

#Mensaje de aplicacion terminada (terminado)
def exitApp():
    
    print(
        
    )
    print("Nos vemos...\nEspero que vuelvas en otra ocación")

#Menu principal (terminado)
def menu():
    
    print("**********************************************")
    print(
        
    )

    op = "0"

    while op != "2":
        print("1. Empezar la aplicación?")
        print("2. Salir de la aplicación")
        op = input("Digite su opción: ")
        print(
        
        )
        print("**********************************************")

        if op == "1":
            
            startApp()
            print(
                
            )
            print("**********************************************")
        elif op == "2":
            
            exitApp()
            print(
                
            )
            print("**********************************************")
        else:
            
            print("No se ha ingresado un digito valido")
            print(

            )
  
menu()