#!/usr/bin/python
import os
credential_path = "./blossom-dev-81023-firebase-adminsdk-re866-8a7a2b534f.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use the application default credentials
cred = credentials.ApplicationDefault()
firebase_admin.initialize_app(cred, {
    'apiKey': '',
})

db = firestore.client()

#this is a valid user id you can test
#user_id = 'FOEhBhLTgpU8wAERvqlWYdUIJag2'

def get_watched_company_ids(user_id):
    results = []
    docs = db.collection(u'watchlist').where(u'uid', u'==', user_id).stream()

    for doc in docs:

        companiesId = doc.to_dict()['companies']

        for id in companiesId:
            results.append(id)
            
    return results

print(get_watched_company_ids(u'FOEhBhLTgpU8wAERvqlWYdUIJag2'))

