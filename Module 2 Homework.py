# Menu dictionary
menue = {
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

print("Welcome to Fastlane Burgers food truck.")

place_order = True
while place_order:
    print("From which menu would you like to order? ")
    i = 1
    menu_items = {}
    
    for key in menue.keys():
        print(f"{i}: {key}")   
        menu_items[i] = key
        i += 1

    menu_category = input("Type menu number: ")

    if menu_category.isdigit():
        if int(menu_category) in menu_items.keys():
            menu_category_name = menu_items[int(menu_category)]
            
            print(f"You selected {menu_category_name}")
            print(f"What {menu_category_name} item would you like to order?")

            i = 1
            menu_items = {}

            print("Item # | Item name                | Price")
            print("-------|--------------------------|-------")

            for key, value in menue[menu_category_name].items():
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



            menu_item_number = input("Choose the item number you want to order: ")
            if menu_item_number.isdigit():
             menu_item_number = int(menu_item_number)
            print(menu_items)
            print("You slected a number.")

            if menu_item_number is menu_items.keys():
             menu_item_name = menu_items[menu_item_number]["Item Name"]
             menu_item_price = menu_items[menu_item_number]["Price"]
             print (f"{menu_item_name}")


is_valid_amount = False
while not is_valid_amount:
         quantity = input("Please select yout prefered quantity. ")
         if quantity.isdigit():
                    quantity = int(quantity)
                    order_item = {
                    "Item_name": menu_item_name,
                    "Price": menu_item_price,
                    "Quantity": quantity
}
order_list = {"Item_name": menu_item_name, 
                                "Price": menu_item_price,
                                "Quantity": quantity }
order_list.append(order_item)

while True:
    keep_ordering = input("Would you like to keep ordering? (Y)es or (N)o ")
    while True:
        if keep_ordering == "N":
         place_order = False
    print("Keep Ordering Please. ") 

    break

print("This is what we are preparing for you.\n")

print("Item name                 | Price  | Quantity")
print("--------------------------|--------|----------")

for i in range(len(order)):
     menu_item_name = order[i]["Item name "]
     price = order[i]["Price "]
     num_item_spaces = 26 - len(menu_item_name)
num_price_spaces = 6 - len(str(price)) 
item_spaces = " " * num_item_spaces
price_spaces = " " * num_price_spaces
print(f"{menu_item_name}{item_spaces}|${price}{price_spaces}|{quantity}")


total_cost = sum([menu_items[price] * menu_items[quantity]
for item in order])
print(f"The total cost of your order is: ${total_cost: .2f}")