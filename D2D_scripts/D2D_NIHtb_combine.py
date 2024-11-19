""" 
Script to combine NIH toolbox data from 2024 Minnesota State Fair outreach self-report data
Correct ids, drop columns containing only NaN values
"""
# %%
# import libraries 
import numpy as np
import pandas as pd

# %%
# import NIH toolbox and self-report data

self_r = pd.read_csv('/Users/madeleineseitz/Desktop/cleaned_d2d_state_fair_2024.csv')
nihtb = pd.read_csv('/Users/madeleineseitz/Desktop/D2D_NIHTB_ScoresExport_2024-09-05.csv')
# %% 
self_r.head()
# %%
# Correct nihtb IDs that did not translate properly
nihtb['PID'] = nihtb['PID'].astype(str)
zero_list = []
for row in nihtb.index:
    if len(nihtb['PID'][row]) < 5:
        zero_list.append(nihtb['PID'][row])
print(zero_list)

# %%
# Correct Ids
nihtb.loc[nihtb['PID'] == '584', ['PID']] = '00584'
nihtb.loc[nihtb['PID'] == '1180', ['PID']] = '01180'
nihtb.loc[nihtb['PID'] == '5383', ['PID']] = '05383'
nihtb.loc[nihtb['PID'] == '6272', ['PID']] = '06272'
nihtb.loc[nihtb['PID'] == '7443', ['PID']] = '07443'
nihtb.loc[nihtb['PID'] == '9570', ['PID']] = '09570'
nihtb.head()
# %%
#identify columns that contain only NaN values
all_nans = nihtb.columns[nihtb.isna().all()].tolist()
print(all_nans)
#remove columns that contain only nan values
nihtb_short = nihtb
nihtb_short = nihtb_short.drop(columns= all_nans)
nihtb_short.head()
# %%
# Correct self report IDs that did not translate properly
self_r['pt_id'] = self_r['pt_id'].astype(str)
zero_list = []
for row in self_r.index:
    if len(self_r['pt_id'][row]) < 5:
        zero_list.append(self_r['pt_id'][row])
print(zero_list)
# %%
# Correct ids
self_r.loc[self_r['pt_id'] == '7443', ['pt_id']] = '07443'
self_r.loc[self_r['pt_id'] == '6386', ['pt_id']] = '06386'
self_r.loc[self_r['pt_id'] == '6786', ['pt_id']] = '06786'
self_r.loc[self_r['pt_id'] == '9759', ['pt_id']] = '09759'
self_r.loc[self_r['pt_id'] == '5383', ['pt_id']] = '05383'
self_r.loc[self_r['pt_id'] == '9570', ['pt_id']] = '09570'
self_r.loc[self_r['pt_id'] == '584', ['pt_id']] = '00584'
self_r.loc[self_r['pt_id'] == '6272', ['pt_id']] = '06272'
self_r.loc[self_r['pt_id'] == '1180', ['pt_id']] = '01180'
self_r.loc[self_r['pt_id'] == '744', ['pt_id']] = '00744'

# %%
#identify columns that contain only NaN values in self-reports
self_nans = self_r.columns[self_r.isna().all()].tolist()
print(self_nans)
# %%
#Drop irrelevant columns containing only NaNs
self_r = self_r.drop(columns= ['Unnamed: 0', 'redcap_survey_identifier', 'send_form', 'login_code'])
# %%
#rename self_r participant id
self_r = self_r.rename(columns= {'pt_id': 'PID'})
# %%
#merge dfs into single df
combined = pd.merge(self_r, nihtb, on= 'PID', how= 'outer')
combined.head()
# %%
# Move PID to first column, and NIH toolbox report requested and participant notes to the end
col = combined.pop('PID')
combined.insert(0, 'PID', col)
report = combined.pop('NIH_toolbox_report_requested')
combined['NIH_toolbox_report_requested'] = report
notes = combined.pop('Participant_Notes')
combined['Participant_Notes'] = notes
combined.head()

# %%
# Save dataframe 
combined.to_csv('/Users/madeleineseitz/Desktop/D2D_self_reports_nihtb_2024.csv')
# %%
