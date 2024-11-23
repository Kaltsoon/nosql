# Introduction to MongoDB database management system

> MongoDB is a document database with the scalability and flexibility that you want with the querying and indexing that you need.

In the second section of the course we will learn the principles of the MongoDB database management system which is one of the most widely adopted NoSQL database management systems. During this section your will learn about the principles of the data model in the MongoDB database management system, how to install the MongoDB database management system and the MongoDB Compass tool and how to create a database in the MongoDB database management system.

The MongoDB database management system is a widely adopted NoSQL database management system. Based on the [State of Database](https://stateofdb.com/) survey in 2023, MongoDB was among three of most well-known and widely used database management systems along with PostgreSQL and MySQL. MongoDB is a documented-oriented database.

Familiarize yourself with the document-oriented databases by reading the article [What is a Document Database](https://www.mongodb.com/resources/basics/databases/document-databases) and with the principles of the MongoDB database management system by reading the articles [MongoDB Basics](https://www.mongodb.com/resources/products/fundamentals/basics) and [Data Modeling](https://www.mongodb.com/docs/manual/data-modeling/). Once you have read through the articles, test your knowledge by completing the Moodle quiz. After passing the quiz, move on to the next topic in this section.

## Installing MongoDB on our computer

So that we can start practicing the usage of MongoDB we need to install the database management system for our computer. Download the installation program [here](https://www.mongodb.com/try/download/community). Remember to choose the suitable platform based on your operating system (e.g. Windows or macOS).

## User interfaces for using MongoDB

[MongoDB Compass](https://www.mongodb.com/products/tools/compass) is a graphical user interface for operating MongoDB. Other user interfaces for the purpose are e.g. [MongoDB Shell](https://www.mongodb.com/docs/mongodb-shell/) and [MongoDB Vs Code extension]( https://www.mongodb.com/products/tools/vs-code). We will be using MongoDB Compass and the integrated MongoDB Shell in our examples.

MongoDB Compass should be installed along with the MongoDB database management system installed previously. If not, you can install it [here](https://www.mongodb.com/try/download/compass). Once installed, do the following:

1. Open the MongoDB Compass application and a new database connection. The default database connection setting should work for connecting the local MongoDB instance
2. Create a database `library` and in that database create a collection `book`
3. Export the contents of [this](./library.json) JSON file to the `book` collection by following the [Import and Export Data](https://www.mongodb.com/docs/compass/current/import-export/) instructions
4. Open the `library` database in MongoDB Shell by clicking the name of the database in the list of databases on the left and then clicking the "Open MongoDB Shell" button
5. Find out how to implement a query which lists all documents in a collection by reading the [Query Documents](https://www.mongodb.com/docs/manual/tutorial/query-documents/) guide. While you are reading the MongoDB documentation, choose the language as "MongoDB Shell" from the "Select your language" menu. Then, execute a query which list all the documents in the `book` collection using the MongoDB Shell

> [!IMPORTANT]  
> Create a file `part2` (for example a Word document) and add the query and its result in step 5 to the file for a later submission.

## ⭐ Bonus: MongoDB database in the cloud

[MongoDB Atlas](https://www.mongodb.com/atlas) is a cloud-based database service provided by MongoDB, Inc., that allows users to deploy, manage, and scale MongoDB databases with ease. It provides a free plan for hosting MongoDB database in the cloud which accessible to the outside world. This is useful while developing for example a web application used by multiple users.

⏭️ [Move on to the next section](./3-mongo-operations.md)
