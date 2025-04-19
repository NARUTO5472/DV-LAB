import pandas as pd

# Load the dataset (replace 'Cereals.csv' with the correct path)
df = pd.read_csv("Cereals.csv")

# Display first few rows
print(df.head())
summary_before = df.describe().T[['min', '25%', '50%', '75%', 'max']]
print("5-Number Summary Before Handling Missing Data:")
print(summary_before)
# Identify numeric columns (assuming 'proteins' to 'vitamins' are the relevant columns)
numeric_cols = df.loc[:, 'proteins':'vitamins'].columns

# Replace -1 values with mean of respective column
for col in numeric_cols:
    mean_value = df[df[col] != -1][col].mean()  # Exclude -1 while calculating mean
    df[col] = df[col].replace(-1, mean_value)

print("Missing values replaced with mean.")
summary_after_missing = df.describe().T[['min', '25%', '50%', '75%', 'max']]
print("5-Number Summary After Handling Missing Data:")
print(summary_after_missing)
for col in numeric_cols:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1

    # Define outlier thresholds
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    # Replace outliers with median
    median_value = df[col].median()
    df.loc[(df[col] < lower_bound) | (df[col] > upper_bound), col] = median_value

print("Noisy values replaced with median.")
summary_after_noisy = df.describe().T[['min', '25%', '50%', '75%', 'max']]
print("5-Number Summary After Handling Noisy Data:")
print(summary_after_noisy)
