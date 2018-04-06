import pandas as pd
import numpy as np
import json
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
pd.options.display.max_columns = 999

cred = credentials.Certificate('D:\Code\geckorizer\geckorizer.json')
firebase_admin.initialize_app(cred ) #, {'databaseURL': 'https://geckorizer.firebaseio.com'})
# snapshot_custom = db.reference('1518077810').get()
snapshot_client = firestore.client()
snapshot_ref = snapshot_client.collection(u'snapshot')
snapshot_get = snapshot_ref.get()

print('Getting data from firestore...')

key_series = []
for key in snapshot_get:
    key_series.append(key.to_dict())

print('Finished appending to key_series. Now converting to dataframe...')
print('Length of series: {:0}'.format(len(key_series)))
snapshot_df_all = pd.DataFrame()

# for entry in range(134):
#     snapshot_df = pd.io.json.json_normalize(key_series[entry]['stock'], record_path= 'location')
#     snapshot_df['sku'] = key_series[entry]['stock'][entry]['sku']
#     snapshot_df['timestamp'] = key_series[entry]['timestamp']
#     snapshot_df['datetime'] = pd.to_datetime(snapshot_df['timestamp'], unit= 's')
#     snapshot_df_all = snapshot_df_all.append(snapshot_df)

# snapshot_df_all.to_csv('geckorizer_snapshot.csv')

print('Finished converting to dataframe. Dataframe exported to csv.')
# Use this to loop
# pd.DataFrame.from_dict(key_series[0]['stock'])['location'][1]
