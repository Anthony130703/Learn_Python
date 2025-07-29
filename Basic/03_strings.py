### Strings ###

my_string = "Mi String"
my_other_string = "Mi otro String"

print(len(my_string))
print(len(my_other_string))

print(my_string + " " + my_other_string)

my_new_line_string = "Este es un string\ncon salto de linea"
print(my_new_line_string)

my_tab_string = "\tEste es un string con tabulacion"
print(my_tab_string)

# Formateo

name, surname, age = "Anthony", "Dolores", 22

print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age))
print("Mi nombre es %s %s y mi edad es %d" %(name, surname, age))
print(f"Mi nombre es {name} {surname} y mi edad es {age}")

# Desempaquetado de caracteres
lenguage = "python"
a , b, c ,d ,e ,f = lenguage
print(a)
print(b)

# División 

lenguage_slice = lenguage[1:3]
print(lenguage_slice)

lenguage_slice = lenguage[1:]
print(lenguage_slice)

lenguage_slice = lenguage[-2]
print(lenguage_slice)

lenguage_slice = lenguage[0:6:2]
print(lenguage_slice)


# Reverse

reversed_lenguage = lenguage[::-1]
print(reversed_lenguage)

# Funciones

print(lenguage.capitalize()) # imprime la primera letra en mayuscula
print(lenguage.upper()) # todo el texto lo imprime en mayuscula
print(lenguage.count("t"))
print(lenguage.isnumeric())
print("1".isnumeric())
print(lenguage.lower())
print(lenguage.upper().isupper())