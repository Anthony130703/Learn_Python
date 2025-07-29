### Loops ###

# While loop example

my_condition = 0

while my_condition < 5:
    print("El valor de my_condition es:", my_condition)
    my_condition += 1
else: # Es opcional, se ejecuta al finalizar el bucle
    print("Mi condición es mayor o igual a 5 ")


while my_condition < 20:
    my_condition += 2
    if my_condition == 15:
        print("Mi condición es igual a 15")
        break

    print(my_condition)

print("La ejecución continua")

# For loop example

my_list = [35, 24, 62, 52, 30, 30, 17]

for element in my_list:
    print(element)

my_tuple = (22, 1.77, "Anthony", "Dolores")

my_other_set = {"Anthony", "Dolores", "Narciso"}

my_other_dict = {"name": "Anthony", "surname": "Dolores", "age": 22, "height": 1.77, 1: "Python"}

for element in my_tuple:
    print(element)

for element in my_other_set:
    print(element)

for element in my_other_dict:
    print(element)

for element in my_other_dict.values():
    print(element)
    if element == "Anthony":
        print("Se ha encontrado a Anthony")
        break
else:
    print("El bucle for ha finalizado")

for element in my_other_dict.values():
    print(element)
    if element == 1.77:
        continue
    print("Se ejecuta")
else:
    print("El bucle for ha finalizado")