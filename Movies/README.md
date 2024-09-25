## u.data:
Format: `userID`, `movieID`, `rating`, `timestamp`
## u.item:
Format: `movieID`, `movie_title`, `date`, `IMDb_URL`, `[genres]`
## Small dataset:
- **popular-movies-dataframe**:\
  Sorts all movie IDs by number of reviews using dataframes
- **popular-movies-nice-dataframe**:\
  Shows top 10 most reviewed movies with their names
- **movie-similarities-dataframe**:\
  Gets movie ID as argument and computes top 10 most similar movies using cosine similarity (id 50 = Star Wars (1977))
- **movie-recommendations-als-dataframe**:\
  Gets user ID as argument and computes top 10 movie recommendations based on user reviews using ALS
- **ratings-counter**:\
  Counts the number of reviews for each rating

## Big dataset:
- **movieSimilarities1M**:\
  Gets movie ID as argument and computes top 10 most similar movies using cosine similarity (id 260 = Star Wars: Episode IV - A New Hope (1977))