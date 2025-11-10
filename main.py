menus = {
    "FOOD": {
        "CHICKEN": {
            "Crispy Melted Chicken": 69000,
            "Garlic Chicken Steak": 59000,
            "Herb Butter Chicken": 75000,
            "Chicken Cordon Blue": 69000
        },
        "FISH": {
            "Fish and Chips": 69000,
            "Garlic Blackpaper Fish": 69000,
            "Sambal Matah Fish": 69000,
            "Creamy Salmon": 129000
        },
        "MEAT": {
            "Truffle Butter Medallion": 165000,
            "Beef Fondue": 159000,
            "Smoked Steak": 125000,
            "Truffle Steak": 125000
        }
    },
    "BEVERAGE": {
        "JUICE": {
            "Green Healty Juice": 35000,
            "Rainbow Juice": 38000,
            "Strowberry Smoothies": 38000
        },
        "MOCKTAIL": {
            "Ginger Marry Mojito": 38000,
            "Strowbarry Mojito": 38000,
            "Lychee Mojito": 38000
        },
        "COFFEE": {
            "Americano": 28000,
            "Cappucino": 35000,
            "Hot Latte": 30000,
            "Macadamia Brulee": 40000
        }
    },
    "DESSERT": {
        "Banana Split": 49000,
        "Dadar Gulung Pandan": 35000,
        "Banana Friters": 45000,
        "Lava Tiramisu Toast": 49000
    }
}

# function for displat menu category
def menu_category(menus):
    print('''
===========================================
| Welcome To The Milion Bean Cafe n Resto |
|       Please Choose The Category        |
===========================================
        '''.strip())
    for i, list in enumerate(menus):
        print(f"|{i+1}.{list:^38} |")
    print("===========================================")


# funcion of display sub menu
def sub_menu_category(num):
    if num == 1:
        name = "FOOD"
        x = 0
        print("========================")
        print(f"|{name:^22}|")
        print("========================")
        for key, value in menus["FOOD"].items():
            print(f"|{x + 1}.{key:^20}|")
            x += 1
        print("========================")
    elif num == 2:
        name = "BEVERAGE"
        x = 0
        print("========================")
        print(f"|{name:^22}|")
        print("========================")
        for key, value in menus["BEVERAGE"].items():
            print(f"|{x + 1}.{key:^20}|")
            x += 1
        print("========================")
    elif num == 3:
        lists_dessert_menu(num)
    else:
        print("The Menu is Not Valid")


# function for display Food menu
def lists_food_menu(num):
    if num == 1:
        food_menu = menus["FOOD"]["CHICKEN"]
        value = list(food_menu.items())
        print("=================================================")
        print(f"|{"CHICKEN":^47}|")
        print("=================================================")
        for i, (name, harga) in enumerate(value, start=1):
            print("|{}.{:^30} Rp. {:>10}|".format(i, name, harga))
        print("=================================================")
    elif num == 2:
        food_menu = menus["FOOD"]["FISH"]
        value = list(food_menu.items())
        print("=================================================")
        print(f"|{"FISH":^47}|")
        print("=================================================")
        for i, (name, harga) in enumerate(value, start=1):
            print("|{}.{:^30} Rp. {:>10}|".format(i, name, harga))
        print("=================================================")
    elif num == 3:
        food_menu = menus["FOOD"]["MEAT"]
        value = list(food_menu.items())
        print("=================================================")
        print(f"|{"MEAT":^47}|")
        print("=================================================")
        for i, (name, harga) in enumerate(value, start=1):
            print("|{}.{:^30} Rp. {:>10}|".format(i, name, harga))
        print("=================================================")
    else:
        print("The Number is Not Valid")


# function for display beverage menu
def lists_beverage_menu(num):
    if num == 1:
        beverage_menu = menus["BEVERAGE"]["JUICE"]
        value = list(beverage_menu.items())
        print("=================================================")
        print(f"|{"JUICE":^47}|")
        print("=================================================")
        for i, (name, harga) in enumerate(value, start=1):
            print("|{}.{:^30} Rp. {:>10}|".format(i, name, harga))
        print("=================================================")
    elif num == 2:
        beverage_menu = menus["BEVERAGE"]["MOCKTAIL"]
        value = list(beverage_menu.items())
        print("=================================================")
        print(f"|{"MOCKTAIL":^47}|")
        print("=================================================")
        for i, (name, harga) in enumerate(value, start=1):
            print("|{}.{:^30} Rp. {:>10}|".format(i, name, harga))
        print("=================================================")
    elif num == 3:
        beverage_menu = menus["BEVERAGE"]["COFFEE"]
        value = list(beverage_menu.items())
        print("=================================================")
        print(f"|{"COFFEE":^47}|")
        print("=================================================")
        for i, (name, harga) in enumerate(value, start=1):
            print("|{}.{:^30} Rp. {:>10}|".format(i, name, harga))
        print("=================================================")
    else:
        print("The Number is Not Valid")


