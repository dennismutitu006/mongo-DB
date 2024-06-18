"""
when you have an application that occasionally uses a MongoDB database. In this case, you might want to open the connection when needed and close it immediately after use for freeing the acquired resources. A consistent approach to this problem would be to use the with statement. Yes, MongoClient implements the context manager protocol:
"""
>>> import pprint
>>> from pymongo import MongoClient

>>> with MongoClient() as client:
...     db = client.rptutorials
...     for doc in db.tutorial.find():
...         pprint.pprint(doc)
...
{'_id': ObjectId('600747355e6ea8d224f754ba'),
 'author': 'Jon',
 'contributors': ['Aldren', 'Geir Arne', 'Joanna', 'Jason'],
 'title': 'Reading and Writing CSV Files in Python',
 'url': 'https://realpython.com/python-csv/'}
    ...
{'_id': ObjectId('6008511c87eb0fbf73dbf71f'),
 'author': 'David',
 'contributors': ['Aldren', 'Joanna', 'Jacob'],
 'title': 'Object-Oriented Programming (OOP) in Python 3',
 'url': 'https://realpython.com/python3-object-oriented-programming/'}
