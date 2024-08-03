string = "mi mama me mima"
contador = 0

print (string.center(40, "="))

contador = string.count ("M")
print (f"\nLa letra M se encontro {contador} veces en la cadena: {string}")

contador = string.count ("m")
print (f"\nLa letra m se encontro {contador} veces en la cadena: {string}")


contador = string.count ("mama")
print (f"\nLa letra mama se encontro {contador} veces en la cadena: {string}")

contador = string.count ("me mima")
print (f"\nLa oracion me mima se encontro {contador} veces en la cadena: {string}")

contador = string.count ("ma")
print (f"\nLa oracion ma se encontro {contador} veces en la cadena: {string}")

contador = string.count ("m", 13)
print (f"\nLa letra m se encontro {contador} veces, desde la posicion 13 en la cadena: {string}")
contador = string.count ("m", 100)
print (f"\nLa letra m se encontro {contador} veces, desde la posicion 100 en la cadena: {string}")


contador = string.count ("m", -3)
print (f"\nLa letra m se encontro {contador} veces, desde la posicion -3 en la cadena: {string}")

contador = string.count ("m", 3, 7)
print (f"\nLa letra m se encontro {contador} veces, desde la posicion 3 hasta la 7 en la cadena: {string}")
