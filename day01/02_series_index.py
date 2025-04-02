# %%
import pandas as pd

# %% List of names representing my cats
names = [
    "Tapioca",
    "Marceline",
    "Frida",
    "Bambu",
    "Jennie",
    "Stacy",
    "Frodo",
    "Naniquinha",
    "Mon Cherri",
]

# %% List of ages corresponding to the names above
ages = [3, 1, 8, 9, 3, 1, 8, 2, 1]

# %% Creating a Pandas Series with ages as values and names as indices
series_ages = pd.Series(ages, index=names)

# %% Sorting the Series by values (ages)
# Note: The indices (names) remain associated with their respective values after sorting
series_ages = (
    series_ages.sort_values()
)  # The indices remain the same even after sorting
series_ages

# ACCESSING ELEMENTS IN A LIST

# %% Accessing the first element of the ages list
ages[0]

# %% Accessing the first element of the Series using iloc
series_ages.iloc[
    0
]  # Ignores the index keys and returns the position. Searching in rows

# %% Retrieving the first three elements of the Series using iloc
series_ages.iloc[:3]

# %% Accessing an element in the Series by its index (name)
series_ages["Tapioca"]
