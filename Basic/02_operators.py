## Operadores Aritmético ##

print(3 + 4)
print(3 - 4)
print(3 * 4)
print(3 / 4)
print(3 % 4) # Calcula el modulo o mejor dicho el resto
print(3 // 4) # Este calcula la division y nos da el numero entero
print(2 ** 3) # Calcula el exponente

print("Hola " + "Python")
print("Hola " + str(5))
print("Hola " * 3)
print("Hola " * (2 ** 3))

my_float = 2.5 * 2
print( "Hola " * int(my_float))

## Operadores Comparativos ##

print(3 > 4)
print(3 < 4)
print(3 >= 4)
print(3 <= 4)
print(3 == 4)
print(3 != 4)

print("Hola" > "Python")
print("Hola" < "Python")
print("Hola" >= "Zola") # Esta comparando una ordenacion alfabética por ASCII
print(len("Hola") <= len("Python")) # Cuenta caracteres
print("Hola" == "Python")
print("Hola" != "Python")

## Operadores Lógicos ##

print(3 > 4 and "Hola" > "Python")
print(3 > 4 or "Hola" > "Python")
print( not 3 > 4 and  not "Hola" > "Python")