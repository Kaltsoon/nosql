# Database operations in MongoDB

In the third section of the course we learn the basic database operation in the MongoDB database management system. During this section your will learn e.g. TODO.

## CRUD operations

The [CRUD](https://en.wikipedia.org/wiki/Create,_read,_update_and_delete) operations (create, read, update, delete) are the most common database operations in any database management system. Next, let's practice their usage in MongoDB. Before starting the exercises, oven the MongoDB Compass application we used during the previous section and open the `library` database in MongoDB Shell.

TODO: https://chatgpt.com/share/66ffb828-3890-8006-9e05-2f0914ca8c80

### Inserting documents

> [!IMPORTANT]  
> While you are reading the MongoDB documentation, choose the language as "MongoDB Shell" from the "Select your language" menu.

Read the [Insert Documents](https://www.mongodb.com/docs/manual/tutorial/insert-documents/) guide. Then, insert a single document to the `book` collection with the following details using the `insertOne` method:

| title                 | author        | year | genres                            | copies |
| --------------------- | ------------- | ---- | --------------------------------- | ------ |
| "Pride and Prejudice" | "Jane Austen" | 1813 | ["Romance", "Classic", "Fiction"] | 3      |

Then, list all documents in the `book` collection. You'll notice that each document has an automatically generated `_id` attribute which act as a primary key. These values are [ObjectId](https://www.mongodb.com/docs/manual/reference/method/ObjectId/) objects, such as `ObjectId("507f1f77bcf86cd799439011")`.

Insert the following documents using the `insertMany` method:

| title                   | author                      | year | genres                                                     | copies |
| ----------------------- | --------------------------- | ---- | ---------------------------------------------------------- | ------ |
| "War and Peace"         | "Leo Tolstoy"               | 1869 | ["Historical Fiction", "Classic", "Philosophical Fiction"] | 84     |
| "The Lord of the Rings" | "John Ronald Reuel Tolkien" | 1954 | ["Fantasy", "Adventure", "Epic"]                           | 0      |
| "Brave New World"       | "Aldous Huxley"             | 1931 | ["Dystopian", "Science Fiction", "Classic"]                | 11     |
| "The Hobbit"            | "John Ronald Reuel Tolkien" | 1937 | ["Fantasy", "Classic"]                                     | 17     |

Then, list the all the documents in the `book` collection.

### Querying documents

Read the [Query Documents](https://www.mongodb.com/docs/manual/tutorial/query-documents/) guide. Then, implement and execute the following queries in MongoDB Shell:

1. Find the book, which name is "War and Peace"
2. Find out what's the `_id` attribute value of the book "War and Peace". Then, find the book based on that `_id`. Note that `ObjectId("507f1f77bcf86cd799439011")` is an `ObjectId` object whereas `"507f1f77bcf86cd799439011"` is a string
3. Find books which are published after year 1900
4. Find books with more than 0 copies. Note that `0` is a number whereas `"0"` is a string
5. Find the books written by author "John Ronald Reuel Tolkien" before year 1950
6. Find the books in "Fantasy" genre. Hint: [Query an Array](https://www.mongodb.com/docs/manual/tutorial/query-arrays/)

### Updating documents

Read the [Update Documents](https://www.mongodb.com/docs/manual/tutorial/update-documents/) guide. Then, implement and execute the following queries in MongoDB Shell:

1. Change the publish year of the book "Brave New World" into 1932
2. Set the number of copies as 0 for all books written by the author "John Ronald Reuel Tolkien"
3. Increase the number of copies for books published after 1900 by two. Hint: [$inc](https://www.mongodb.com/docs/manual/reference/operator/update/inc/) operator
4. Add a genre "Adventure" for the book "The Hobbit". Hint: [$push](https://www.mongodb.com/docs/manual/reference/operator/update/push/#mongodb-update-up.-push) operator
5. Remove the genre "Classic" from the book "War and Peace". Hint: [$pull](https://www.mongodb.com/docs/manual/reference/operator/update/pull/) operator

### Deleting documents

Read the [Delete Documents](https://www.mongodb.com/docs/manual/tutorial/remove-documents/) guide. Then, implement and execute the following queries in MongoDB Shell:

1. Delete the book "Pride and Prejudice"
2. Delete all the books which have 0 copies

## Embedding data or using references

Let's consider the case where we would need to store more author-related information to the `book` collection, such as the author's nationality and year of birth. We would need to consider whether adding new attributes to the `book` collection or adding a new `author` collection and referencing it from the `book` collection documents. The latter approach would resemble a foreign key referencing a primary key in a relational database schema.

Read the [Embedded Data Versus References
](https://www.mongodb.com/docs/manual/data-modeling/concepts/embedding-vs-references/) guide. Then, create a new `author` collection with the following documents:

| name                        | birthYear | nationality |
| --------------------------- | --------- | ----------- |
| "Leo Tolstoy"               | 1828      | "Russian"   |
| "John Ronald Reuel Tolkien" | 1892      | "British"   |
| "Aldous Huxley"             | 1894      | "British"   |
| "Jane Austen"               | 1775      | "British"   |

Then, update the documents in the `book` collection so that the `author` attribute is an `ObjectId` object referencing the corresponding document's `_id` attribute in the `author` collection.

## Aggregointi-operaatiot

TODO

⏭️ [Move on to the next section](./4-mongo-python.md)