### Funciones ###

def my_function():
    print("Esto es una función")

my_function()

def sum_two_values(first_values, second_values):
    print(first_values + second_values)

sum_two_values(5, 10)
sum_two_values("5", "7")

def sum_two_values_with_return(first_values, second_values):
    return first_values + second_values

my_result = sum_two_values_with_return(5, 10)
print(my_result)

def print_name(name, surname):
    print(f"{name} {surname}")

print_name("Anthony", "Dolores")

def print_name_with_default(name, surname, alias = "Sin alias"):
    print(f"{name} {surname} {alias}")

print_name_with_default("Anthony", "Dolores")
print_name_with_default("Anthony", "Dolores", "Tony")

def print_upper_texts(*texts):
    for texts in texts:
        print(texts.upper())

print_upper_texts("Hola", "Mundo", "Python")
print_upper_texts("Hola")