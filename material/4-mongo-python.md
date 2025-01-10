# MongoDB with Python

In the fourth section of the course, we learn how to use MongoDB with Python programming language. During this section, you will learn how to build a database application using Python and the PyMongo library.

## PyMongo

PyMongo is a Python library containing tools for working with MongoDB and is the recommended way to work with MongoDB from Python. With PyMongo, we can execute similar database operations as we did with the MongoDB Shell, but using Python. This is handy when we want to implement database applications instead of just executing queries.

First things first, we need to install the PyMongo library. On Windows computer execute (type in the command and press the <kbd>Enter</kbd> key) the following command in the [PowerShell](https://learn.microsoft.com/en-us/powershell/scripting/overview?view=powershell-7.4) application and on macOS computer in the [Terminal](https://support.apple.com/en-gb/guide/terminal/welcome/mac) application:

```bash
python -m pip install pymongo
```

> [!TIP]  
> If the command doesn't work, try the `python3` command instead of the `python` command. The correct command depends on the Python installation.

Next, go through the [tutorial](https://pymongo.readthedocs.io/en/stable/tutorial.html) in _small steps_:

1. Create a Python program which imports the `pymongo` library
2. Initialize a `MongoClient` object and see that the database connection works
3. Print all the documents in one of the collections you inserted test data for in the previous section using the [find](https://www.w3schools.com/python/python_mongodb_find.asp) method
4. Try out other operations, e.g. by inserting a document into a collection

Execute the program after each step and see that there are no errors.

> [!IMPORTANT]  
> Exercise 1 👨‍💻: Try out the database connection and the basic MongoDB operations using the `pymongo` library with your database by following the steps above. There's no need to include this prototyping code in the submission.

## Database application

Now that we know the basics of PyMongo, let's implement a database application for our project. At this point, you should have already designed the database schema and inserted some test data to the database. Use Python and PyMongo to implement a simple database application which uses the database. These are the requirements for the application:

- _Some kind of user interface_. The easiest way is to implement a command-line user interface that reads user input from the command line with the [input](https://www.w3schools.com/python/ref_func_input.asp) function and prints information with the [print](https://www.w3schools.com/python/ref_func_print.asp) function. You can use [this](./application.py) Python program as a starting point. If you want, you can also do something fancier, like a web application using [Flask](https://flask.palletsprojects.com/en/3.0.x/quickstart/)
- Usage of _all CRUD operations_ for at least two collections

Implement the application _one simple feature at a time_ and confirm that it works before moving on to the next feature. Starting with a create feature of one of the collections is a good place to start. Use the MongoDB Compass to verify that different features work, for example by checking that a document is added to a collection using the create feature.

These PyMongo guides will be useful while implementing the CRUD features:

- [Insert Document](https://www.w3schools.com/python/python_mongodb_insert.asp)
- [Find Documents](https://www.w3schools.com/python/python_mongodb_find.asp)
- [Update Documents](https://www.w3schools.com/python/python_mongodb_update.asp)
- [Delete Documents](https://www.w3schools.com/python/python_mongodb_delete.asp)

### Working with the `_id` primary key

The `_id` primary key is useful for referencing a specific document e.g. when deleting or updating it. We just need to remember that the value of the `_id` attribute is an `ObjectId` object:

```python
from pymongo import MongoClient
from bson.objectid import ObjectId

book_id_to_delete = "6780b2d277f48b749b940ee4"

# ❌ Using a string won't work, the following won't delete the correct document
db.book.delete_one({ "_id": book_id_to_delete })

# ✔️ Using an ObjectId object will work
db.book.delete_one({ "_id": ObjectId(book_id_to_delete) })
```

### Relationships between documents

Consider how you establish relationships between documents, e.g. author of a book. For example, creating a `book` with an `author` could be implemented in the following way:

```python
from pymongo import MongoClient
from bson.objectid import ObjectId

# ...

def add_book():
  # Request other attributes from the user...
  author = input("Author ID:")

  book = {
    # Other attributes...
    # We need to use an ObjectId object as the author attribute value
    "author": ObjectId(author)
  }

  db.book.insert_one(book)
```

In this case, the author could also be provided in a more user-friendly way by providing the author's full name and using it to find the corresponding author's `_id` attribute value.

> [!IMPORTANT]  
> Exercise 2 👨‍💻: Implement a Python database application based on the requirements.

### ⭐ Bonus: ideas for additional features

If you want to expand your application here are some ideas for optional requirements:

- Filtering information (e.g. searching books based on name, author, category, or other properties)
- Statistics (e.g. number of books of each author)
- Instead of a local MongoDB database, create a database in the [MongoDB Atlas](https://www.mongodb.com/products/platform/cloud) and [connect to it in your application](https://pymongo.readthedocs.io/en/stable/atlas.html). NB: If you are going to publish the source code of your project (e.g. in GitHub), make sure to use an [envinronment variable](https://www.geeksforgeeks.org/using-python-environment-variables-with-python-dotenv/) for the database connection string

## Submitting the course work

We are done, good job! 🎉 The last thing to do is to submit the project. There are two ways to do it:

1. Create a _public_ [GitHub](https://github.com/) repository for the exercises and the project. This is the recommended way because it adds another cool project to your portfolio. But, if you don't know anything about Git or GitHub, you don't have to learn it for this course. Add the link to the GitHub repository to the Moodle submission (link below)
2. Add the exercises and the project to a folder and turn it into a compressed zip folder. Add the zip folder to the Moodle submission (link below)

> [!IMPORTANT]  
> Exercise 3 👨‍💻: Submit your work to the "MongoDB with Python" Moodle submission by following the instructions above.

Once you have done all the submissions (from this section and the previous sections), your work will be reviewed as soon as possible. If it takes more than two weeks for your submission to be reviewed, contact the teacher. After the review, if there are no problems with your work, you'll get the credits. Otherwise, you'll be asked to make changes and re-submit your work.
