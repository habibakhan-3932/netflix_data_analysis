import pandas as pd
import matplotlib.pyplot as plt
# Load cleaned dataset
df = pd.read_csv("netflix_cleaned.csv")
# 1.Movies vs TV Shows count
plt.figure(figsize=(6,4))
df['type'].value_counts().plot(kind='bar')
plt.title("Count of Movies vs TV Shows")
plt.xlabel("Type")
plt.ylabel("Count")
plt.show()
# 2.Top 10 countries producing content
top_countries = df['country'].value_counts().head(10)
plt.figure(figsize=(8,5))
top_countries.plot(kind='bar')
plt.title("Top 10 Countries on Netflix")
plt.xlabel("Country")
plt.ylabel("Number of Titles")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
# 3.Content releases by year
plt.figure(figsize=(8,5))
df['release_year'].value_counts().sort_index().plot(kind='line')
plt.title("Netflix Releases by Year")
plt.xlabel("Year")
plt.ylabel("Count")
plt.grid(True)
plt.show()
# 4.Rating distribution
plt.figure(figsize=(8,4))
df['rating'].value_counts().plot(kind='bar')
plt.title("Rating Distribution")
plt.xlabel("Rating")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.show()
# 5.Movie duration distribution
movie_df = df[df['type'] == "Movie"]
plt.figure(figsize=(8,5))
plt.hist(movie_df['duration'].dropna(), bins=20)
plt.title("Movie Duration Distribution")
plt.xlabel("Minutes")
plt.ylabel("Frequency")
plt.show()
