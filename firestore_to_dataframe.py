
import pandas as pd
import numpy as np
import json
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
cred = credentials.Certificate('D:\Code\geckorizer\geckorizer.json')
firebase_admin.initialize_app(cred)

db = firestore.client()
users_ref = db.collection(u'snapshot')

docs = users_ref.order_by(
    u'timestamp',
    direction=firestore.Query.DESCENDING).limit(3).get()

json_list = []
for doc in docs:
    json_list.append(doc.to_dict())

print(json_list)

print('Each \'json_list\' element contains:', json_list[0].keys())
print('Each \'json_list[\'timestamp\'] element contains the timestamp integer:',
      json_list[0]['timestamp'])
print('Each \'json_list[element][\'stock\'][element] entry contains a list of JSON entries: \n',
      json_list[1]['stock'][0].keys())


# The last element 'sku' is housed in another key 'separate' from 'location' key, and will not be 'json_normalized' together with the 'location' key when
# 'pd.io.json.json_normalize(... , record_path='location')'
# is called.
# Thus, we need to append the sku number into each 'location' entry.

df_from_json = pd.DataFrame()
for json_list_element in json_list:
    for stock_element in json_list_element['stock']:
        for location_element in stock_element['location']:
            location_element.update({'sku': stock_element['sku']})

    # now that the SKU number has been appended to each element in 'location'
    # break down the json table into pandas dataframe using json_normalize
    top_normalize = pd.io.json.json_normalize(json_list_element['stock'],
                                              record_path='location',
                                              # meta='location',
                                              errors='ignore')
    top_normalize['timestamp'] = pd.to_datetime(json_list_element['timestamp'], unit='s')
    df_from_json = df_from_json.append(top_normalize)

print(df_from_json.head(10))
