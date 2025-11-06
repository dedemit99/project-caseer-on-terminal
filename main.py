menus = ["Food", "Beverage", "Dessert"]
food_menu = ["Chicken", "Fish", "Meat"]
beverage_menu = ["Juice", "Mocktail", "Coffee"]
dessert_menu = ["Banana Split", "Strowberry Pancake", "Es Goyobod"]
fish_menu = [
    "Fish and Chips",
    "Garlic Blackpepper Fish",
    "Sambal Matah Fish",
    "Creamy Salmon"
]
chicken_menu = [
    "Crispy Melted Chicken",
    "Garlic Chicken Steak",
    "Herb Butter Chicken",
    "Chicken Cordon Blue"
    ]
meat_menu = [
    "Truffle Butter Medalion",
    "Beed Fondue",
    "Smoke Steak",
    "DP Steak"
    ]


def print_menu(menu):
    for item in menu:
        print(f"""
            ====MENU ======
                    {item}
                    {item}
                    {item}
            ==================
            """)


print_menu(menus)