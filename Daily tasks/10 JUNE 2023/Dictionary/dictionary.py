# A Python dictionary is a mutable, unordered collection that stores data as key-value pairs for efficient data management.
person = {
    'name': 'John Doe',
    'age': 30,
    'address': {
        'street': '123 Main St',
        'city': 'New York',
        'state': 'NY'
    }
}

# Accessing nested data
print(f"Name:  {person['name']}")  
print(f"Address: {person['address']['city']}") 

#Merging two dictionaries
def merge_dicts(dict1, dict2):
    merged = dict1.copy()
    merged.update(dict2)
    return merged

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
merged_dict = merge_dicts(dict1, dict2)
print(merged_dict) 