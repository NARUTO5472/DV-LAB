import pandas as pd

# Read CSV file into a DataFrame
df = pd.read_csv("Movies.csv")

# Find the movie with the highest rating
highest_rated_movie = df.loc[df["Rating"].idxmax()]
print("Movie with the Highest Rating:")
print(highest_rated_movie)

# Filter Hindi movies
hindi_movies = df[df["Language"] == "Hindi"]

# Save Hindi movies to a new CSV file
hindi_movies.to_csv("HindiMovies.csv", index=False)

print("HindiMovies.csv file created successfully!")

