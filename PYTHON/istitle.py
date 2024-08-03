fist_name = input ("Nombre: ")
last_name= input ("Apellido: ")
full_name = f"{fist_name} {last_name}"

print()

print(f"el formato de title () se ha aplicad?: {full_name.istitle()}")
print(f"aplicando el metodo title (): {full_name.title()}")
print (f"Volvemos a imprimir el nombre: {full_name}")
