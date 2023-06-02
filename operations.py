import pandas as pd

# you should get the file "innerlinks.csv" from the notebook mentioned in the Readme.md, which contanis the raw inforamtion about internal links; from page A => to Page B
inlinks=pd.read_csv('/Users/abdulrahmanhenedy/PycharmProjects/links/Files/innerlinks.csv')

# Rename column names in the 'inlinks' DataFrame
inlinks = inlinks.rename(columns={'url': 'Source', 'links_url': 'Target'})

# Select specific columns in the 'inlinks' DataFrame
cols=['Source', 'Target']
inlinks = inlinks[cols]

# Save the 'inlinks' DataFrame to a CSV file named 'gephi.csv'
inlinks.to_csv('gephi.csv')

# Count the number of occurrences of each unique URL in the 'links_url' column of 'inlinks' DataFrame
innerlinks = inlinks['links_url'].value_counts()

# Save the 'innerlinks' Series to a CSV file named 'inlinks_final.csv'
innerlinks.to_csv('inlinks_final.csv')
