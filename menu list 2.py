# Menu dictionary
menu = {
    "Fast Burgers" : {
        "Small Burger" : 1.99,
        "Medium Burger" : 2.99,
        "Large Burger" : 3.99,
        "add cheese" : 0.50
    },
    "Burger Specials" : {
        "Quick Burger" : 6.99,
        "Express Burger" : 6.99,
        "First Class" : 8.99,
        "Fastlane Special" : 9.99
    },

    "Fast Fries" : {
        "Small" : 0.99,
        "Medium" : 1.99,
        "Large" : 2.99
    },

    "Drinks" : {
        "Fountain Drink" : 1.99,
        "Can Soda" : 0.99,
        "Bottled Water" : 1.99
    }
}


            
# 1. Set up order list. Order list will store a list of dictionaries for
# menu item name, item price, and quantity ordered


# Launch the store and present a greeting to the customer
print("Welcome to Fastlane Burgers food truck")

# Customers may want to order multiple items, so let's create a continuous
# loop
place_order = True
while place_order:
    # Ask the customer from which menu category they want to order
    print("From which menu would you like to order? ")

    # Create a variable for the menu item number
    i = 1
    # Create a dictionary to store the menu for later retrieval
    menu_items = {}

    # Print the options to choose from menu headings (all the first level
    # dictionary items in menu).
    for key in menu.keys():
        print(f"{i}: {key}")
        # Store the menu category associated with its menu item number
        menu_items[i] = key
        # Add 1 to the menu item number
        i += 1

    # Get the customer's input
    menu_category = input("Type menu number: ")

    # Check if the customer's input is a number
    if menu_category.isdigit():
        # Check if the customer's input is a valid option
        if int(menu_category) in menu_items.keys():
            # Save the menu category name to a variable
            menu_category_name = menu_items[int(menu_category)]
            # Print out the menu category name they selected
            print(f"You selected {menu_category_name}")

            # Print out the menu options from the menu_category_name
            print(f"What {menu_category_name} item would you like to order?")
            i = 1
            menu_items = {}
            print("Item # | Item name                | Price")
            print("-------|--------------------------|-------")
            for key, value in menu[menu_category_name].items():
                # Check if the menu item is a dictionary to handle differently
                if type(value) is dict:
                    for key2, value2 in value.items():
                        num_item_spaces = 24 - len(key + key2) - 3
                        item_spaces = " " * num_item_spaces
                        print(f"{i}      | {key} - {key2}{item_spaces} | ${value2}")
                        menu_items[i] = {
                            "Item name": key + " - " + key2,
                            "Price": value2
                        }
                        i += 1
                else:
                    num_item_spaces = 24 - len(key)
                    item_spaces = " " * num_item_spaces
                    print(f"{i}      | {key}{item_spaces} | ${value}")
                    menu_items[i] = {
                        "Item name": key,
                        "Price": value
                    }
                    i += 1
            # 2. Ask customer to input menu item number
menu_item_number = input("Please enter item number.")

            # 3. Check if the customer typed a number
if menu_item_number. isdigit():
        print("You slected a number.")
                # Convert the menu selection to an integer
menu_item_number = int(menu_item_number)

                # 4. Check if the menu selection is in the menu items
if menu_item_number is menu_items.keys():
                    # Store the item name as a variable
 menu_item_name = menu_items[menu_item_number]["Item Name"]
menu_item_price = menu_items[menu_item_number]["Price "]
print (f"{menu_item_name}")
                    # Ask the customer for the quantity of the menu item
is_valid_amount = False
while not is_valid_amount:
         quantity = input("Please select yout prefered quantity. ")

                    # Check if the quantity is a number, default to 1 if not
if quantity.isdigit():
                    quantity = int(quantity)
                else:
                    quantity = 1
                    print("Input is invalid, defaulting quantity to 1.")

                    # Add the item name, price, and quantity to the order list
order_item = {
                    "Item_name": menu_item_name,
                    "Price": menu_item_price,
                    "Quantity": quantity
}


order_list = {"Item_name": menu_item_name, 
                                "Price": menu_item_price,
                                "Quantity": quantity }
order_list.append(order_item) 


                    # Tell the customer that their input isn't valid
print("You made an invalid selection.")


                # Tell the customer they didn't select a menu option
print("You did not select a menu option.")
       
          # Tell the customer they didn't select a menu option
else:
print(f"{menu_category} was not a menu option.")
 
        # Tell the customer they didn't select a number
else:
print("You didn't select a number.")

   
        # Ask the customer if they would like to order anything else

while True:
    keep_ordering = input("Would you like to keep ordering? (Y)es or (N)o ")

        # 5. Check the customer's input
    while true:
           

                # Keep ordering
     if keep_ordering == "N":
         place_order = False
    print("Keep Ordering Please. ")  

                # Exit the keep ordering question loop
break
                # Complete the order

                # Since the customer decided to stop ordering, thank them for
                # their order

                # Exit the keep ordering question loop


                # Tell the customer to try again
print("Please try again.")


# Print out the customer's order
print("This is what we are preparing for you.\n")

# Uncomment the following line to check the structure of the order
#print(order)

print("Item name                 | Price  | Quantity")
print("--------------------------|--------|----------")

# 6. Loop through the items in the customer's order
for i in range(len(order)):

    # 7. Store the dictionary items as variables
    menu_item_name = order[i]["Item name "]
    price = order[i]["Price "]
    quantity = order[i]["Quantity "]



    # 8. Calculate the number of spaces for formatted printing
num_item_spaces = 26 - len(menu_item_name)
num_price_spaces = 6 - len(str(price))

    # 9. Create space strings
item_spaces = " " * num_item_spaces
price_spaces = " " * num_price_spaces

    # 10. Print the item name, price, and quantity
print(f"{menu_item_name}{item_spaces}|${price}{price_spaces}|{quantity}")

# 11. Calculate the cost of the order using list comprehension
# Multiply the price by quantity for each item in the order list, then sum()
# and print the prices.
total_cost = sum([menu_items[price] * menu_items[quantity]
for item in order])
print(f"The total cost of your order is: ${total_cost: .2f}")