### Loops ###

# While loop example

my_condition = 0

while my_condition < 5:
    print("El valor de my_condition es:", my_condition)
    my_condition += 1
else: # Es opcional, se ejecuta al finalizar el bucle
    print("Mi condición es mayor o igual a 5 ", my_condition)


while my_condition < 20:
    my_condition += 2
    if my_condition == 15:
        print("Mi condición es igual a 15")

    print("Mi condición es menor que 20 ", my_condition)

print("La ejecución continua")