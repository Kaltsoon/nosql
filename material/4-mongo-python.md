# MongoDB with Python

In the fourth section of the course we learn how to use MongoDB with Python programming language. During this section your will learn how to build a database application using Python and the PyMongo library.

## PyMongo

PyMongo is a Python library containing tools for working with MongoDB, and is the recommended way to work with MongoDB from Python. With PyMongo, we can execute similar database operations as we did with the MongoDB Shell, but using Python. This is handy when we want to implement database applications instead of just executing queries.

First things first, let's install PyMongo by following [these](https://pymongo.readthedocs.io/en/stable/installation.html) instructions. Follow the "Installing with pip" instructions.

> [!IMPORTANT]  
> Try `python` command instead of `python3` command, if it doesn't work. The correct command depends on the Python installation.

Next, go through the [tutorial](https://pymongo.readthedocs.io/en/stable/tutorial.html) in _small steps_:

1. Create a Python program which imports the `pymongo` library
2. Initialize a `MongoClient` object and see that the database connection works
3. Print all the documents in one of the collections you inserted test data for in the previous section
4. Try out the other operations in the tutorial

Execute the program after each step and see that there's no errors.

### Database application

Now that we know the basics of PyMongo, let's implement a database application for our project. At this point you should have already designed the database schema and inserted some test data to the database. Use Python and PyMongo to implement a simple database application which uses the database. These are the requiremenets for the application:

- _Some kind of user interface_. The easiest way is to implement a command-line user interface which reads user input from the command-line with the [input](https://www.w3schools.com/python/ref_func_input.asp) function and prints information with the [print](https://www.w3schools.com/python/ref_func_print.asp) function. You can use [this](./application.py) Python program as a starting point. If you want, you can also do something fancier, like a web application using [Flask](https://flask.palletsprojects.com/en/3.0.x/quickstart/)
- Usage of _all CRUD operations_ for at least two collections

#### Where to start?

Implement the application _one simple feature at a time_ and confirm that it works before moving on to the next feature. Starting with a create feature of one of the collections is a good place to start. Read the [Inserting a document](https://pymongo.readthedocs.io/en/stable/tutorial.html#inserting-a-document) documentation for implementation instructions. Use the MongoDB Compass to verify that different features work, for example by checking that a document is added to a collection using the create feature.

Consider how you establish connections between collections. For example, creating a `book` with an `author` could be implemented in the following way:

```python
from bson.objectid import ObjectId

author_id = input("Author ID:")
# Request other attributes from the user...

book = {
  # Other attributes...
  # We need to use an ObjectId object as the author attribute value
  "author": ObjectId(author_id)
}

db.book.insert_one(book)
```

#### ⭐ Bonus: ideas for additional features

If you want to expand your application here's some ideas for optional requirements:

- Filtering information (e.g. searching books based on name, author, category or other properties)
- Statistics (e.g. number of books of each author)
- Instead of local MongoDB database, create a database in the [MongoDB Atlas](https://www.mongodb.com/products/platform/cloud) and [connect to it in your application](https://pymongo.readthedocs.io/en/stable/atlas.html). NB: If you are going to publish the source code of your project (e.g. in GitHub), make sure to use an [envinronment variable](https://www.geeksforgeeks.org/using-python-environment-variables-with-python-dotenv/) for the database connection string

## Submitting the course work

We are done, good job! 🎉 The last thing to do is to submit the exercises and the project. There are two ways to do it:

1. Create a _public_ [GitHub](https://github.com/) repository for the exercises and the project. This is the recommended way because it adds another cool project for your portfolio. But, if you don't know anything about Git, you don't have to learn it for this course. Add the link to the GitHub repository to the Moodle submission (link below)
2. Add the exercises and the project to a folder and turn it into a compressed zip folder. Add the zip folder to the Moodle submission (link below)

Regardless of the way you want to submit the exercises and the project, use the following folder structure:

```
exercises/ <- all exercise-related files goes to this folder
  part2.pdf
  part3.pdf
project/ <- all project-related files goes to this folder
  ...
```

TODO
The exercise files can be either PDF or Markdown files. The exercises and the project are submitted to [this]() Moodle submission. Once you have done the submission, your work will be reviewed as soon as possible. If it takes more than two weeks for you submission to be reviewed, contact the teacher. After the review, if there are no problems with your work, you'll get the credits. Otherwise, you'll be asked to make changes and re-submit your work.
