import pandas as pd
from textblob import TextBlob

# Read in HW2 files as pandas DFs
raw_df1 = pd.read_csv('output.csv')
raw_df2 = pd.read_csv('50companyData.csv')

# Removing Unnamed first column
raw_df2 = raw_df2[['Name', 'Purpose']]

# Combining Data Frames into single DF
comb_df = pd.concat([raw_df1, raw_df2], axis=0)

# Delete Raw DFs
del raw_df1
del raw_df2

# Testing textblob
test = 'This is terrible'
blob = TextBlob(test)
print(blob.sentiment)






