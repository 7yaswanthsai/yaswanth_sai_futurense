# A set is a collection of distinct elements, useful for membership checks, removing duplicates, and mathematical operations like union and intersection.
#A set can be created using curly braces '{}' or using 'set()' constructor.
# Using curly braces
my_set = {1, 2, 3, 5}

# Using set() constructor
another_set = set([4, 5, 6, 7, 8])

#print
print("Set created using '{}' curly brackets:",my_set)
print("Set created using set constructor:",another_set)

#Union Operation
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1 | set2 
print("Union:",union_set)

#Intersection Operation
intersection_set = set1 & set2 
print("Intersection:",intersection_set)

#Difference
difference_set = set1 - set2 
print("Difference:",difference_set)

#Add, remove, discard, pop, clear, copy andupdate operations.
my_set.add(4)
print("After add():",my_set)

my_set.remove(2)
print("After remove():",my_set)

my_set.discard(2)
print("After discard():",my_set)

removed_element = my_set.pop()
print("After pop():",removed_element)

my_set.clear()
print("After clear():",my_set)

copied_set = my_set.copy()
print("After copy():",copied_set)

my_set.update([4, 5])
print("After update():",my_set)