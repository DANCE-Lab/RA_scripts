# %%
### Script to pull out necessary columns for D2D report
import pandas as pd
import numpy as np
# %%
#read in CSV with D2D 2024 State Fair Data
state_fair = pd.read_csv('/Users//Desktop/cleaned_D2DKidBrainPowerStud_DATA_2024-09-03.csv')
#select columns needed for initial D2D report
relevant_columns = ['pt_id', 'participant_information_form_timestamp', 'demo_child_age', 'demo_sex', 'demo_race___1', 'demo_race___2',
                     'demo_race___3', 'demo_race___4', 'demo_race___5', 'demo_race___6', 'demo_race___7', 'demo_prnt_age', 
                    'demo_collateral_gender', 'demo_prnt_ed', 'demo_current_zipcode']
#create DF containing only needed columns
state_fair_short = state_fair[relevant_columns]
#rename columns in DF to make them easier to understand
state_fair_short = state_fair_short.rename(columns = {'pt_id': 'UMN_ID', 'participant_information_form_timestamp': 'timestamp', 
                                                      'demo_child_age': 'participant_age', 'demo_sex': 'participant_sex', 'demo_race___1': 'american_indian', 
                                                      'demo_race___2': 'asian', 'demo_race___3': 'black', 'demo_race___4': 'hispanic', 
                                                      'demo_race___5': 'middle_eastern', 'demo_race___6': 'pacific_islander', 'demo_race___7': 'white', 
                                                      'demo_prnt_age': 'parent_age', 'demo_collateral_gender': 'parent_gender', 'demo_prnt_ed': 'parent_education', 
                                                      'demo_current_zipcode': 'participant_current_zipcode'})
#Replace numeric values with words where relevant to make csv understandable
state_fair_short.loc[state_fair_short['participant_sex'] == 1, ['participant_sex']] = 'male'
state_fair_short.loc[state_fair_short['participant_sex'] == 2, ['participant_sex']] = 'female'
state_fair_short.loc[state_fair_short['parent_gender'] == '1', ['parent_gender']] = 'agender'
state_fair_short.loc[state_fair_short['parent_gender'] == '4', ['parent_gender']] = 'cis_woman'
state_fair_short.loc[state_fair_short['parent_gender'] == '2', ['parent_gender']] = 'cis_man'
state_fair_short.loc[state_fair_short['parent_gender'] == '8', ['parent_gender']] = 'identity_not_listed'
state_fair_short.loc[state_fair_short['parent_education'] == 1, ['parent_education']] = 'never_attended'
state_fair_short.loc[state_fair_short['parent_education'] == 2, ['parent_education']] = 'grad_high_school'
state_fair_short.loc[state_fair_short['parent_education'] == 3, ['parent_education']] = 'GED_equiv'
state_fair_short.loc[state_fair_short['parent_education'] == 4, ['parent_education']] = 'some_college'
state_fair_short.loc[state_fair_short['parent_education'] == 5, ['parent_education']] = 'Occupational_Assoociates'
state_fair_short.loc[state_fair_short['parent_education'] == 6, ['parent_education']] = 'Academic_Associates'
state_fair_short.loc[state_fair_short['parent_education'] == 7, ['parent_education']] = 'Bachelor'
state_fair_short.loc[state_fair_short['parent_education'] == 8, ['parent_education']] = 'Master'
state_fair_short.loc[state_fair_short['parent_education'] == 9, ['parent_education']] = 'Doctorate'
#export csv
state_fair_short.to_csv('/Users//Desktop/2024_kid_brain_power_raw_demographics.csv')
# %%
