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
    if num == "1":
        name = "FOOD"
        x = 0
        print("========================")
        print(f"|{name:^22}|")
        print("========================")
        for key, value in menus["FOOD"].items():
            print(f"|{x + 1}.{key:^20}|")
            x += 1
        print("========================")
    elif num == "2":
        name = "BEVERAGE"
        x = 0
        print("========================")
        print(f"|{name:^22}|")
        print("========================")
        for key, value in menus["BEVERAGE"].items():
            print(f"|{x + 1}.{key:^20}|")
            x += 1
        print("========================")
    elif num == "3":
        lists_dessert_menu(num)
    else:
        print("The Menu is Not Valid")


# function for display Food menu
def lists_food_menu(num):
    food_menu = menus["FOOD"]
    if num == "1":
        if "CHICKEN" in food_menu:
            value = food_menu["CHICKEN"]
            x = 0
            print("=================================================")
            print(f"|{"CHICKEN":^47}|")
            print("=================================================")
            for name, harga in value.items():
                print(f"|{x + 1}.{name:^30} Rp. {harga:>10}|")
                x += 1
            print("=================================================")
    elif num == "2":
        if "FISH" in food_menu:
            value = food_menu["FISH"]
            x = 0
            print("=================================================")
            print(f"|{"FISH":^47}|")
            print("=================================================")
            for name, harga in value.items():
                print(f"|{x + 1}.{name:^30} Rp. {harga:>10}|")
                x += 1
            print("=================================================")
    elif num == "3":
        if "MEAT" in food_menu:
            value = food_menu["MEAT"]
            x = 0
            print("=================================================")
            print(f"|{"MEAT":^47}|")
            print("=================================================")
            for name, harga in value.items():
                print(f"|{x + 1}.{name:^30} Rp. {harga:>10}|")
                x += 1
            print("=================================================")
    else:
        print("The Number is Not Valid")


# function for display beverage menu
def lists_beverage_menu(num):
    beverage_menu = menus["BEVERAGE"]
    if num == "1":
        if "JUICE" in beverage_menu:
            value = beverage_menu["JUICE"]
            x = 0
            print("=================================================")
            print(f"|{"JUICE":^47}|")
            print("=================================================")
            for name, harga in value.items():
                print(f"|{x + 1}.{name:^30} Rp. {harga:>10}|")
                x += 1
            print("=================================================")
    elif num == "2":
        if "MOCKTAIL" in beverage_menu:
            value = beverage_menu["MOCKTAIL"]
            x = 0
            print("=================================================")
            print(f"|{"MOCKTAIL":^47}|")
            print("=================================================")
            for name, harga in value.items():
                print(f"|{x + 1}.{name:^30} Rp. {harga:>10}|")
                x += 1
            print("=================================================")
    elif num == "3":
        if "COFFEE" in beverage_menu:
            value = beverage_menu["COFFEE"]
            x = 0
            print("=================================================")
            print(f"|{"COFFEE":^47}|")
            print("=================================================")
            for name, harga in value.items():
                print(f"|{x + 1}.{name:^30} Rp. {harga:>10}|")
                x += 1
            print("=================================================")
    else:
        print("The Number is Not Valid")


# function for display dessert menu
def lists_dessert_menu(num):
    if num == "3":
        x = 0
        print("=================================================")
        print(f"|{"DESSERT":^47}|")
        print("=================================================")
        for key, value in menus["DESSERT"].items():
            print(f"|{x + 1}.{key:^30} Rp. {value:>10}|")
            x += 1
        print("=================================================")
    else:
        print("The Number is Not Valid")


menu_category(menus)
input_menu_category = input("Please choise the category: ")
if input_menu_category == "1":
    sub_menu_category(input_menu_category)
    input_sub_menu = input("Please Choise the menu that you like: ")
    if input_sub_menu == "1":
        lists_food_menu(input_sub_menu)
    elif input_sub_menu == "2":
        lists_food_menu(input_sub_menu)
    elif input_sub_menu == "3":
        lists_food_menu(input_sub_menu)
    else:
        print("Input is not valid")
elif input_menu_category == "2":
    sub_menu_category(input_menu_category)
    input_sub_menu = input("Please Choise the menu that you like: ")
    if input_sub_menu == "1":
        lists_beverage_menu(input_sub_menu)
    elif input_sub_menu == "2":
        lists_beverage_menu(input_sub_menu)
    elif input_sub_menu == "3":
        lists_beverage_menu(input_sub_menu)
    else:
        print("Input is not valid")
elif input_menu_category == "3":
    sub_menu_category(input_menu_category)
    input_sub_menu = input("Please Choise the menu that you like: ")
else:
    print("Input not valid")