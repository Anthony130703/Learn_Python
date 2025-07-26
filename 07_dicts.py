### Diccionarios ###

my_dict = dict()
my_other_dict = {}

print(my_dict)
print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"name": "Anthony", "surname": "Dolores", "age": 22, "height": 1.77, 1: "Python"}

my_dict = {"name": "Anthony", 
           "surname": "Dolores", 
           "age": 22, 
           "height": 1.77, 
           "Lenguajes": {"Python", "Java", "C++"}}

print(my_other_dict)
print(my_dict)

print(len(my_other_dict))
print(len(my_dict))

print(my_dict["name"])

my_dict["name"] = "Jesus"
print(my_dict["name"])

my_dict["Calle"] = "Calle Falsa 123"
print(my_dict)

my_dict["Lenguajes"].add("JavaScript")
print(my_dict)

del my_dict["Calle"]
print(my_dict)

print("Jesus" in my_dict)
print("name" in my_dict)

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())

my_list = ["Name", "Surname", "Age"]

my_new_dict = my_other_dict.fromkeys(my_list, "vacio")
print(my_new_dict)

my_new_dict = dict.fromkeys(my_dict)
print(my_new_dict)

my_values = my_new_dict.values()
print(my_values)
