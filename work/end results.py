import pandas as pd

df=pd.read_csv('/Users/abdulrahmanhenedy/PycharmProjects/links/Files/semrush.csv')
dff=pd.read_csv('/work/gsc_agg.csv')
dfff=pd.read_csv('/Users/abdulrahmanhenedy/PycharmProjects/links/Files/inlinks_final.csv')

dff = dff.rename(columns={'page': 'Source url'})
dfff = dff.rename(columns={'links_url': 'Source url'})

merged_df = pd.merge(left=df, right=dff, on='Source url', how='inner')
output = pd.merge(left=merged_df, right=dfff, on='Source url', how='inner')

output.to_csv('final_output.csv')