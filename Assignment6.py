import numpy as np
import pandas as pd

# 0. Create and load a sample .csv file 
sample_data = {
    "Student_ID": [101, 102, 103, 104, 102, 105, 106],
    "Name": ["Aarav", "Priya", "Rohan", "Sneha", "Priya", "Vikram", None],
    "Marks": [85.0, 92.0, np.nan, 78.0, 92.0, 88.0, 65.0],
    "City": ["Pune", "Mumbai", "Pune", None, "Mumbai", "Nagpur", "Pune"],
    "Temp_Notes": ["N/A", "Ok", "Check", "Ok", "Ok", "N/A", "Check"],
}


# Save sample data to a CSV file and read it back
pd.DataFrame(sample_data).to_csv("students.csv", index=False)

# Reading from .csv
df = pd.read_csv("students.csv")
print("--- Original Dataset ---")
print(df)

# 1. Handle Missing Values using fillna() and dropna()

df["Marks"] = df["Marks"].fillna(df["Marks"].mean())

# Fill missing 'City' with a default string
df["City"] = df["City"].fillna("Unknown")

# Drop rows where critical information like 'Name' is missing
df = df.dropna(subset=["Name"])

print("\n--- After Handling Missing Values ---")
print(df)

# 2. Identify & Remove Duplicates and Irrelevant Records
# Check for duplicate rows
print("\nDuplicate rows found:", df.duplicated().sum())

# Remove duplicate rows
df = df.drop_duplicates()

# Remove an irrelevant column using drop()
df = df.drop(columns=["Temp_Notes"])

print("\n--- After Removing Duplicates & Irrelevant Columns ---")
print(df)

# 3. Data Selection and Filtering using loc[]
# Select students from 'Pune' who scored more than 80 marks
filtered_df = df.loc[
    (df["City"] == "Pune") & (df["Marks"] > 80), ["Student_ID", "Name", "Marks"]
]

print("\n--- Filtered Data (Pune Students with Marks > 80) ---")
print(filtered_df)
