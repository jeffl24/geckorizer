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
<<<<<<< HEAD
    direction=firestore.Query.DESCENDING).limit(1).get()

json_dict = dict()
# for doc in docs:
#     preview1 = pd.io.json.json_normalize(doc.to_dict()['stock'],
#         record_path=['location'])
#     # u'{}': '{}'.format(doc.id, doc.to_dict()))
#     preview2 = pd.io.json.json_normalize(doc.to_dict()['timestamp'])
#     print(preview2)
=======
    direction=firestore.Query.DESCENDING).limit(3).get()
>>>>>>> origin/master

print(u'Document Data: {}'.format(docs.to_dict()))
# json_data = json.load(docs, encoding='UTF-8')
# pprint(json_data)
# json_df = pd.read_json(docs, orient='columns')
# print(json_df.head(10))
# print(json_df.head())
'''f = open("text.txt", "w")
for doc in docs:
<<<<<<< HEAD
    print(u'{}, {}'.format(doc.id, doc.to_dict()))
# json_df = pd.io.json.json_normalize(json_dict)
# print(json_df)
    # data = json.loads(doc.to_dict())
    # data_new = json_normalize(data['stock'])

# json_df = []
# for entry in json_list:
#     json_df = json.loads(entry)

# pew = json.loads(json_list[0])
# print(pew)

# with open('data.json', 'w') as fp:
#     for doc in docs:
#         entry = json.dump(doc.to_dict(), fp)
#         json_list.append(entry)
# print(json_list)
=======
    f.write(doc)
    # print(u'{} => {}'.format(doc.id, doc.to_dict()), "\n")
f.close()
'''
>>>>>>> origin/master
