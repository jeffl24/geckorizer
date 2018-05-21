
# coding: utf-8

# In[1]:

import requests
import json
import numpy as np
import pandas as pd
import pprint
import math
import datetime
pd.options.display.max_columns = 999


# In[2]:

url = 'https://api.tradegecko.com/variants'
bearer = {'Authorization': 'Bearer f4855aebc4a92c0d6a09f07b105bcbae81afbaf8cb1344f47a5b5c45cf8f4c1e'}

# convert data to json format
variants_request = requests.get(url, headers=bearer).text
variants_json = json.loads(variants_request)

# create counter to loop across different pages
total_items = variants_json['meta']['total']
items_per_page = 250
loop_count = math.ceil(total_items / items_per_page)


# loop the counter to create customized links to download all pages of inventory data
variants_df_all = pd.DataFrame()
for loop in range(loop_count):
    url_pattern = 'https://api.tradegecko.com/variants?limit={}&page={}'.format(items_per_page, loop+1)
    variants_request = requests.get(url_pattern, headers=bearer).text
    variants_json = json.loads(variants_request)
    variants_df = pd.io.json.json_normalize(variants_json, record_path='variants')
    variants_df_all = variants_df_all.append(variants_df)
    
# split the dict columns into individual columns, 
# and then apply pd.concat to create a full dataframe
committed_stock_level_cols = variants_df_all['committed_stock_levels'].apply(pd.Series).rename({81481: "HQ Committed",
                                                                                            87144: "WH Committed",
                                                                                            87350: "BC Commmitted",
                                                                                            87351: "FP Committed"})
prices_cols = variants_df_all['prices'].apply(pd.Series)
stock_level_cols = variants_df_all['stock_levels'].apply(pd.Series).rename({81481: "HQ Committed",
                                                                                            87144: "WH On Hand",
                                                                                            87350: "BC On Hand",
                                                                                            87351: "FP On Hand"})

# pd.concat([variants_df, committed_stock_level_cols, prices_cols, stock_level_cols], axis = 1)

df_others = pd.concat([variants_df_all, prices_cols], axis=1)

df_locations = pd.DataFrame()
for row in range(len(variants_df_all['locations'])):
    x = pd.DataFrame(variants_df_all['locations'].iloc[row])
    x['sku'] = variants_df_all['sku'].iloc[row]
    df_locations = df_locations.append(x)

df_locations['location_id'] = df_locations['location_id'].map({81481: "HQ",
                     87144: "WH",
                     87350: "BC",
                     87351: "FP"})


df_final = pd.merge(df_locations, df_others, on='sku').drop(['buy_price','committed_stock','stock_on_hand_y','incoming_stock','committed_stock_levels', 'locations', 'prices', 'stock_levels', 'variant_prices'], axis = 1)

# export file to csv
df_final.to_csv('inventory_api_{}.csv'.format(str(datetime.datetime.now()).replace(':', '-')))

