Spark Scripts:

Customer orders:
- **amount-spent-customer**:\
  Computes total spent by customer_id using RDDs.
- **amount-spent-customer-dataframe**:\
  Computes total spent by customer_id using dataframes.

Marvel Superheroes:
- **degrees-of-separation**:\
  BFS through the graph to find the degree of separation between 2 given superheroes (nodes).
- **most-popular-superhero-dataframe**:\
  Returns the name of the superhero with the most connections in the Graph.
- **most-unpopular-superhero-dataframe**:\
  Returns the names of the superheroes with the minimum number of connections.

Movies:
- **popular-movies-dataframe**:\
  Sorts all movie IDs by number of reviews using dataframes.
- **popular-movies-nice-dataframe**:\
  Shows top 10 most reviewed movies with their names.
- **movie-similarities-dataframe**:\
  Gets movie ID as argument and computes top 10 most similar movies using cosine similarity (id 50 = Star Wars (1977)).
- **movie-recommendations-als-dataframe**:\
  Gets user ID as argument and computes top 10 movie recommendations based on user reviews using ALS.
- **ratings-counter**:\
  Counts the number of reviews for each rating.

Friends count:
- **friends-by-age**:\
  Computes average number of friends for every age using RDDs.
- **friends-by-age-dataframe**:\
  Computes average number of friends for every age using dataframes.
- **spark-sql**:\
  Prints all teens in the dataset and their number of friends. Computes number of people for each age in ascending order.
- **spark-sql-dataframe**:\
  Runs different SQL queries for a dataset with a header.

Temperatures:
- **max-temperatures**:\
  Computes maximum recorded temperatures for the 2 locations using RDDs.
- **min-temperatures**:\
  Computes minimum recorded temperatures for the 2 locations using RDDs.
- **min-temperatures-dataframe**:\
  Computes minimum recorded temperatures for the 2 locations using dataframes.

Regression:
- **spark-linear-regression**:\
  Trains a model with Linear Regression to predict values. Prints pairs of predicted value and the actual value.

real-estate.csv:
- **real-estate-regression**:\
  Trains a model with DecisionTreeRegressor to predict house prices based on house age, distance to public transport, number of convenience stores in proximity. Prints predicted price and actual price for the houses in the test set.

Word counting:
- **word-count**:\
  Counts all words in a text file and prints them sorted in ascending order.
- **word-count-better-sorted-dataframe**:\
  Counts all words in a text file and prints them sorted in ascending order using dataframes.

Streaming:
- **structured-streaming**:\
  Reads server access logs from a logs directory and counts the number of appearances of each status code.
- **windowed-streaming**:\
  Reads server access logs from a logs directory and counts the number of requests for each endpoint in the last 60 seconds. Prints the highest 20 counts every 10 seconds.