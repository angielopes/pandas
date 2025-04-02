# %% List of ages

ages = [1, 2, 3, 8, 9, 27, 35, 58, 63, 65]

# %% Working with statistics without Pandas

# Calculating the average of a list of numbers
avg = sum(ages) / len(ages)
print(f"Average: {avg}")

# Calculating the variance of a list of numbers
diffs = 0
for age in ages:
    diffs += (age - avg) ** 2

variance = diffs / (len(ages) - 1)

print(f"Variance: {variance}")

# %% Working with statistics using Pandas

import pandas as pd

series_age = pd.Series(ages)

# Average
avg_pandas = series_age.mean()
print(f"Average using Pandas: {avg_pandas}")

# Variance
variance_pandas = series_age.var()
print(f"Variance using Pandas: {variance_pandas}")

# Describe
summary_idades = series_age.describe()
print(f"Details about the data:\n{summary_idades}")
