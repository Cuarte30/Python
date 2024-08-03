#CONJUNCION

print ("Conjuncion (and)")

num_uno= int(input("Escribe un numero mayor a 2 y menor a 5:"))

if num_uno > 2 and num_uno < 5:
    print("El numero ", num_uno, " cumple con la condicion. \n")

else:
    print("el numero ", num_uno, "NO cumple con la condicino. \n")


#Disyuncion


print ("Disyuncion (or)")
palabra = input ("para cunnplir con la condicion escribe 'si' o 'yes':")

if palabra == "si" or palabra == "yes":
    print("la condicion se ha cumplido")
 

else:
     print ("la condicion no se ha cumplido")

#Negacion


print("negacion (not)")

num_uno = int (input("introduce un numero iguala 5:"))

if not num_uno == 5:
    print ("el numero es difereente de cinco y si cumple la condicion")
else:
    print ("el numero es igual a cinco y no cumple la condicion")

