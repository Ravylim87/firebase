# Overview

In this particular module, I am utilizing the dynamic and versatile Python programming language to develop a robust program that seamlessly integrates with Firebase, a cutting-edge cloud-based platform for data storage. The program boasts an array of user-friendly options, including the ability to log in, sign up, or gracefully exit the system. Once a user logs in, an entire spectrum of advanced functionalities become available, including the ability to Add Item, View Items, Remove Item, Compute Total Items, Update Item, Log out, or quit the application.

The primary objective of designing and developing this program was to provide the user with a comprehensive, easy-to-use grocery list tool that enables them to conveniently store and access the items they need to purchase during their shopping trips. The program empowers users to efficiently organize and manage their grocery lists, ensuring that they never miss out on essential items again. Whether it's for a weekly or monthly shopping trip, this innovative program offers unparalleled functionality and convenience, simplifying the entire shopping experience.


[Software Demo Video](https://www.youtube.com/watch?v=BQwr8gnj0Wo)

# Cloud Database

The code is using the Firebase Firestore, which is a flexible, scalable NoSQL cloud database provided by Google. Firestore provides various features like automatic syncing, real-time updates, offline data access, and robust security rules to ensure data privacy and integrity.

The database structure is relatively simple, containing two collections, 'users' and 'shopping_cart'. The 'users' collection has documents with user IDs as document IDs and password fields to store user login credentials. The 'shopping_cart' collection contains documents representing items added by the user to their shopping cart, with fields for the name of the item and the quantity needed.

The program uses the db object initialized using the Firebase Admin SDK to access the collections and documents. The program also uses the firestore module's various methods to perform operations like adding documents, updating documents, deleting documents, querying documents, and retrieving documents from the collections.

# Development Environment

The software was developed using the Python programming language and the Firebase platform for cloud data storage. The Firebase Admin SDK was used to connect to the Firebase Firestore database and perform database operations. The program also uses the input() function to receive user input and the print() function to display output to the user.

In addition to the Firebase Admin SDK, the program uses the firebase_admin, credentials, and firestore libraries provided by Firebase. No other external libraries or modules were used in the program.

# Useful Websites

{Make a list of websites that you found helpful in this project}

- [Firestore Tutorial](https://firebase.google.com/docs/firestore)
- [Firebase Console](https://firebase.google.com/docs/firestore)

# Future Work

- User Interface: The current program is entirely text-based, which may not be very user-friendly. Adding a graphical user interface (GUI) could greatly improve the user experience.
- Error Handling: The program assumes that all user input is valid and does not include much error handling. Adding error handling and input validation could make the program more robust and less prone to crashing.
- Integration with Other Services: The program could be integrated with other services, such as online grocery stores or delivery services, to provide a more comprehensive shopping experience.