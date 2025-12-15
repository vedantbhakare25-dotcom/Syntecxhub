import pandas as pd


df=pd.read_csv("data.csv")

print("First 5 rows", df.head())
print("\nLast 5 rows", df.tail())
print("\nData Types", df.dtypes)
print("\nDataset Info:")
df.info()

print("\nMean", df.mean(numeric_only=True))
print("\nMedian", df.median(numeric_only=True))
print("\nMinimum values", df.min(numeric_only=True))
print("\nMaximum values", df.max(numeric_only=True))
print("\nCount", df.count())

filtered_df=df[df["Age"] > 25]

selected_df=filtered_df[["Name", "Age", "Salary"]]

subset_df=selected_df.iloc[0:10]

subset_df.to_csv("filtered_data.csv", index=False)
subset_df.to_excel("filtered_data.xlsx", index=False)

print("\nFiltered data saved successfully!")
