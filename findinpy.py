""""
To retrieve documents from a collection, you can use .find().
Without arguments, .find() returns a Cursor object that yields the
ocuments in the collection on demand:
"""
import pprint

>>> for doc in tutorial.find():
...     pprint.pprint(doc) #provides a user friendly output
..."""answer"""
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

"""use .find_one() to retrieve a single doc.
e.g if u want to retrieve the 1st tutorial by Jon
"""
>>> import pprint

>>> jon_tutorial = tutorial.find_one({"author": "Jon"})

>>> pprint.pprint(jon_tutorial)
{'_id': ObjectId('600747355e6ea8d224f754ba'),
 'author': 'Jon',
 'contributors': ['Aldren', 'Geir Arne', 'Joanna', 'Jason'],
 'title': 'Reading and Writing CSV Files in Python',
 'url': 'https://realpython.com/python-csv/'}
