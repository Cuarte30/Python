print("Conversor")
print ("================\n")

print ("menu de opciones")

print ("Presiona 1 para convertir de numero a palabra.")
print ("presiona 2 para convertir de palabra a número.")

opcion = int(input("¿ cual es tu opcion deseada?:"))

if opcion == 1:
    print("\n Conversor de numero a palabra. \n")

    opcion_uno = int(input("¡cual es el numero que deseas convertir a palabra?"))

    if opcion_uno == 1:
        print("El numero es 'uno'")
    elif opcion_uno == 2:
        print ("el numero es 'dos'")
    elif opcion_uno ==3:
        print ("el numero es 'tres'")
    elif opcion_uno ==4:
        print ("el numero es 'cuatro'")
    elif opcion_uno ==5:
        print ("el numero es 'cinco'")
    else:
        print ("el numero seleccionado no esta registrado")

    
elif opcion == 2:
    print("\n Conversor de palabra a numero. \n")

    opcion_dos = input("cual es la palabra que desas convertir a numero?: ")
    opcion_dos = opcion_dos.lower()

    if opcion_dos == "uno":
        print("el numero es '1'" )
    elif opcion_dos == "dos":
        print ("el numero es '2'")
    elif opcion_dos == "tres":
        print ("el numero es '3'")
    elif opcion_dos == "cuatro":
        print ("el numero es '4'")
    elif opcion_dos == "cinco":
        print ("el numero es '5'")
    else:
        print ("el numero seleccionado noe sta registrado")
        
else:
    print("opcion no disponible.")
print("fin.")
