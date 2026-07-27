import pandas as pd
import joblib

# Read CSV
df = pd.read_csv("data/house_prices.csv")

# Save DataFrame
joblib.dump(df, "data/house_prices.joblib")

print("DataFrame saved successfully.")


#Load

# Load DataFrame
df = joblib.load("data/house_prices.joblib")

print(df.head())
