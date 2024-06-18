"""
Storing data in your database using PyMongo is similar to what you did with the mongo shell in the above sections. But first, you need to create your documents. In Python, you use dictionaries to create documents:
"""
>>> tutorial1 = {
...     "title": "Working With JSON Data in Python",
...     "author": "Lucas",
...     "contributors": [
...         "Aldren",
...         "Dan",
...         "Joanna"
...     ],
...     "url": "https://realpython.com/python-json/"
... }

#after creation specify which collection you want to use 
#use the dot notation on the dbase obj.
>>> tutorial = db.tutorial
>>> tutorial
Collection(Database(..., connect=True), 'rptutorials'), 'tutorial')

"""
 tutorial is an instance of Collection and represents a physical collection of documents in your database
 You can insert documents into tutorial by calling .insert_one() on it with a
 doc as an arg
"""
>>> result = tutorial.insert_one(tutorial1)
>>> result
<pymongo.results.InsertOneResult object at 0x7fa854f506c0>

>>> print(f"One tutorial: {result.inserted_id}")
One tutorial: 60084b7d87eb0fbf73dbf71d
#Note that since MongoDB generates the ObjectId dynamically, your output won’t match the ObjectId shown above.
#If you have many documents to add to the database, then you can use .insert_many() to insert them in one go:
