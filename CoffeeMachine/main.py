MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 15.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 20.0,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 25.0,
    }
}

resources = {
    "water": 900,
    "milk": 700,
    "coffee": 300,
}
profit = 0
password = "Admin"


# TODO: 1. Print the report of the coffee machine resources


# TODO: 2 coin processing system
def coin_processing():
    """Process the coins and returns the total calculation"""
    print("Please insert coins.")
    total = int(input("How many tens? (N$10): ")) * 10
    total += int(input("How manny fives? (N$5): ")) * 5
    total += int(input("How many ones? (N$1): ")) * 1
    total += int(input("How many 50 cents? (N$0.5): ")) * 0.5
    return total


def coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}, Enjoy.")


def successful_transaction(money_payed, drink_cost):
    if money_payed >= drink_cost:
        change = round(money_payed - drink_cost, 2)
        print(f"Here is N${change} change")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money returned.")
        return False


def sufficient_resources(order_ingredients):
    """Returns true if there is enough  resources and false if there isn't"""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


is_machine_on = True
while is_machine_on:
    order = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if order == "off":
        ps = input("Enter Password: ")
        if ps == password:
            is_machine_on = False
        else:
            print("Wrong Password")
            is_machine_on = True
    elif order == "report":
        ps = input("Enter Password: ")
        if ps == password:
            print(f"Water: {resources['water']}ml")
            print(f"Milk: {resources['milk']}ml")
            print(f"Coffee: {resources['coffee']}ml")
            print(f"Money: N${profit}")
        else:
            print("Wrong Password")
    else:
        drink = MENU[order]
        if sufficient_resources(drink['ingredients']):
            payment = coin_processing()
            if successful_transaction(payment, drink['cost']):
                coffee(order, drink['ingredients'])
