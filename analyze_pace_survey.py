# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 13:44:15 2016

@author: sglyon
"""

#%% Reading data from the internet
import pandas as pd
url1 = "https://raw.githubusercontent.com/NYUDataBootcamp/"
url2 = "Materials/master/Data/fall16_ug_pace.csv"
url = url1 + url2
df = pd.read_csv(url, index_col=0)

#%% Dataframe properties
print("The columns in this dataframe are:")
print(df.columns.tolist())

#%%
print("The size of this DataFrame is (# rows, # columns)")
print(df.shape)

# save number of rows and columns
n_response, n_columns = df.shape

#%% Accesing a variable
# get pace variable, save it as a new variable
pace = df["pace"]

# get all variables for subjects
subject_cols = list(range(3, n_columns))
subjects = df[subject_cols]

#%% DataFrame methods

# number of people who requested a review of each topic
subjects.sum()

# bar plot of the sum
subject_totals = subjects.sum()
subject_totals.plot(kind="barh")

#%% loops
# Iterate over all responses
for i in range(n_response):
    print("This is response", i)

    # Iterate over all questions
    print("Person", i, "asked to cover")
    for question in df.columns:
        if question in subjects:
            if df[question][i] == True:
                print("  ", question)
    
#%% 