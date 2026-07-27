df = pd.read_csv("data/house_prices.csv")

#
Empty cells
Data in wrong format
Wrong data
Duplicates
Missing Values
Outliers

# DF methods
print(df)
df.isnull().sum()
df1.duplicated().sum()
df.dropna(how = 'any')
df.shape() 	# Prints the number of rows as well as columns in a data frame
df.head(n) 	# Prints first n rows of the DataFrame
df.tail(n) 	# Prints last n rows of the DataFrame
df.info() 	# Index, Datatype, and Memory details
df.describe() # Summary statistics for numerical columns
df.apply(pd.Series.value_counts) # Unique values and counts for every columns
df.describe() # brief statistics for numerical columns
df.mean() # Returns the mean of every columns
df.corr() # Returns the correlation between columns in a DataFrame
df.count() # Returns the number of non-null values in each DataFrame column
df.max() # Returns the biggest value in every column
df.min() # Returns the lowest value in every column
df.median() # Returns the median of every column
df.std() # Returns the standard deviation of every column

#cleaning
df.columns = ['a','b','c'] # Renames columns
pd.isnull() # Checks for null Values, Returns Boolean Array
pd.notnull() # Opposite of s is null()
df.dropna() # Drops all rows that contain null values
df.dropna(axis=1) # Drops all columns that contain null values
df.dropna(axis=1,thresh=n) # Drops all rows have have less than n non null values
df.fillna(x) # Replaces all null values with x
s.fillna(s.mean()) # Replaces all null values with the mean (mean can be replaced with almost any function from the statistics section)
s.astype(float) # Converts the datatype of the series to float
s.replace(1,'one') # Replaces all values equal to 1 with 'one'
s.replace([1,3],['one','three']) # Replaces all 1 with 'one' and 3 with 'three'
df.rename(columns=lambda x: x + 1) # Mass renaming of columns
df.rename(columns={'old_name': 'new_ name'}) # Selective renaming
df.set_index('column_one') # Changes the index
df.rename(index=lambda x: x + 1) # Mass renaming of index  
 


##python
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

df = pd.read_csv('IMDB-Movie-Data.csv')

#1 Missing Values
#will return the sum of missing values within each column in the data frame
df.isnull().sum()

#2 visually ,Creating the heatmap
plt.figure(figsize = (8,6))
sb.heatmap(df.isnull(), cbar=False , cmap = 'magma')

#3 Dropping Missing Values:
 print(df.shape)
 #Dropping the missing rows.
 df_dropped = df.dropna(how = 'any')
 print(df_dropped.shape)
 df_dropped.to_csv('df_dropped.csv', encoding='utf-8', index=False)

#4 Replacing Missing values
   --Creating a copy of dataframe
	 df_new = df 
	 df_new['Metascore'] = df_new['Metascore'].fillna((df_new['Metascore'].mean()))
 
    --printing the dataframes after replacing null values
	print(df_new.isna().sum())
	print(df.isna().sum())
	df_new.to_csv('df_new.csv', encoding='utf-8', index=False)

#5 Dealing with Outliers
  -Z-score
  -Scatter Plots
  -Interquartile range(IQR)
   
   #Z-score  filtering outliers
   --column on which this method is applied should be a numerical variable and not categorical.
  df_new = df[(np.abs(stats.zscore(df.Votes)) < 3)]
  print(df_new.isna().sum())
  
  #Quantiles
 -- By this method values falling below 0.01 & above 0.99 quantiles in series will filtered out.
   #Selecting limits
	q_low = df["Votes"].quantile(0.01)
	q_hi  = df["Votes"].quantile(0.99)
 
	#filtering outliers
	df_filtered = df[(df["Votes"] < q_hi) & (df["Votes"] > q_low)]
	print(df_filtered.isna().sum())

#6  Duplicate entries
    df1 = df._append(df.iloc[20:30,:])
    df1.duplicated().sum()
	--dropping the duplicates
    df1 = df1.drop_duplicates()
