# %%
import numpy as np
import pandas as pd

# %%
# Read in state fair data
df = pd.read_csv('/Users/madeleineseitz/Desktop/cleaned_D2DKidBrainPowerStud_DATA_2024-09-03.csv')
# %%
state_fair_clean = df
# %%
# Create a function to map new values (contained in a dictionary) to the existing column. These will match the cleaned REDCap codebook
def update_value(dataframe, col, dic): 
    for key in dic:
        dataframe.loc[dataframe[col] == key, col] = dic[key]
    return dataframe
# %%
#create dictionaries for mapping values
#dictionary name corresponds to column name
demo_child_age = {9: 10, 8: 9, 7: 8, 6: 7, 5: 6, 4: 5, 3: 4, 2: 3, 1: 2, 0: 1}
demo_household = {9: 10, 8: 9, 7: 8, 6: 7, 5: 6, 4: 5, 3: 4, 2: 3, 1: 2, 0: 1}
demo_moved_times = {2: 3, 1: 2, 0: 1}
sefq_1 = {6: 7, 5: 6, 4: 5, 3: 4, 2: 3, 1: 2, 0: 1}
sefq_2 = {6: 7, 5: 6, 4: 5, 3: 4, 2: 3, 1: 2, 0: 1}
sefq_3 = {6: 7, 5: 6, 4: 5, 3: 4, 2: 3, 1: 2, 0: 1}
sefq_4 = {6: 7, 5: 6, 4: 5, 3: 4, 2: 3, 1: 2, 0: 1}
sefq_5 = {6: 7, 5: 6, 4: 5, 3: 4, 2: 3, 1: 2, 0: 1}
sefq_6 = {6: 7, 5: 6, 4: 5, 3: 4, 2: 3, 1: 2, 0: 1}
sefq_7 = {6: 7, 5: 6, 4: 5, 3: 4, 2: 3, 1: 2, 0: 1}
sefq_8 = {6: 7, 5: 6, 4: 5, 3: 4, 2: 3, 1: 2, 0: 1}
sefq_9 = {6: 7, 5: 6, 4: 5, 3: 4, 2: 3, 1: 2, 0: 1}
sefq_10 = {6: 7, 5: 6, 4: 5, 3: 4, 2: 3, 1: 2, 0: 1}
sefq_11 = {6: 7, 5: 6, 4: 5, 3: 4, 2: 3, 1: 2, 0: 1}
sefq_12 = {6: 7, 5: 6, 4: 5, 3: 4, 2: 3, 1: 2, 0: 1}
sefq_13 = {6: 7, 5: 6, 4: 5, 3: 4, 2: 3, 1: 2, 0: 1}
sefq_14 = {6: 7, 5: 6, 4: 5, 3: 4, 2: 3, 1: 2, 0: 1}

#Create dictionary with corresponding column and dictionary names
cols_dict = {
    'demo_child_age': demo_child_age,
    'demo_household': demo_household,
    'demo_moved_times': demo_moved_times,
    'sefq_1': sefq_1,
    'sefq_2': sefq_2,
    'sefq_3': sefq_3,
    'sefq_4': sefq_4,
    'sefq_5': sefq_5,
    'sefq_6': sefq_6,
    'sefq_7': sefq_7,
    'sefq_8': sefq_8,
    'sefq_9': sefq_9,
    'sefq_10': sefq_10,
    'sefq_11': sefq_11,
    'sefq_12': sefq_12,
    'sefq_13': sefq_13,
    'sefq_14': sefq_14
}

# %%
# Update mismatched values in dataframe
for key in cols_dict:
    state_fair_clean = update_value(state_fair_clean, key, cols_dict[key])
# %%
state_fair_clean[10:20]
# %%
#Perform sanity checks
#Compare value frequencies in sefq_10
df['sefq_10'].value_counts()
state_fair_clean['sefq_10'].value_counts()
# %%
#Compare  value frequencies in demo_moved_times
df['demo_moved_times'].value_counts()
state_fair_clean['demo_moved_times'].value_counts()
# %%
#compare value frequencies in demo_child_age
df['demo_child_age'].value_counts()
state_fair_clean['demo_child_age'].value_counts()
# %%
""" 
Frequency of values shows that values have successfully been updated
"""
# %%
# Save updated df as csv
state_fair_clean.to_csv('/Users/madeleineseitz/Desktop/cleaned_d2d_state_fair_2024.csv')
# %%
