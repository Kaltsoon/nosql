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

- Some kind of user interface. The easiest way is to implement a command-line user interface which reads user input from the command-line with the `input` function and prints information with the `print` function. You can use [this](./application.py) Python program as a starting point. If you want, you can also do something fancier, like a web application using [Flask](https://flask.palletsprojects.com/en/3.0.x/quickstart/)
- Usage of all CRUD operations for at least one collection

## The end

TODO

