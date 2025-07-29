## Lists ##

my_list = list()
my_other_list = []

print(len(my_list))

my_list = [1, 2, 3, 4, 5]

print(my_list)
print(len(my_list))

my_other_list = [35, 1.70, "Anthony", "Dolores"]

print(type(my_other_list))
print(type(my_list))

print(my_other_list[0])

print(my_other_list.count(1.70)) # El .count() cuenta cuantas veces aparece un elemento en la lista
print(my_other_list.index("Anthony")) # El .index() devuelve el indice del elemento buscado

age, height, name, surname = my_other_list
print(age)

print(my_list + my_other_list) # Concatenacion de listas
print(my_list * 2) # Repeticion de listas
print(my_list[1:3]) # Slice de listas

my_other_list.append("Python") # Agrega un elemento al final de la lista
print(my_other_list)

my_other_list.insert(1, "Rojo") # Inserta un elemento en una posicion especifica
print(my_other_list)

my_other_list[1] = "Verde" 
print(my_other_list)

my_other_list.remove("Verde") # Elimina el primer elemento que coincida con el valor
print(my_other_list)

my_other_list.pop() # Elimina el utlimo elemento de la lista
print(my_other_list)

my_other_list.pop(1) # Elimina el elemento en la posicion indicada
print(my_other_list)

del my_list[1]
print(my_list)

my_new_list = my_list.copy()

my_list.clear() # Elimina todos los elementos de la lista
print(my_list)
print(my_new_list)

my_new_list.reverse() # Invierte el orden de los elementos en la lista
print(my_new_list)

my_new_list.sort() # Ordena los elementos de la lista
print(my_new_list)

my_list = "Hola Python" 
print(my_list) # Esto es un string, no una lista

my_list = "Hola Python".split() # Convierte un string en una lista
print(my_list)
print(type(my_list))