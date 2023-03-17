import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Initialize Firebase Admin SDK
cred = credentials.Certificate('myfirstproject-4e9c9-firebase-adminsdk-liis4-4fe062b87a.json')
firebase_admin.initialize_app(cred)

# Get a reference to the Firestore database
db = firestore.client()

# Get a reference to the shopping cart collection
shopping_cart_ref = db.collection('shopping_cart')

# Start with no user logged in
user = None

# Add a loop to handle user input
while True:
    if user:
        print(f"\nHello {user}, please select one of the following actions: \n1. Add Item, \n2. View Items, \n3. Remove Item, \n4. Compute Total Items, \n5. Update Item, \n6. Log out or quit ")
        action_taken = input("Enter Your Choice: ")
    else:
        print("Please select one of the following actions: \n1. Log in, \n2. Sign up, \n3. Quit ")
        action_taken = input("Enter Your Choice: ")

    if action_taken == '1' and user:
        grocery_item = input("Enter the name of the item you want to add:")
        grocery_amount = input("Enter the amount of the item:")
        shopping_cart_ref.add({
            'name': grocery_item,
            'amount': grocery_amount
        })

    elif action_taken == '2' and user:
        shopping_cart = shopping_cart_ref.get()
        for doc in shopping_cart:
            print(doc.to_dict()['name'], doc.to_dict()['amount'])

    elif action_taken == '1' and not user:
        id = input("Enter your ID: ")
        password = input("Enter your password: ")
        user_ref = db.collection('users').document(id)
        if user_ref.get().exists and user_ref.get().to_dict()['password'] == password:
            user = id
            print("Logged in successfully.")
        else:
            print("\nInvalid ID or password.\n")

    elif action_taken == '3' and user:
        grocery_item_to_remove = input("Enter the name of the item you want to remove:")
        query = shopping_cart_ref.where('name', '==', grocery_item_to_remove)
        docs = query.stream()
        for doc in docs:
            doc.reference.delete()

    elif action_taken == '4' and user:
        shopping_cart = shopping_cart_ref.get()
        total = sum([float(doc.to_dict()['amount']) for doc in shopping_cart])
        print('Total:', total)

    elif action_taken == '5' and user:
        grocery_item_to_update = input("Enter the name of the item you want to update:")
        grocery_amount_to_update = input("Enter the new amount of the item:")
        query = shopping_cart_ref.where('name', '==', grocery_item_to_update)
        docs = query.stream()
        for doc in docs:
            doc.reference.update({'amount': grocery_amount_to_update})

    elif action_taken == '6':
        user = None
        print("\nLogged out\n")

    elif action_taken == '2':
        # Allow user to sign up with a unique ID and password
        if not user:
            id = input("Enter your ID: ")
        password = input("Enter your password: ")
        # Check if user already exists
        user_ref = db.collection('users').document(id)
        if user_ref.get().exists:
            print("\nUser already exists. Please log in.\n")
        else:
            user_ref.set({'password': password})
            print("\nUser created successfully. Please log in.\n")

    elif action_taken == '3':
        if not user:
            print("\nGoodbye!\n")
            break
        else:
            print("\nPlease log out before quitting.\n")

    else:
        print("\nInvalid Choice\n")
