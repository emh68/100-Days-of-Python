from data import MENU, resources


def process_payment():
    """Returns the total calculated from coins inserted"""
    print("Please insert coins.")
    total = float(input("How many quarters?: ")) * .25
    total += float(input("How many dimes?: ")) * .1
    total += float(input("How many nickels?: ")) * .05
    total += float(input("How many pennies?: ")) * .01
    return total


def is_sufficient_resources(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient"""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


profit = 0


def is_transaction_successful(money_received, drink_cost):
    """Return True when payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}. Enjoy!")


is_on = True
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_sufficient_resources(drink["ingredients"]):
            payment = process_payment()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])

