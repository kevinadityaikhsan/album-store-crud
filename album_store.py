from tabulate import tabulate

# Define album data using a list of dictionaries
album_data = [
    {"Title": "The Dark Side of the Moon", "Artist": "Pink Floyd", "Genre": "Progressive Rock", "Stock": 20, "Price ($)": 29.99},
    {"Title": "Thriller", "Artist": "Michael Jackson", "Genre": "Pop", "Stock": 15, "Price ($)": 19.99},
    {"Title": "Abbey Road", "Artist": "The Beatles", "Genre": "Rock", "Stock": 25, "Price ($)": 24.99},
    {"Title": "Back in Black", "Artist": "AC/DC", "Genre": "Hard Rock", "Stock": 30, "Price ($)": 22.99},
    {"Title": "The White Album", "Artist": "The Beatles", "Genre": "Rock", "Stock": 22, "Price ($)": 26.99},
    {"Title": "Rumours", "Artist": "Fleetwood Mac", "Genre": "Soft Rock", "Stock": 18, "Price ($)": 17.99},
    {"Title": "Led Zeppelin IV", "Artist": "Led Zeppelin", "Genre": "Hard Rock", "Stock": 20, "Price ($)": 21.99},
    {"Title": "The Wall", "Artist": "Pink Floyd", "Genre": "Progressive Rock", "Stock": 15, "Price ($)": 27.99},
    {"Title": "Born to Run", "Artist": "Bruce Springsteen", "Genre": "Rock", "Stock": 12, "Price ($)": 20.99},
    {"Title": "Hotel California", "Artist": "Eagles", "Genre": "Rock", "Stock": 28, "Price ($)": 23.99},
    {"Title": "Let It Be", "Artist": "The Beatles", "Genre": "Rock", "Stock": 20, "Price ($)": 25.99},
    {"Title": "The Joshua Tree", "Artist": "U2", "Genre": "Rock", "Stock": 25, "Price ($)": 28.99},
]

# Initialize an empty list for the transaction cart
trx = []

def show_albums(): # Read (R1)
    """Display the album data."""
    
    # Prepare data for tabulation
    headers = ["Index", "Title", "Artist", "Genre", "Stock", "Price ($)"]
    formatted_album_data = []
    for index, album in enumerate(album_data):
        album_row = [index + 1, album["Title"], album["Artist"], album["Genre"], album["Stock"], album["Price ($)"]]
        formatted_album_data.append(album_row)
    print("\n", tabulate(formatted_album_data, headers=headers, tablefmt="grid"))

def edit_album_data(): # Update (U1)
    """Edit the album data."""
    global album_data

    while True:
        show_albums()  
        try:
            index = int(input("\nEnter the index of the album you want to edit (0 to cancel): "))
            if index == 0:
                print("Action canceled. Returning to previous menu.")
                break
            elif 1 <= index <= len(album_data):
                album = album_data[index - 1]
                print(f"\nEditing {album['Title']}...")

                while True:
                    print("""
                    1. Edit album title
                    2. Edit artist
                    3. Edit genre
                    4. Edit stock
                    5. Edit price
                    0. Return to previous menu
                    """)

                    edit_choice = input("Enter your choice: ")
                    if edit_choice == '1':
                        # Prompt for a new album title
                        while True:
                            new_title = input("Enter new album title: ")
                            if any(t["Title"] == new_title for t in album_data):
                                print("Album with that name already exists!")
                                continue
                            break
                        
                        album["Title"] = new_title
                        print("Album title edited successfully!")
                        show_albums()

                    elif edit_choice == '2':
                        # Prompt for a new artist
                        new_artist = input("Enter new artist: ")
                        album["Artist"] = new_artist
                        print("Artist edited successfully!")
                        show_albums()

                    elif edit_choice == '3':
                        # Prompt for a new genre
                        new_genre = input("Enter new genre: ")
                        album["Genre"] = new_genre
                        print("Genre edited successfully!")
                        show_albums()

                    elif edit_choice == '4':
                        # Prompt for a new stock
                        while True:
                            try:
                                new_stock = int(input("Enter new stock: "))
                                if new_stock < 0:
                                    print("Invalid input! Please enter a positive number for stock.")
                                    continue
                                album["Stock"] = new_stock
                                print("Stock edited successfully!")
                                show_albums()
                                break
                            except ValueError:
                                print("Invalid input! Please enter a valid number for stock.")

                    elif edit_choice == '5':
                        # Prompt for a new price
                        while True:
                            try:
                                new_price = float(input("Enter new price: $"))
                                if new_price <= 0:
                                    print("Invalid input! Please enter a positive number for price.")
                                    continue
                                album["Price ($)"] = new_price
                                print("Price edited successfully!")
                                show_albums()
                                break
                            except ValueError:
                                print("Invalid input! Please enter a valid number for price.")

                    elif edit_choice == '0':
                        print("Returning to previous menu.")
                        break

                    else:
                        print("Invalid input! Please enter a valid choice.")
                show_albums()
                break
            else:
                print("Invalid input! Please enter the available index.")
        except ValueError:
            print("Invalid input! Please enter the available index.")

