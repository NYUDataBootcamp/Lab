# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 11:50:26 2016

@author: sglyon
"""
#%% read data
import pandas as pd

url1 = "https://raw.githubusercontent.com/NYUDataBootcamp/"
url2 = "Materials/master/Data/fall16_ug_pace_raw.csv"
url = url1 + url2
df = pd.read_csv(url)

#%% rename columns
df.columns = ["time", "experience", "pace", "help"]

#%% clean up dates
df["time"] = pd.to_datetime(df["time"])

#%% make experience column 0, 1 indicator
exp = df["experience"].copy()
exp[exp == "No"] = 0
exp[exp == "Yes"] = 1
df["experience"] = exp.astype(float)

#%% Make pace column 0, 1, 2, categorical
df["pace"] = df["pace"].astype("category")

#%% Split multiple response column

# get list of all topics people wanted help with
help_str = df["help"].str
help_list = help_str.split(r";").tolist()
topics = set()
for response in help_list:
    if type(response) == list:
        for topic in response:
            topics.add(topic.strip())
new_names = {'Conditionals (if/else) and comparisons (<, >, ==, etc.) -- from python fundamentals 2': 'conditionals',
'DataFrame properties and methods  -- from Pandas 1: Data input': 'dataframe_methods',
'Defining our own functions -- from python fundamentals 2': 'functions',
'Dictionaries -- from python fundamentals 2': 'dictionaries',
'Importing packages -- from Pandas 1: Data input': 'importing',
'List comprehensions (for inside square brackets) -- from python fundamentals 2': 'list_comprehensions',
'Loops (for) --- from python fundamentals 2': 'loops',
'Objects and methods -- from python fundamentals 1': 'objects',
'Reading data from internet -- from Pandas 1: Data input': 'internet_data',
'Slicing (square brackets) -- from python fundamentals 2': 'slicing',
'Working with variables in DataFrames  -- from Pandas 1: Data input': 'df_variables'}

# make one column per topic, and add 0 or 1 for each response
for topic in topics:
    # keep only first word
    colname = new_names[topic]
    df[colname] = 0
    has_topic = help_str.contains(topic, regex=False)
    df.loc[has_topic.fillna(False), colname] = 1
    
#%% drop old help column
df.drop(["help"], axis=1, inplace=True)

