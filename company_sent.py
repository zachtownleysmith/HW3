import pandas as pd
from textblob import TextBlob
pd.set_option("display.max_rows", 100, "display.max_columns", 4, "display.max_colwidth", 200)

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

# Compute the TextBlob Sentiment and append result to Data Frame
comb_df['Polarity'] = [TextBlob(purpose).sentiment.polarity for purpose in comb_df['Purpose']]
comb_df['Subjectivity'] = [TextBlob(purpose).sentiment.subjectivity for purpose in comb_df['Purpose']]

# Sort Data Frame by Sentiment (Polarity then Subjectivity)
comb_df = comb_df.sort_values(by=['Polarity', 'Subjectivity'])
comb_df.reset_index(drop=True, inplace=True)

if __name__ == '__main__':
    # Report 10 companies with highest sentiment
    print("10 Company Purposes With Highest TextBlob Sentiment:")
    print(comb_df.tail(10))
    print("")

    # Report 10 companies with lowest sentiment
    print("10 Company Purposes With Lowest TextBlob Sentiment:")
    print(comb_df.head(10))




