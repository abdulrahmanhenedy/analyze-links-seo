import pandas as pd

backlinks=pd.read_csv('/Users/abdulrahmanhenedy/PycharmProjects/links/Files/bookonboard - backlinks.csv')
gsc=pd.read_csv('/work/gsc_agg.csv')
inlinks=pd.read_csv('/Users/abdulrahmanhenedy/PycharmProjects/links/Files/inlinks_final.csv')

gsc = gsc.rename(columns={'page': 'Source url'})
inlinks = inlinks.rename(columns={'links_url': 'Source url'})

merged_df = pd.merge(left=backlinks, right=gsc, on='Source url', how='inner')
output = pd.merge(left=merged_df, right=inlinks, on='Source url', how='inner')

output.to_csv('final_output.csv')
