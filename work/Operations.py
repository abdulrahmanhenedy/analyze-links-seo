import pandas as pd

inlinks=pd.read_csv('/Users/abdulrahmanhenedy/PycharmProjects/links/Files/innerlinks.csv')

inlinks = inlinks.rename(columns={'url': 'Source', 'links_url': 'Target'})

cols=['Source', 'Target']
inlinks=inlinks[cols]
inlinks.to_csv('gephi.csv')

innerlinks=inlinks['links_url'].value_counts()

innerlinks.to_csv('inlinks_final.csv')
