# Day 15: Make a Coffee Machine!
from menu import MENU, resources

money = 0
profit = 0


def report_resources():
    """Print resources in coffee machine"""
    print(f"water: {resources['water']}ml")
    print(f"milk: {resources['milk']}ml")
    print(f"coffee: {resources['coffee']}g")
    print(f"money: ${money}")


def insert_coin():
    """Returns the total calculated from coins inserted."""
    print(f"Please insert coins. ${money}")
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickles = int(input("How many nickles? "))
    pennies = int(input("How many pennies? "))
    total = round(quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01, 2)
    return total


def is_resource_sufficient(ingredients_in_drink):
    """Returns true when order can be made, False if ingredients are insufficient."""
    for item in ingredients_in_drink:
        if resources[item] < ingredients_in_drink[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True


def is_transaction_successful(money_received, drink_costs):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if money_received >= drink_costs:
        global money, profit
        profit += drink_costs
        money = round(money_received - drink_costs, 2)
        print(f"I got ${money_received} now, and it's ${money} in total.")
        return True
    else:
        print(f"Sorry, that's not enough money. ${money} is refunded.")
        money = 0
        return False


def make_drink(drink_name, drink_ordered):
    """Deduct the required ingredients from the resources."""
    ingredients_in_drink = drink_ordered['ingredients']
    for item in ingredients_in_drink:
        resources[item] -= ingredients_in_drink[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino/off): ").lower()
    if choice == "off":
        is_on = False
        print(f"Here is your change ${money}")
    elif choice == "report":
        report_resources()
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink['ingredients']):
            money += insert_coin()
            if is_transaction_successful(money, drink['cost']):
                make_drink(choice, drink)
    print("")
