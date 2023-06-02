import pandas as pd

# the SEMrush's file from Backlinks => Indexed pages => download as csv 
backlinks=pd.read_csv('/Users/abdulrahmanhenedy/PycharmProjects/links/Files/bookonboard - backlinks.csv')

# this is a GSC data and it preferably should be have aggreagate numbers like total click and impressions for each URL 
gsc=pd.read_csv('/work/gsc_agg.csv') #Optional

# the file we just got from the operations.py 
inlinks=pd.read_csv('/Users/abdulrahmanhenedy/PycharmProjects/links/Files/inlinks_final.csv')

# Rename columns in the 'gsc' and 'inlinks' DataFrames
gsc = gsc.rename(columns={'page': 'Source url'})
inlinks = inlinks.rename(columns={'links_url': 'Source url'})

# Merge the 'backlinks', 'gsc', and 'inlinks' DataFrames based on the 'Source url' column, using an inner join
merged_df = pd.merge(left=backlinks, right=gsc, on='Source url', how='inner')

# Merge the 'merged_df' DataFrame with the 'inlinks' DataFrame based on the 'Source url' column, using an inner join
output = pd.merge(left=merged_df, right=inlinks, on='Source url', how='inner')

# Save the final merged DataFrame as a CSV file named 'final_output.csv'
output.to_csv('final_output.csv')
