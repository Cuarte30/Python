print ("Calciuladora con una sola variable \n")

print ("*************")
print ("* Menu de opciones *")
print ("*********************")

print ("1. Suma")
print ("2. Resta")
print ("3. Multiplicacion")
print ("4. Division")
print ("5. Division Entera")
print ("6. Exponente")
print ("7. Modulo o resto \n")

numero = int (input("Introduce la opcion deseada:"))

if numero == 1:

    print("elegiste suma \n")
    numero = int (input("introduce el primer numero:"))
    numero += int (input("introduce el segundo numero:"))
    print ("El resultado de la suma es:", numero)
elif numero == 2:

    print("elegiste resta \n")
    numero = int (input("introduce el primer numero:"))
    numero -= int (input("introduce el segundo numero:"))
    print ("El resultado de la resta es:", numero)

    

elif numero == 3:

    print("elegiste multiplicacion \n")
    numero = int (input("introduce el primer numero:"))
    numero *= int (input("introduce el segundo numero:"))
    print ("El resultado de la multiplicacion es:", numero)

elif numero == 4:

    print("elegiste Division \n")
    numero = float (input("introduce el primer numero:"))
    numero /= float (input("introduce el segundo numero:"))
    print ("El resultado de la division es:", round(numero, 2))
    

elif numero == 5:

    print("elegiste Division Entera \n")
    numero = int (input("introduce el primer numero:"))
    numero //= int (input("introduce el segundo numero:"))
    print ("El resultado de la division entera es:", numero)

elif numero == 6:

    print("elegiste Exponente \n")
    numero = int (input("introduce el primer numero:"))
    numero **= int (input("introduce el segundo numero:"))
    print ("El resultado de la exponencial es:", numero)

elif numero == 7:

    print("elegiste Modulo o resto \n")
    numero = int (input("introduce el primer numero:"))
    numero %= int (input("introduce el segundo numero:"))
    print ("El  modulo es:", numero)

else:
    print ("La opcion elegida no existe, vuelve a intentar.")





