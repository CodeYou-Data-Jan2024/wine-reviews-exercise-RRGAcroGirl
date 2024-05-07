# import pandas 
import pandas as pd

# Read wine mag data
wine_reviews = pd.read_csv("data/winemag-data-130k-v2.csv.zip")

# Group data by county and then list the number of reviews and the average point per each country
reviews_country = wine_reviews.groupby(['country']).points.agg([len, "mean"]).round(decimals=1)
reviews_country = reviews_country.rename(columns={"county": 'country', 'len': "count", 'mean': "points"})

# create a csv file in the data folder
reviews_country.to_csv("data/reviews-per-country.csv")
