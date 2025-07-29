### Sets ###

my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set)) # Inicialmente es un diccionario

my_other_set = {22, 1.77, "Anthony", "Dolores"}
print(type(my_other_set))

print(len(my_other_set))

my_other_set.add("Narciso")
print(my_other_set) # Un set no es una estructura ordenada

my_other_set.add("Narciso")
print(my_other_set) # No se agregará porque "Narciso" ya existe

print("Narciso" in my_other_set) # Verifica si el elemento está en el set

my_other_set.remove("Narciso")
print(my_other_set) # Elimina el elemento "Narciso"

my_other_set.clear() # Elimina todos los elementos del set
print(my_other_set)
print(len(my_other_set)) # Deberia ser 0

del my_other_set # Elimina el set por completo
# print(my_other_set) Esto generara un NameError porque my_oyher_set ya no existe

my_set = {22, 1.77, "Anthony", "Dolores"}
my_list = list(my_set)
print(my_list)
print(my_list[0])

my_other_set = {"Anthony", "Dolores", "Narciso"}

my_new_set = my_set.union(my_other_set) # Unión de sets
print(my_new_set.union(my_new_set))

print(my_new_set.difference(my_set))