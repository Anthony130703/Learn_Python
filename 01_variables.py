# Variables

my_string_variable = "My String variable"
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = False
print(my_bool_variable)

# Concatenación de variables en un print
print(my_string_variable, my_int_variable, my_bool_variable)
print("Este es el valor de:", my_bool_variable )

# Algunas funciones del sistema
print(len(my_string_variable))

# Variables en una sola línea. ¡Cuidado con abusar de esta sintaxis!
name, surname, alias, age = "Anthony", "Dolores", "Tony", 22
print("Me llamo:", name, surname, ". Mi edad es:", age, ". Y mi alias es:", alias)

# Inputs
""""
name = input("What is your name: ")
age = input("How old are you: ")

print(name)
print(age)
"""

# Cambiamos su tipo
name = 35
age = "Anthony"
print(name)
print(age)

# ¿Forzamos el tipo?
address: str = "Mi direccion"
address = 32
print(address)