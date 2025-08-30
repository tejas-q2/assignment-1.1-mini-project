import pandas as pd

try:
    df = pd.read_csv('Superstore.csv')
    print("Successfully loaded the 'Superstore.csv' file!")
except FileNotFoundError:
    print("Error: Could not find 'Superstore.csv'. Make sure it's in the same folder as this script.")
    exit()

print("\n--- 1. Here are the first 5 rows of your data: ---")
print(df.head())

print("\n--- 2. Here is some information about your dataset: ---")
df.info()

print("\n--- 3. Here is the 'Category' column: ---")
print(df['Category'])

print("\n--- 4. Filtering to show only sales from California: ---")
california_sales = df[df['State'] == 'California']
print(california_sales.head())

print("\n--- 5. Basic statistics for numerical columns: ---")
print(df.describe())

df.to_csv('cleaned_superstore_data.csv', index=False)
