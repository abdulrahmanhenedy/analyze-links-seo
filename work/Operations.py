import pandas as pd

df=pd.read_csv('/Users/abdulrahmanhenedy/PycharmProjects/links/Files/innerlinks.csv')

df = df.rename(columns={'url': 'Source', 'links_url': 'Target'})

cols=['Source', 'Target']
df=df[cols]
df.to_csv('gephi.csv')

inlinks=df['links_url'].value_counts()

inlinks.to_csv('inlinks_final.csv')