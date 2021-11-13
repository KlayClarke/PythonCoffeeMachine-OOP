from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

items = Menu()
coffee_machine = CoffeeMaker()
register = MoneyMachine()

machine_on = True

while machine_on:
    #ask the user what they would like to drink...
    user_input = input('what would you like? espresso, latte, cappuccino?').lower()
    # if the user types 'off'
    if user_input == 'off':
        # turn machine off
        machine_on = False
    # if the user types 'report'
    elif user_input == 'report':
        # print a report of machine resources and profit
        coffee_machine.report()
        register.report()
    # find whether the drink is in the menu
    elif items.find_drink(user_input):
        #create variable for drink if it is in menu
        drink_order = items.find_drink(user_input)
        #if the resources are sufficient to make said drink...
        if coffee_machine.is_resource_sufficient(drink_order):
            print('resources sufficient')


# TODO: if resources are sufficient, process coins - if not, deal refund
# TODO: check if transaction is successful -
# TODO: if user payment is sufficient, brew drink and deduct resources from coffee machine.. add profit to money machine
# - else, deal refund
