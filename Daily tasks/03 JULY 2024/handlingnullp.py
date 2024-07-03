import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.image as mpimg
df = pd.read_csv("C:/Users/91903/Desktop/Data-Science-Content-main/Data-Science-Content-main/Daily tasks/03 JULY 2024/Loan 1.csv")
df.head(5)

df.isnull()

df.isnull().sum()

df.info()

#Null to 0
df2 = df["Dependents"].fillna(value=0)
df2.head(5)
df2.isnull().sum()

#Nan value replaced to previous value
df3 = df.fillna(method='pad')
df3

#Null value with value of next row
df4 = df.fillna(method='bfill')
df4

#Null values with previous value but colums wise
df5 = df.fillna(method='pad',axis=1)
df5

image_path = "C:/Users/91903/Desktop/Data-Science-Content-main/Data-Science-Content-main/Daily tasks/03 JULY 2024/Screenshot (253).png"
img = mpimg.imread(image_path)
plt.imshow(img)
plt.axis('off')
plt.title('Symmetric Distribution')
plt.show()

plt.figure(figsize=(16, 8))

#Histogram
plt.subplot(1, 2, 1)
sns.histplot(df['Income (USD)'], kde=True)
plt.title('Histogram of Income (USD)')
plt.xlim(0, 10000)

#Density plot
plt.subplot(1, 2, 2)
sns.kdeplot(df['Income (USD)'], shade=True)
plt.title('Density Plot of Income (USD)')
plt.xlim(0, 10000)
plt.tight_layout()
plt.show()


df['Income (USD)'].median()

#Null values with mean of a column
df6 = df['Income (USD)'].fillna(value=df['Income (USD)'].median())
print(df6)

fig, axs = plt.subplots(1, 3, figsize=(16, 6), sharey=True)
#Before vs After
sns.histplot(df['Income (USD)'], kde=True, color='lightblue', bins=40, ax=axs[0])
axs[0].set_title("Original Data Distribution")
axs[0].set_xlabel("Income (USD)")
axs[0].set_ylabel("Frequency")
axs[0].set_xlim(0, 10000)

sns.histplot(df6, kde=True, color='green', bins=40, ax=axs[1])
axs[1].set_title("Data Distribution after Filling with Median")
axs[1].set_xlabel("Income (USD)")
axs[1].set_xlim(0, 10000)
plt.xlim(0, 10000)
plt.show()

#Drop all the rows with null values
df7 = df.dropna()
df7

df8 =df.dropna(how='any')
df8

df9 = df.dropna(how='all')
df9

#Rows where specific columns have null values
df10 = df.dropna(subset=['Type of Employment', 'Dependents'])
df10

#Drop row with atleast 4 nulls
df11 =  df.dropna(thresh=4)
df11

#Interpolation
df_interpolated = df.copy()
df_interpolated['Income (USD)_interpolated'] = df['Income (USD)'].interpolate(method='linear')
plt.figure(figsize=(18, 8))

#Original vs Interpolated
plt.subplot(1, 2, 1)
sns.histplot(df['Income (USD)'], kde=True, color='lightblue', bins=40)
plt.title('Original Data Distribution')
plt.xlabel('Income (USD)')
plt.ylabel('Frequency')
plt.xlim(0, 10000)

plt.subplot(1, 2, 2)
sns.histplot(df_interpolated['Income (USD)_interpolated'], kde=True, color='green', bins=40)
plt.title('Data Distribution after Interpolation')
plt.xlabel('Income (USD)')
plt.ylabel('Frequency')
plt.xlim(0, 10000)
plt.tight_layout()
plt.show()

#Replace
df12 = df.replace(to_replace= np.nan, value= 0)
df12

image_path = "C:/Users/91903/Desktop/Data-Science-Content-main/Data-Science-Content-main/Daily tasks/03 JULY 2024/Screenshot (254).png"
img = mpimg.imread(image_path)
plt.imshow(img)
plt.axis('off')  
plt.show()

#Quartiles
q1 = df['Age'].quantile(0.25)
q2 = df['Age'].quantile(0.5)
q3 = df['Age'].quantile(0.75)
print("First Quartile (Q1):", q1)
print("Median (Q2):", q2)
print("Third Quartile (Q3):", q3)

sns.boxplot(x=df['Age'])
plt.title('Box Plot for Age')
plt.show()

#Before vs After
q1 = df['Age'].quantile(0.25)
q2 = df['Age'].quantile(0.5)
q3 = df['Age'].quantile(0.75)

print("First Quartile (Q1):", q1)
print("Median (Q2):", q2)
print("Third Quartile (Q3):", q3)
plt.figure(figsize=(10, 6))
plt.hist(df['Age'], bins=30, color='lightblue', edgecolor='black')
plt.axvline(x=q1, color='red', linestyle='--', label='Q1 (25th percentile)')
plt.axvline(x=q2, color='green', linestyle='--', label='Q2 (50th percentile)')
plt.axvline(x=q3, color='blue', linestyle='--', label='Q3 (75th percentile)')
plt.title('Histogram of Age - Original Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.legend()
plt.grid(True)
plt.show()

iqr = q3 - q1  # Interquartile Range
lower_whisker = q1 - 1.5 * iqr
upper_whisker = q3 + 1.5 * iqr

print("Lower Whisker:", lower_whisker)
print("Upper Whisker:", upper_whisker)

df_lower_filled = df.fillna(lower_whisker)
df_upper_filled = df.fillna(upper_whisker)
plt.figure(figsize=(14, 6))

#Lower whisker
plt.subplot(1, 2, 1)
plt.hist(df_lower_filled['Age'], bins=30, color='orange', edgecolor='black')
plt.axvline(x=lower_whisker, color='red', linestyle='--', label='Lower Whisker')
plt.title('Histogram of Age - Filled with Lower Whisker')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.legend()
plt.grid(True)

#Upper whisker
plt.subplot(1, 2, 2)
plt.hist(df_upper_filled['Age'], bins=30, color='green', edgecolor='black')
plt.axvline(x=upper_whisker, color='blue', linestyle='--', label='Upper Whisker')
plt.title('Histogram of Age - Filled with Upper Whisker')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()

from sklearn.impute import KNNImputer
#KNN imputation
imputer = KNNImputer(n_neighbors=5)
df_knn_imputed = pd.DataFrame(imputer.fit_transform(df[columns_for_knn]), columns=columns_for_knn)
plt.figure(figsize=(14, 10))
for i, col in enumerate(columns_for_knn, 1):
    plt.subplot(3, 2, i)
    plt.hist(df_knn_imputed[col], bins=30, color='green', edgecolor='black')
    plt.title(f'Histogram of {col} - After KNN Imputation')
    plt.xlabel(col)
    plt.ylabel('Frequency')
    plt.grid(True)

plt.tight_layout()
plt.show()

from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
#MICE(Multiple imputation buy chianed equations)
imputer_mice = IterativeImputer(random_state=0)
df_mice_imputed = pd.DataFrame(imputer_mice.fit_transform(df[columns_for_knn]), columns=columns_for_knn)
plt.figure(figsize=(14, 10))
for i, col in enumerate(columns_for_knn, 1):
    plt.subplot(3, 2, i)
    plt.hist(df_mice_imputed[col], bins=30, color='orange', edgecolor='black')
    plt.title(f'Histogram of {col} - After MICE Imputation')
    plt.xlabel(col)
    plt.ylabel('Frequency')
    plt.grid(True)

plt.tight_layout()
plt.show()