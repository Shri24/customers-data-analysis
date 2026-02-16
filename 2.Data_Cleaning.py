
# install the pandas 
import pandas as pd


# import the csv file 
df = pd.read_csv(
    r"C:\\Users\\srika\\Downloads\\messy_IMDB_dataset.csv",
    sep=";",
    encoding="latin1")
print(df.head())


# display column names,datatypes and non-null counts
print("\nDataset Info:\n")
print(df.info())


# shows how many missing values are present in each column.
print("\nMissing Values:\n")
print(df.isna().sum())


# Clean column names
df.columns = df.columns.str.strip()

# Replace spaces with underscore for easier access
df.columns = df.columns.str.replace(" ", "_")

print("\nCleaned Column Names:\n")
print(df.columns)


#  Remove rows where all values are missing
df = df.dropna(how="all")


# Fix Numeric Columns
# Clan & Convert numeric columns
numeric_columns = ["duration", "votes", "score", "income"]

for col in numeric_columns:
    if col in df.columns:
        df[col] = (
            df[col]
            .astype(str)
            .str.replace("$", "", regex=False)
            .str.replace("Inf", "", regex=False)
            .str.strip()
        )
        df[col] = pd.to_numeric(df[col], errors="coerce")


# Convert Date Column
        if "release_date" in df.columns:
         df["release_date"] = pd.to_datetime(
        df["release_date"],
        errors="coerce"
    )
         
# Fill numeric columns with median
for col in numeric_columns:
    if col in df.columns:
        df[col].fillna(df[col].median(), inplace=True)
        

# Fill categorical columns with "Unknown"
categorical_cols = df.select_dtypes(include="object").columns

for col in categorical_cols:
    df[col].fillna("Unknown", inplace=True)

# Remove Duplicates
df = df.drop_duplicates()

# Save Final Clean Dataset
df.to_csv("final_cleaned_IMDB_dataset.csv", index=False)
print("\nFinal cleaned file saved successfully!")
