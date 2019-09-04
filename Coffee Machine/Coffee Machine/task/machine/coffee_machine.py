class CoffeeMachine:
    def __init__(self, water_amount, milk_amount, coffee_beans_amount, cups_amount, money):
        self.water = water_amount
        self.milk = milk_amount
        self.coffee = coffee_beans_amount
        self.cups = cups_amount
        self.money = money

    COFFEE_RECIPES = {  # water, milk, coffee, cost
        'espresso': {"water": 250, "milk": 0, "coffee": 16, "money": 4, "cups": 1},
        'latte': {"water": 350, "milk": 75, "coffee": 20, "money": 7, "cups": 1},
        'cappuccino': {"water": 200, "milk": 100, "coffee": 12, "money": 6, "cups": 1},
    }

    def make_coffee(self, coffee_type):
        """
        Makes coffee if possible, subtracts used resources from machine
        :param coffee_type:string
        """

    @staticmethod
    def init_machine():
        pass

    def print_current_machine_resources(self):
        print('The coffee machine has:')
        print(f'{self.water} of water')
        print(f'{self.milk} of milk')
        print(f'{self.coffee} of coffee beans')
        print(f'{self.cups} of disposable cups')
        print(f'{self.money} of money')

    def check_resources(self, coffee_type):
        resources_to_check = ['water', 'milk', 'coffee', 'money']
        for resource in resources_to_check:
            if self.resource < self.COFFEE_RECIPES[coffee_type][resource]:
                return False