def add_album(): # Create (C1)
    """Add a new album to the list."""
    show_albums()
    
    # Prompt for album title
    input_album_title = input("\nInput album title: ")
    
    # Check if the album already exists in the album data
    if any(album["Title"] == input_album_title for album in album_data):
        print("Album already exists!")
        
        # Loop until a valid additional quantity is provided
        while True:
            try:
                add_qty = int(input("Enter the additional quantity: "))
                if add_qty <= 0:
                    print("Invalid input! Please enter a positive number for quantity.")
                else:
                    # Add the additional quantity to the existing stock
                    for album in album_data:
                        if album["Title"] == input_album_title:
                            album["Stock"] += add_qty
                    print("Album quantity added successfully!")
                    show_albums()
                    return
            except ValueError:
                print("Invalid input! Please enter a positive number for quantity.")
    else:
        # Prompt for artist
        input_album_artist = input("Input artist: ")
        
        # Prompt for genre
        input_album_genre = input("Input genre: ")
        
        # Loop until a valid stock is provided
        while True:
            try:
                input_album_stock = int(input("Input album stock: "))
                if input_album_stock <= 0:
                    print("Invalid input! Please enter a positive number for stock.")
                    continue
                break
            except ValueError:
                print("Invalid input! Please enter a valid number for stock.")

        # Loop until a valid price is provided
        while True:
            try:
                input_album_price = float(input("Input album price: $"))
                if input_album_price <= 0:
                    print("Invalid input! Please enter a positive number for price.")
                    continue
                break
            except ValueError:
                print("Invalid input! Please enter a valid number for price.")

        # Add the new album to the album data
        album_data.append({"Title": input_album_title, "Artist": input_album_artist, "Genre": input_album_genre, "Stock": input_album_stock, "Price ($)": input_album_price})
        print("Album added successfully!")
        show_albums()

def delete_album(): # Delete (D1)
    """Delete album from the list."""
    
    # Loop until a valid index is provided
    while True:
        try:
            show_albums()
            
            # Prompt the user to enter the index to delete
            index_to_delete = int(input("\nEnter the index you want to delete (0 to cancel): "))
            if index_to_delete == 0:
                print("Action canceled. Returning to previous menu.")
                break
            elif 1 <= index_to_delete <= len(album_data):
                # Delete the album at the specified index
                del album_data[index_to_delete - 1]
                print("Album deleted successfully!")
                show_albums()
                break
            else:
                print("Invalid input! Please enter the available index.")
        except ValueError:
            print("Invalid input! Please enter the available index.")

