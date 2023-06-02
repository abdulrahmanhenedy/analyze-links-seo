# Control the Internal/External Links Flow
![Screen Shot 2023-02-02 at 5 08 50 AM](https://user-images.githubusercontent.com/114556029/216784971-8f58faf5-46c8-4dab-9466-25bb76c035d9.png)

## Step 1: Gather the data

1.Using SEMrush, go to "backlink audit" and export the report under the "Indexed pages" tab.

2.Use this template to get the internal links data (cc:@EliasDabbas): https://www.kaggle.com/code/eliasdabbas/seo-crawl-analysis-template

3.Under the "Link Analysis" section you'll fix the following code from "links_df_count_dup" to "links_df_count_dup.to_csv('innerlinks.csv')" to save the dataframe to csv and then download it.

4.We'll need GSC data but it's optional. If you need to add it, you'll have to extract the data from the API, aggregate it by URL, and cluster it into groups (I'll break this down in the next reportistry since it's a complicated topic)
## Step 2: Use the code

1.Use the "operations.py" file to get the number of internal links for each link.

2.Use the "output.py" file to merge all the dataframes together and get the following dataframe:

![Screen Shot 2023-02-02 at 3 46 54 AM](https://user-images.githubusercontent.com/114556029/216785685-ed23d5c5-dfda-4b1b-abfa-2396103bfc76.png)

## Step 3: Internal links Graph
![Screen Shot 2023-02-02 at 5 13 35 AM](https://user-images.githubusercontent.com/114556029/216786041-1e9c97dd-66ed-4af9-98a8-45a776c88bfc.png)

1.Use the file we extracted from the notebook above "innerlinks.csv" to feed it to Gephi.

2.Before that, make sure that the file has only 2 colmuns "Source, Target". The source is the columns  from which the link come from and the Target is the column from which the link points to.

3.Calculate the modularity class and PageRank in Gephi.

4.Make the colors based on the modularity class and the size of the dots based on PageRank.

I recommend reading this article to get a better sense of how to use Gephi: https://searchengineland.com/easy-visualizations-pagerank-page-groups-gephi-265716
