### Classes ###

class MyEmptyPerson:
    pass

print(MyEmptyPerson)
print(MyEmptyPerson())

class Person:
    def __init__(self, name, surname, alias = "Sin alias"):
        self.full_name = f"{name} {surname} ({alias})"
        self.__name = name # Atributo privado

    def get_name(self):
        return self.__name

    def walk(self):
        print(f"{self.full_name} está caminando")

my_person = Person("Anthony", "Dolores")
print(my_person.full_name)
print(my_person.get_name())
my_person.walk()

my_other_person = Person("Anthony", "Dolores", "Tony")
print(my_other_person.full_name)
my_other_person.walk()
my_other_person.full_name = "Héctor de León (El loco de los perros)"
print(my_other_person.full_name)