def add_item(): # Create (C2) and Update (U2)
    """Add items to the shopping cart."""
    
    while True:
        try:
            show_albums()
            
            # Prompt the user to enter the index of the album to add
            index = int(input("\nEnter the index of the album you want to add (0 to cancel): "))
            if index == 0:
                print("Action canceled. Returning to previous menu.")
                break
            elif 1 <= index <= len(album_data):
                selected_album = album_data[index - 1]
                if selected_album["Stock"] == 0:
                    print("Sorry, this album is out of stock.")
                    continue

                # Check if the selected album already exists in the cart
                selected_index = None
                for i, item in enumerate(trx):
                    if item["Title"] == selected_album["Title"]:
                        selected_index = i
                        break

                if selected_index is not None: # Album already exists in cart
                    while True:
                        try:
                            qty = int(input("Enter the additional quantity: "))
                            if qty <= 0:
                                print("Invalid input! Please enter a positive number for quantity.")
                                continue
                            if qty > selected_album["Stock"]:
                                print("Sorry, we don't have enough stock for this album.")
                                continue

                            # Update quantity and subtotal
                            trx[selected_index]["Qty"] += qty
                            subtotal = selected_album["Price ($)"] * qty
                            selected_album["Stock"] -= qty
                            trx[selected_index]["Subtotal ($)"] += subtotal
                            print("Album quantity updated successfully!")
                            show_albums()
                            return
                        except ValueError:
                            print("Invalid input! Please enter a positive number for quantity.")

                else: # Album doesn't exist in cart
                    while True:
                        try:
                            qty = int(input("Enter the quantity: "))
                            if qty <= 0:
                                print("Invalid input! Please enter a positive number for quantity.")
                                continue
                            if qty > selected_album["Stock"]:
                                print("Sorry, we don't have enough stock for this album.")
                                continue

                            # Calculate subtotal and add the album to the cart
                            subtotal = selected_album["Price ($)"] * qty
                            selected_album["Stock"] -= qty
                            trx.append({"Title": selected_album["Title"], "Artist": selected_album["Artist"], "Genre": selected_album["Genre"], "Qty": qty, "Price ($)": selected_album["Price ($)"], "Subtotal ($)": subtotal})
                            print("Album added to the cart successfully!")
                            show_albums()
                            return
                        except ValueError:
                            print("Invalid input! Please enter a positive number for quantity.")
            else:
                print("Invalid input! Please enter the available index.")
        except ValueError:
            print("Invalid input! Please enter the available index.")

def view_cart(): # Read (R2)
    """View the shopping cart and proceed to payment."""
    if trx:
        # Display the shopping cart contents
        print("\nShopping cart: ")
        headers = ["Title", "Artist", "Genre", "Qty", "Price ($)", "Subtotal ($)"]
        album_cart_data = [[item["Title"], item["Artist"], item["Genre"], item["Qty"], item["Price ($)"], item["Subtotal ($)"]] for item in trx]
        print(tabulate(album_cart_data, headers=headers, tablefmt="grid"))

        # Calculate and display the total amount
        total_amount = sum(item["Subtotal ($)"] for item in trx)
        print(f"Total amount for shopping cart: ${total_amount}")

        # Prompt for payment confirmation
        proceed_payment = ""
        while proceed_payment not in ("Y", "N"):
            proceed_payment = input("\nProceed to payment? (Y/N) : ").strip().upper()

            if proceed_payment == "Y":
                # Process payment
                while True:
                    try:
                        payment_amount = float(input("Enter the payment amount: $"))
                        if payment_amount < total_amount:
                            print(f"Insufficient payment! You still owe ${total_amount - payment_amount:.2f}.")
                        elif payment_amount == total_amount:
                            print("Payment successful! Thank you!")
                            trx.clear()
                            return
                        else:
                            change = payment_amount - total_amount
                            print(f"Payment successful! Here is your change: ${change:.2f}")
                            print("Thank you!")
                            trx.clear()
                            return
                    except ValueError:
                        print("Invalid input! Please enter a valid amount for payment.")

            elif proceed_payment == "N":
                print("Payment canceled. You can continue shopping.")
                return
            
            else:
                print("Invalid input! Please enter a valid choice to proceed.")
    else:
        print("Shopping cart is empty.")

