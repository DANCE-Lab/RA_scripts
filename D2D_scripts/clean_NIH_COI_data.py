# %%
import pandas as pd
import numpy as np
# %%
# Read the NIH and COI data
nih_df = pd.read_csv("/Users/madeleineseitz/Desktop/coi/D2D_NIHTB_ScoresExport_2024-09-05.csv")
coi_df = pd.read_csv("/Users/madeleineseitz/Desktop/coi/COI_Census_DANCE.csv")
# %%
#Restore ID numbers
# Correct self report IDs that did not translate properly
def fix_bad_ids(df):
    df['PID'] = df['PID'].astype(str)
    zero_list = []
    for row in df.index:
        if len(df['PID'][row]) < 5:
            zero_list.append(df['PID'][row])
    print(zero_list)
    df.loc[df['PID'] == '7443', ['PID']] = '07443'
    df.loc[df['PID'] == '6386', ['PID']] = '06386'
    df.loc[df['PID'] == '6786', ['PID']] = '06786'
    df.loc[df['PID'] == '9759', ['PID']] = '09759'
    df.loc[df['PID'] == '5383', ['PID']] = '05383'
    df.loc[df['PID'] == '9570', ['PID']] = '09570'
    df.loc[df['PID'] == '584', ['PID']] = '00584'
    df.loc[df['PID'] == '6272', ['PID']] = '06272'
    df.loc[df['PID'] == '1180', ['PID']] = '01180'
    df.loc[df['PID'] == '744', ['PID']] = '00744'
    return df
# %%
#fix incorrect ids in both dfs
nih_df = fix_bad_ids(nih_df)
coi_df = fix_bad_ids(coi_df)
nih_df.loc[nih_df['PID'] == '333028', ['PID']] = '33028'
# %%
#generate a list of nih columns
list(nih_df)
# %%
#drop columns that contain only NaN values
nih_df = nih_df.dropna(axis=1, how='all')
coi_df = coi_df.dropna(axis=1, how='all')
# %%
#generate a list of coi columns
list(coi_df)
#isolate columns containing address information
address_cols = [ 'Match Address',
 'Long Label',
 'Short Label',
 'Place Address',
 'Street Address',
 'Neighborhood',
 'City',
 'Subregion',
 'Region',
 'Region Abbreviation',
 'Postal',
 'Postal Extension',
 'Country',
 'Country Name',
'demo_current_street',
 'demo_current_city',
 'demo_current_state',
 'demo_current_zipcode',
 'street_1',
 'street_2',
 'city_1',
 'city_2',
 'city_3',
 'state_1',
 'state_2',
 'zipcode_1',
 'zipcode_2',
 'ObjectID.1']
coi_df = coi_df.drop(columns=address_cols, axis=1)
# %%
#Move PID to first column
col = coi_df.pop('PID')
coi_df.insert(0, 'PID', col)
# %%
coi_df.to_csv("/Users/madeleineseitz/Desktop/coi/COI_Census_DANCE_clean.csv", index=False)
nih_df.to_csv("/Users/madeleineseitz/Desktop/coi/D2D_NIHTB_ScoresExport_2024-09-05_clean.csv", index=False)
# %%
