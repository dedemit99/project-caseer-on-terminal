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


def lists_food_menu(menus, sub_menu):
    if sub_menu == "CHICKEN":
        for key, value in menus["FOOD"].items():
            print("===============================================")
            print(f"|{key:^45}|")
            print("===============================================")
            for name, harga in value.items():
                print(f"|{name:^30} Rp. {harga:>10}|")
            print("===============================================")
    elif sub_menu == "FISH":
        for key, value in menus["FOOD"].items():
            print("===============================================")
            print(f"|{key:^45}|")
            print("===============================================")
            for name, harga in value.items():
                print(f"|{name:^30} Rp. {harga:>10}|")
            print("===============================================")
    elif sub_menu == "MEAT":
        for key, value in menus["FOOD"].items():
            print("===============================================")
            print(f"|{key:^45}|")
            print("===============================================")
            for name, harga in value.items():
                print(f"|{name:^30} Rp. {harga:>10}|")
            print("===============================================")
    else:
        print("The Number is Not Valid")


def lists_beverage_menu(menus, sub_menu):
    if sub_menu == "JUICE":
        for key, value in menus["BEVERAGE"].items():
            print("===============================================")
            print(f"|{key:^45}|")
            print("===============================================")
            for name, harga in value.items():
                print(f"|{name:^30} Rp. {harga:>10}|")
            print("===============================================")
    elif sub_menu == "MOCKTAIL":
        for key, value in menus["BEVERAGE"].items():
            print("===============================================")
            print(f"|{key:^45}|")
            print("===============================================")
            for name, harga in value.items():
                print(f"|{name:^30} Rp. {harga:>10}|")
            print("===============================================")
    elif sub_menu == "COFFEE":
        for key, value in menus["BEVERAGE"].items():
            print("===============================================")
            print(f"|{key:^45}|")
            print("===============================================")
            for name, harga in value.items():
                print(f"|{name:^30} Rp. {harga:>10}|")
            print("===============================================")
    else:
        print("The Number is Not Valid")


def lists_dessert_menu(menus, sub_menu):
    if sub_menu == "DESSERT":
        print("===============================================")
        print(f"|{sub_menu:^45}|")
        print("===============================================")
        for key, value in menus["DESSERT"].items():
            print(f"|{key:^30} Rp. {value:>10}|")
        print("===============================================")
    else:
        print("The Number is Not Valid")


# menu_category(menus)
# sub_menu_category(menus, "FOOD")
lists_food_menu(menus, "CHICKEN")
# lists_beverage_menu(menus, "JUICE")
# lists_dessert_menu(menus, "DESSERT")