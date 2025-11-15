import pandas as pd
# 1.Load dataset
df = pd.read_csv("netflix_dataset.csv")
# See first rows
print(df.head())
# 2.Check shape, datatypes & missing values
print(df.shape)
print(df.info())
print(df.isnull().sum())
# 3.Handle missing values
# Fill missing director and cast with "Unknown"
df['director'] = df['director'].fillna("Unknown")
df['cast'] = df['cast'].fillna("Unknown")
# Fill missing country
df['country'] = df['country'].fillna("Unknown")
# Drop rows where title is missing (rare but important)
df = df.dropna(subset=["title"])
# 4.Convert date formats
df["date_added"] = pd.to_datetime(df["date_added"], errors="coerce")
# 5.Clean duration column
df["duration_clean"] = df["duration"].str.extract(r"(\d+)")
df["duration_clean"] = pd.to_numeric(df["duration_clean"])

# Add a column for duration type
df["duration_type"] = df["duration"].apply(
    lambda x: "Minutes" if "min" in x else "Seasons"
)
# 6.Remove duplicates
df = df.drop_duplicates()
# 7. Strip extra spaces in text columns
text_cols = ["title", "director", "cast", "country", "listed_in", "description"]

for col in text_cols:
    df[col] = df[col].astype(str).str.strip()
    df['date_added'] = df['date_added'].fillna('Not Available')
# 8.Save cleaned dataset
df.to_excel("netflix_cleaned.xlsx", index=False)
df.to_csv("netflix_cleaned.csv", index=False)
print("Cleaning complete! Files saved: netflix_cleaned.xlsx and netflix_cleaned.csv")
