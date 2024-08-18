MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def calculatecoin(quarters, dimes, nickles, pennies):
    sumcion = float(0.25 * float(quarters) + 0.1 * float(dimes) + 0.05 * float(nickles) + 0.01 * float(pennies))
    return sumcion


def checkresources(user):
    if user == "report":
        return False
    comparision = [key for key in MENU[user]["ingredients"]
                   if MENU[user]["ingredients"][key] > resources[key]
                   ]
    if not comparision:
        return True
    else:
        formaed_list = ','.join(map(str,comparision))
        print(f"Sorry there is not enough {formaed_list}.")

def coffeemachine():
    userchoice = input("What would you like? (espresso/latte/cappuccino):")

    if checkresources(userchoice):
        print("Please insert coins.")
        quarters = input("how many quarters?: ")
        dimes = input("how many dimes?: ")
        nickles = input("how many nickles?: ")
        pennies = input("how many pennies?: ")
        usercoin = float(calculatecoin(quarters, dimes, nickles, pennies))
        global profit

        if usercoin > MENU[userchoice]["cost"]:
            morattaokane = MENU[userchoice]['cost']
            profit += morattaokane
            print(f"Here is {float(usercoin) - MENU[userchoice]['cost']} in change.")
            print(f"Here is your {userchoice} ☕️. Enjoy!")
            for key in MENU[userchoice]["ingredients"]:
                resources[key] -= MENU[userchoice]["ingredients"][key]
            coffeemachine()
        else:
            print("Sorry that's not enough money. Money refunded.")
            coffeemachine()
    elif checkresources(userchoice) == False:
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
        coffeemachine()
    else:
        coffeemachine()

coffeemachine()