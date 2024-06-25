fruits = ["apple", "mango", "cherry"]

# Append
fruits.append("orange")
print(f"Append: {fruits}")

# Insert
fruits.insert(1, "grape")
print(f"Insert: {fruits}")

# Remove
fruits.remove("mango")
print(f"Remove: {fruits}")

# Copy
# Shallow Copy
fruits_shallow_copy = fruits.copy()
fruits_shallow_copy[0] = "lemon"  
print(f"Shallow Copy: {fruits_shallow_copy}, Original: {fruits}")

# Deep Copy
import copy
fruits_deep_copy = copy.deepcopy(fruits)
fruits_deep_copy[0] = "watermelon"  
print(f"Deep Copy: {fruits_deep_copy}, Original: {fruits}")

# Count
fruits.append("apple")
apple_count = fruits.count("apple")
print(f"Count of 'apple': {apple_count}")

# Extend
more_fruits = ["papaya", "banana"]
fruits.extend(more_fruits)
print(f"Extend: {fruits}")

# Index
apple_index = fruits.index("apple")
print(f"Index of 'apple': {apple_index}")

# Sort
fruits.sort() 
print(f"Sort: {fruits}")

# Reverse
fruits.reverse()
print(f"Reverse: {fruits}")

# Clear
fruits.clear()
print(f"Clear: {fruits}")

#Remove or Pop
removed_fruit = more_fruits.pop()  
print(f"Pop: {removed_fruit}, Remaining: {more_fruits}")

#  list of squares for numbers from 0 to 9
squares = [x ** 2 for x in range(10)]
print("List of squares:", squares)

  

