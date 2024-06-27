#Pandas is a python library used for data manipulation ad analysis.

#From lists
import pandas as pd
data = [10, 20, 30, 40]
s = pd.Series(data, index=["a", "b", "c", "d"])
print("series from list:")
print(s) 

#From arrays
import numpy as np
array_data = np.array([1.1, 2.2, 3.3, 4.4])
s_from_array = pd.Series(array_data, index=["p", "q", "r", "s"])
print("series from array:")
print(s_from_array)

#From dictionaries
dict_data = {"apple": 100, "mango": 200, "banana": 50}
s_from_dict = pd.Series(dict_data)
print("series from dictionary: ")
print(s_from_dict)

#Attributes
print("Index: ", s.index)
print("Values: ", s.values)
print("Data Type: ", s.dtype)
print("Size: ", s.size)

#Methods
print("First two elements: ")
print(s.head(2))
print("Last two elements: ")
print(s.tail(2))
print("Sorted values: ")
print(s.sort_values())
print("Mean: ", s.mean())