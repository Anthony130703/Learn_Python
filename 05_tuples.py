### Tuples ###

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (22, 1.77, "Anthony", "Dolores")
my_other_tuple = (22, 35, 60)

print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])

print(my_tuple.count(1.77))
print(my_tuple.index("Anthony"))

# my_tuple[1] = 1.78  This will raise a TypeError because tuples are inmutable

my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

print(my_sum_tuple[1:4])

my_tuple = list(my_tuple)
print(type(my_tuple))

my_tuple[3] = "Jesus"
my_tuple.insert(1, "Narciso")
my_tuple = tuple(my_tuple)
print(my_tuple)
print(type(my_tuple))

del my_tuple[1] # This will raise a TypeError because tuples are inmutable