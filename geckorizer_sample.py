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
from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account
cred = credentials.Certificate('./geckorizer.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

users_ref = db.collection(u'snapshot')
docs = users_ref.limit(1).get()

for doc in docs:
    print(u'{} => {}'.format(doc.id, doc.to_dict()))
