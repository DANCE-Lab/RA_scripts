#This script deidentifies data collected at the 2024 Minnesota State Fair (D2D data)

# %%
#Import libraries
import numpy as np
import pandas as pd

# %%
#Import data
self_r = pd.read_csv('.../cleaned_d2d_state_fair_2024.csv')

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
#Move PID to first column
col = self_r.pop('PID')
self_r.insert(0, 'PID', col)
# %%
#Drop Unnamed: 0
d2d = self_r
#Drop identifiers and consent columns 
id_cols = ['participant_information_form_timestamp', 'consent_version', 'irb_number', 'irb_date', 
           'pt_first_name', 'pt_last_name', 'pt_email', 'who_sign', 'in_person_consent', 'participant_information_form_complete', 
           'consent_form_timestamp', 'child_name', 'parent_name', 'sig_parent', 'parent_date', 'sig_worker', 'worker_name', 
           'worker_date', 'demo_birthday', 'demo_current_street', 'street_1', 'street_2', 'street_3', 'city_1', 'city_2', 'city_3',
            'state_1', 'state_2', 'state_3', 'zipcode_1', 'zipcode_2', 'zipcode_3', 'email_box']
id_df_cols = ['PID', 'record_id', 'participant_information_form_timestamp', 'consent_version', 'irb_number', 'irb_date', 
           'pt_first_name', 'pt_last_name',  'pt_email', 'who_sign', 'in_person_consent', 'participant_information_form_complete', 
           'consent_form_timestamp', 'child_name', 'parent_name', 'sig_parent', 'parent_date', 'sig_worker', 'worker_name', 
           'worker_date', 'demo_birthday', 'demo_current_street', 'demo_current_city', 'demo_current_state', 'demo_current_zipcode',
           'street_1', 'street_2', 'street_3', 'city_1', 'city_2', 'city_3', 'state_1', 'state_2', 'state_3',
           'zipcode_1', 'zipcode_2', 'zipcode_3', 'email_box']
geocoding_cols = ['PID', 'demo_current_street', 'street_1', 'street_2', 'street_3', 'city_1', 'city_2', 'city_3',
            'state_1', 'state_2', 'state_3', 'zipcode_1', 'zipcode_2', 'zipcode_3']
birthday = ['PID', 'participant_information_form_timestamp', 'demo_birthday']
# %%
#Create df without identifiers
d2d_deid = d2d.drop(columns=id_cols)

#Create identifier df
d2d_id_df = d2d[id_df_cols]
d2d_id_df.head()

#create geocoding df
geo = d2d[geocoding_cols]

#create birthday df for calculating exact age
bday = d2d[birthday]
# %%
#Export deidentified data
d2d_deid.to_csv('.../d2d_deidentified_self_report_data.csv', index=False)

#Export identifier data
d2d_id_df.to_csv('.../d2d_identifiers.csv', index=False)

#Export geocoding data
geo.to_csv('.../d2d_geocoding.csv', index=False)

#Export birthday data
bday.to_csv('.../d2d_birthday.csv', index=False)
# %%
#Isolate columns in the Multidimensional Neighborhood Perceived Opportunity Scale
d2d_cols = list(d2d_deid.columns)
mnp_cols = [col for col in d2d_cols if 'mpnos' in col]
mnp_cols = ['PID', 'record_id', 'multidimensional_perceived_neighborhood_opportunit_complete'] + mnp_cols
print(mnp_cols)
#
# %%
d2d.head()
# %%
