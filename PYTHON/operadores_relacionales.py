print ("introduce dos numeros a comparar: ")

num_uno = int(input("Introduce el primer numero: "))
num_dos = int(input("Introduce el segundo numero:"))

print("\n Los numeros a comrpar son: ", num_uno, "y", num_dos, "\n")

if num_uno == num_dos:
    print("Es igual...")
if num_uno != num_dos:
    print("Es diferente..")
if num_uno < num_dos:
    print("Es menor..")
if num_uno > num_dos:
    print ("es mayor..")
if num_uno <= num_dos:
    print ("es menor o igual...")
if num_uno >= num_dos:
    print("Es mayor o iguall...")


