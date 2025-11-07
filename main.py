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


def menu_category(menus):
    print("""
===========================================
| Welcome To The Milion Bean Cafe n Resto |
|       Please Choose The Category        |
        """)
    for list in menus:
        print(f"|{list:^40} |")
    print("===========================================")


# menu_category(menus)

def sub_menu_category(menus, cat_menu):
    if cat_menu == "FOOD":
        name = "FOOD"
        print("======================")
        print(f"|{name:^20}|")
        print("======================")
        for key, value in menus["FOOD"].items():
            print(f"|{key:^20}|")
        print("======================")
    elif cat_menu == "BEVERAGE":
        name = "BEVERAGE"
        print("======================")
        print(f"|{name:^20}|")
        print("======================")
        for key, value in menus["BEVERAGE"].items():
            print(f"|{key:^20}|")
        print("======================")
    elif cat_menu == "DESSERT":
        name = "DESSERT"
        print("===========================")
        print(f"|{name:^25}|")
        print("===========================")
        for list in menus["DESSERT"]:
            print(f"|{list:^25}|")
        print("===========================")
    else:
        print("The Menu is Not Valid")


sub_menu_category(menus, "FOOD")
sub_menu_category(menus, "BEVERAGE")
sub_menu_category(menus, "DESSERT")