def edit_cart_item(): # Update (U3)
    """Edit items in the shopping cart."""

    while True:
        try:
            if not trx:
                print("Shopping cart is empty.")
                break

            # Display the current shopping cart
            print("\nShopping cart")
            headers = ["Index", "Title", "Artist", "Qty", "Price ($)", "Subtotal ($)"]
            album_cart_data = []
            for i, item in enumerate(trx):
                trx_row = [i + 1, item["Title"], item["Artist"], item["Qty"], item["Price ($)"], item["Subtotal ($)"]]
                album_cart_data.append(trx_row)
            print("\n", tabulate(album_cart_data, headers=headers, tablefmt="grid"))

            # Prompt the user to select an item to edit
            index = int(input("\nEnter the index of the album you want to edit (0 to cancel): "))
            if index == 0:
                print("Process canceled. Returning to the previous menu.")
                break
            elif 1 <= index <= len(trx):
                item = trx[index - 1]
                print(f"Editing {item['Title']}...")

                # Prompt the user to enter the new quantity
                while True:
                    try:
                        new_qty = int(input("Enter the new quantity (0 to remove): "))
                        if new_qty == 0:
                            # Update stock and remove the item from the cart
                            diff_qty = item["Qty"]
                            for album in album_data:
                                if album["Title"] == item["Title"]:
                                    album["Stock"] += diff_qty
                            trx.pop(index - 1)
                            break
                        elif new_qty < 0:
                            print("Invalid input! Please enter a positive number for quantity.")
                            continue
                        else:
                            diff_qty = new_qty - item["Qty"]
                            # Check if there's enough stock for the new quantity
                            for album in album_data:
                                if album["Title"] == item["Title"]:
                                    if diff_qty > 0 and diff_qty > album["Stock"]:
                                        print("Sorry, we don't have enough stock for this album.")
                                        break
                            else:
                                # Update item quantity, subtotal, and stock
                                item["Qty"] = new_qty
                                item["Subtotal ($)"] = item["Price ($)"] * new_qty
                                for album in album_data:
                                    if album["Title"] == item["Title"]:
                                        album["Stock"] -= diff_qty
                                print("Item quantity updated successfully!")
                                break
                    except ValueError:
                        print("Invalid input! Please enter a positive number for quantity.")

            else: 
                print("Invalid input! Please enter the available index.")
        except ValueError:
            print("Invalid input! Please enter the available index.")

def cancel_transaction(): # Delete (D2)
    """Clear cart when transaction canceled."""
    
    # Restore the stock for each item in the cart
    for item in trx:
        for album in album_data:
            if album["Title"] == item["Title"]:
                album["Stock"] += item["Qty"]
    
    # Clear the transaction cart
    trx.clear()
    print("Transaction canceled. Returning to previous menu.")

def buy_album(): # Sub Menu
    """Menu to buy album."""           
    while True:
        print("""
        \n
        1. Add item to the cart
        2. View cart
        3. Edit cart item
        0. Cancel transaction
        \n
        """)
        buy_choice = input("Enter your choice: ")
        if buy_choice == '1':
            add_item()
        elif buy_choice == '2':
            view_cart()
        elif buy_choice == '3':
            edit_cart_item()
        elif buy_choice == '0':
            cancel_transaction()
            break
        else:
            print("Invalid input! Please enter a valid number to proceed.")

def main(): # Main Menu
    """Main function to execute the program."""
    while True:
        print("""
        Welcome to the album market!

        Menu list:
        1. Show albums
        2. Edit albums
        3. Add album
        4. Delete album
        5. Buy album
        0. Exit program     
        """)
        menu_choice = input("Enter the number of the menu you want to execute: ")
        if menu_choice == '1':
            show_albums()
        elif menu_choice == '2':
            edit_album_data()
        elif menu_choice == '3':
            add_album()
        elif menu_choice == '4':
            delete_album()
        elif menu_choice == '5':
            buy_album()
        elif menu_choice == '0':
            print("Exiting the program...")
            break
        else:
            print("Invalid input! Please enter a valid number to proceed.")

if __name__ == "__main__":
    main()
