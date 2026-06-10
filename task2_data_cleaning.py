import pandas as pd

# Load dataset
df = pd.read_excel("sample_-_superstore (1).xls")

print("===== First 5 Rows =====")
print(df.head())

print("\n===== Missing Values =====")
print(df.isnull().sum())

# Handle missing values
df.fillna("Unknown", inplace=True)

print("\n===== Duplicate Rows =====")
print(df.duplicated().sum())

# Remove duplicate rows
df.drop_duplicates(inplace=True)

# Convert date columns
df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Ship Date"] = pd.to_datetime(df["Ship Date"])

print("\n===== Data Types =====")
print(df.dtypes)

# Export cleaned data
df.to_csv("Cleaned_Superstore.csv", index=False)

print("\nData Cleaning Completed Successfully!")
print("File saved as Cleaned_Superstore.csv")