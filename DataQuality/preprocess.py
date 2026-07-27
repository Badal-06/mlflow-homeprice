import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv("data/raw.csv")

# Fill missing values
df["Age"] = df["Age"].fillna(df["Age"].mean())

# Convert Yes/No to 1/0
df["Purchased"] = df["Purchased"].map({"Yes": 1, "No": 0})

train, test = train_test_split(df, test_size=0.2, random_state=42)

train.to_csv("data/train.csv", index=False)
test.to_csv("data/test.csv", index=False)

print("Preprocessing completed.")
