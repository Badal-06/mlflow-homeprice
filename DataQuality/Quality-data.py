import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent.parent / "data"
HOUSE_PRICES_FILE = DATA_DIR / "house_prices.csv"
IMDB_FILE = DATA_DIR / "IMDB-Movie-Data.csv"


def analyze_house_prices():
    df = pd.read_csv(HOUSE_PRICES_FILE)
    print("House Prices dataset shape:", df.shape)
    print("Missing values:\n", df.isnull().sum())
    print("Duplicate rows:", df.duplicated().sum())
    print("Columns:", df.columns.tolist())
    print("First 5 rows:")
    print(df.head(5))
    print("Last 5 rows:")
    print(df.tail(5))
    df.info()
    print("Summary statistics:\n", df.describe(include="all"))
    print("Correlation matrix:\n", df.corr())
    print("Non-null count per column:\n", df.count())

    df_clean = df.dropna(how="any")
    print("Shape after dropping rows with any missing values:", df_clean.shape)
    return df, df_clean


def analyze_imdb():
    df = pd.read_csv(IMDB_FILE)
    print("IMDB dataset shape:", df.shape)
    print("Missing values:\n", df.isnull().sum())

    plt.figure(figsize=(8, 6))
    sb.heatmap(df.isnull(), cbar=False, cmap="magma")
    plt.title("Missing values heatmap")
    plt.tight_layout()
    plt.savefig("imdb_missing_heatmap.png")
    print("Saved missing values heatmap to imdb_missing_heatmap.png")

    df_dropped = df.dropna(how="any")
    print("Shape after dropping rows with any missing values:", df_dropped.shape)
    df_dropped.to_csv("df_dropped.csv", encoding="utf-8", index=False)

    df_new = df.copy()
    if "Metascore" in df_new.columns:
        df_new["Metascore"] = df_new["Metascore"].fillna(df_new["Metascore"].mean())
    else:
        print("Column 'Metascore' not found; skipping fillna step.")

    print("Missing values after filling Metascore:\n", df_new.isna().sum())
    df_new.to_csv("df_new.csv", encoding="utf-8", index=False)

    if "Votes" in df_new.columns and pd.api.types.is_numeric_dtype(df_new["Votes"]):
        votes = df_new["Votes"].dropna()
        if len(votes) > 0:
            z_scores = np.abs(stats.zscore(votes))
            df_zscore_filtered = df_new.loc[votes.index[z_scores < 3]]
            print("Shape after Z-score filtering:", df_zscore_filtered.shape)
            df_zscore_filtered.to_csv("df_zscore_filtered.csv", encoding="utf-8", index=False)

        q_low = df_new["Votes"].quantile(0.01)
        q_hi = df_new["Votes"].quantile(0.99)
        df_quantile_filtered = df_new[(df_new["Votes"] > q_low) & (df_new["Votes"] < q_hi)]
        print("Shape after quantile filtering:", df_quantile_filtered.shape)
        df_quantile_filtered.to_csv("df_quantile_filtered.csv", encoding="utf-8", index=False)
    else:
        print("Column 'Votes' not found or not numeric; skipping outlier filtering steps.")

    df1 = pd.concat([df, df.iloc[20:30, :]], ignore_index=True)
    print("Duplicate rows in df1 sample:", df1.duplicated().sum())
    df1 = df1.drop_duplicates(ignore_index=True)
    print("Shape after dropping duplicates:", df1.shape)
    df1.to_csv("df1_no_duplicates.csv", encoding="utf-8", index=False)

    return df, df_dropped, df_new, df1


def main():
    analyze_house_prices()
    analyze_imdb()


if __name__ == "__main__":
    main()
