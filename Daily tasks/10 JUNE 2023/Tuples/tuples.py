# Tuples are immutable collections of items, ordered and written in round brackets.
y= ("apple", "banana", "cherry")
print(y)

# Allow Duplicates:
x= ("apple", "banana", "cherry", "apple", "cherry")
print(x)

#Tuple Length:
thistuple = tuple(("apple", "banana", "cherry"))
print(len(thistuple))

#Different datatypes
tuple1 = ("abc", 34, True, 40, "male")
print(tuple1)

w = ("apple", "banana", "cherry")
print(w[1])

#This example returns the items from index -4 (included) to index -1 (excluded)
l = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(l[-4:-1])

# Joining two tuples
tuple3 = (1, 2, 3)
tuple2 = (4, 5, 6)

joined_tuple = tuple3 + tuple2

print("Joined tuple:", joined_tuple) 

#Multiplying tuple
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)
     
     


     