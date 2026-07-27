import pandas as pd

# Read CSV file
df = pd.read_csv("data/house_prices.csv")

# Save DataFrame as a pickle file
df.to_pickle("data/house_prices.pkl")

print("DataFrame saved as pickle.")


#load pickle
df = pd.read_pickle("data/house_prices.pkl")

print(df.head())
