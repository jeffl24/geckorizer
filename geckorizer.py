# # import firebase_admin
# # from firebase_admin import credentials
# # from firebase_admin import db
# #
# # # Fetch the service account key JSON file contents
# # cred = credentials.Certificate('.\geckorizer.json')
# #
# # # Initialize the app with a service account, granting admin privileges
# # firebase_admin.initialize_app(cred, {
# #     'geckorizer': 'https://geckorizer.firebaseio.com'
# # })
# #
# # # db.collection(u'snapshot').order_by(u'timestamp').limit(1).get()
# #
# # ss = db.collection(u'snapshot')
# # query = ss.limit(3)
# # results = query.get()
# #
# # print(db)
# from google.cloud import firestore
#
# # Add a new document
# db = firestore.Client.from_service_account_json('geckorizer.json')
# doc_ref = db.collection(u'snapshot')
#
# print(doc_ref.to_dict())
#
# # # Then query for documents
# # users_ref = db.collection(u'users')
# # docs = users_ref.get()
# #
# # for doc in docs:
# #     print(u'{} => {}'.format(doc.id, doc.to_dict()))

import firebase_admin
import json
from pprint import pprint
import pandas as pd
from pandas.io.json import json_normalize
from firebase_admin import credentials
from firebase_admin import firestore

# Fetch the service account key JSON file contents
cred = credentials.Certificate('./geckorizer.json')

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred)

db = firestore.client()

# retrieve the contents of a single document using get() method
users_ref = db.collection(u'snapshot')
# with user count limit use: docs = discover_users_ref.limit(1).get()
docs = users_ref.order_by(
    u'timestamp',
    direction=firestore.Query.DESCENDING).limit(3).get()

print(u'Document Data: {}'.format(docs.to_dict()))
# json_data = json.load(docs, encoding='UTF-8')
# pprint(json_data)
# json_df = pd.read_json(docs, orient='columns')
# print(json_df.head(10))
# print(json_df.head())
'''f = open("text.txt", "w")
for doc in docs:
    f.write(doc)
    # print(u'{} => {}'.format(doc.id, doc.to_dict()), "\n")
f.close()
'''