# function for display dessert menu
def lists_dessert_menu(num):
    if num == 3:
        dessesrt_menu = list(menus["DESSERT"].items())
        print("=================================================")
        print(f"|{"DESSERT":^47}|")
        print("=================================================")
        for i, (key, value) in enumerate(dessesrt_menu, start=1):
            print("|{}.{:^30} Rp. {:>10}|".format(i, key, value))
        print("=================================================")
    else:
        print("The Number is Not Valid")


menu_category(menus)

# list for holding the data
cart = []

input_menu_category = int(input("Please choise the category: "))
if input_menu_category == 1:
    sub_menu_category(input_menu_category)
    input_sub_menu = int(input("Please Choise the menu that you like: "))
    if input_sub_menu == 1:
        lists_food_menu(input_sub_menu)
        while True:
            items = list(menus["FOOD"]["CHICKEN"].items())
            add_cart = int(input("Please choise the menu that you prefer: "))-1
            selected_name, selected_price = items[add_cart]
            cart.append((selected_name, selected_price))
            print(cart)
            ext = input("Do you want to continue or not (y/n): ").lower()
            if ext == "y":
                break
    elif input_sub_menu == 2:
        lists_food_menu(input_sub_menu)
        while True:
            items = list(menus["FOOD"]["FISH"].items())
            add_cart = int(input("Please choise the menu that you prefer: "))-1
            selected_name, selected_price = items[add_cart]
            cart.append((selected_name, selected_price))
            print(cart)
            ext = input("Do you want to continue or not (y/n): ").lower()
            if ext == "y":
                break
    elif input_sub_menu == 3:
        lists_food_menu(input_sub_menu)
        while True:
            items = list(menus["FOOD"]["MEAT"].items())
            add_cart = int(input("Please choise the menu that you prefer: "))-1
            selected_name, selected_price = items[add_cart]
            cart.append((selected_name, selected_price))
            print(cart)
            ext = input("Do you want to continue or not (y/n): ").lower()
            if ext == "y":
                break
    else:
        print("Input is not valid")
elif input_menu_category == 2:
    sub_menu_category(input_menu_category)
    input_sub_menu = int(input("Please Choise the menu that you like: "))
    if input_sub_menu == 1:
        lists_beverage_menu(input_sub_menu)
        while True:
            items = list(menus["BEVERAGE"]["JUICE"].items())
            add_cart = int(input("Please choise the menu that you prefer: "))-1
            selected_name, selected_price = items[add_cart]
            cart.append((selected_name, selected_price))
            print(cart)
            ext = input("Do you want to continue or not (y/n): ").lower()
            if ext == "y":
                break
    elif input_sub_menu == 2:
        lists_beverage_menu(input_sub_menu)
        while True:
            items = list(menus["BEVERAGE"]["MOCKTAIL"].items())
            add_cart = int(input("Please choise the menu that you prefer: "))-1
            selected_name, selected_price = items[add_cart]
            cart.append((selected_name, selected_price))
            print(cart)
            ext = input("Do you want to continue or not (y/n): ").lower()
            if ext == "y":
                break
    elif input_sub_menu == 3:
        lists_beverage_menu(input_sub_menu)
        while True:
            items = list(menus["BEVERAGE"]["COFFEE"].items())
            add_cart = int(input("Please choise the menu that you prefer: "))-1
            selected_name, selected_price = items[add_cart]
            cart.append((selected_name, selected_price))
            print(cart)
            ext = input("Do you want to continue or not (y/n): ").lower()
            if ext == "y":
                break
    else:
        print("Input is not valid")
elif input_menu_category == 3:
    sub_menu_category(input_menu_category)
    while True:
        items = list(menus["DESSERT"].items())
        add_cart = int(input("Please choise the menu that you prefer: "))-1
        selected_name, selected_price = items[add_cart]
        cart.append((selected_name, selected_price))
        print(cart)
        ext = input("Do you want to continue or not (y/n): ").lower()
        if ext == "y":
            break
else:
    print("Input not valid")