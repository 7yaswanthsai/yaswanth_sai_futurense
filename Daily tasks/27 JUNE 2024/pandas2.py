import pandas as pd
data = pd.read_csv("C:/Users/91903/Desktop/Data-Science-Content-main/Data-Science-Content-main/Daily tasks/27 JUNE 2024/Loan 1.csv")

df = pd.DataFrame(data)
print(df)

#Creating DataFrame from Dictionaries
data1 = {
    "Customer ID": ["C-26247", "C-35067", "C-34590"],
    "Name": ["Scarlett", "John", "Tom"],
    "Gender": ["F", "M", "M"],
    "Age": [38, 45, 40],
    "Income (USD)": [35000.50, 48500.81, 50100.20],
    "Income stability": ["Low", "High", "High"],
    "Profession": ["Working", "Pensioner", "Working"],
    "Type of employment": ["Sales staff", "Managers", "Sales staff"],
    "Location": ["Rural", "Urban", "Semi-Urban"],
    "Loan amount request (USD)": [10000.59, 12953.81, 86401.65]
}

data2 = pd.DataFrame(data1)
print(data2)

#Creating DataFrame from CSV file
selected_columns = ["Customer ID", "Name", "Gender", "Income (USD)"]
df_from_csv = pd.read_csv("C:/Users/91903/Desktop/Data-Science-Content-main/Data-Science-Content-main/Daily tasks/27 JUNE 2024/Loan 1.csv")
df_from_csv.head()

#Inspection functions
df.info()
df.head(5)
df.describe()
df.isnull.sum()
df.columns
df.dtypes

#Exploration functions
#.values_count()
gender_counts = df["Gender"].values_counts()
print(gender_counts)

#.unique
unique_locations = df["Location"].unique()
print(unique_locations)

#.corr()
correlation_matrix = data2.corr()
print(correlation_matrix)



