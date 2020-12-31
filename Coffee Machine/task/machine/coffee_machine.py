class CoffeeMachine:
    def __init__(self, water=400, milk=540, coffee_beans=120, disposable_cups=9, money=550):
        self.water = water
        self.milk = milk
        self.coffee_beans = coffee_beans
        self.disposable_cups = disposable_cups
        self.money = money

    def state(self):
        print("""The coffee machine has:
{} of water
{} of milk
{} of coffee beans
{} of disposable cups
${} of money""".format(self.water, self.milk, self.coffee_beans, self.disposable_cups, self.money))

    # noinspection PyGlobalUndefined
    def buy(self):
        global low_resource
        choice = input("\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n")
        if choice == "1":
            if not any(resource < 0 for resource in [self.water - 250, self.coffee_beans - 16,
                                                     self.disposable_cups - 1]):
                self.water = self.water - 250
                self.coffee_beans = self.coffee_beans - 16
                self.money = self.money + 4
                self.disposable_cups = self.disposable_cups - 1
                print("I have enough resources, making you a coffee!")
            else:
                if self.water - 250 < 0:
                    low_resource = "water"
                elif self.coffee_beans - 16 < 0:
                    low_resource = "coffee beans"
                elif self.disposable_cups - 1 < 0:
                    low_resource = "disposable cups"
                # noinspection PyUnboundLocalVariable
                print("Sorry, not enough {}".format(low_resource))
        elif choice == "2":
            if not any(resource < 0 for resource in [self.water - 350, self.milk - 75, self.coffee_beans - 20,
                                                     self.disposable_cups - 1]):
                self.water = self.water - 350
                self.milk = self.milk - 75
                self.coffee_beans = self.coffee_beans - 20
                self.money = self.money + 7
                self.disposable_cups = self.disposable_cups - 1
                print("I have enough resources, making you a coffee!")
            else:
                if self.water - 350 < 0:
                    low_resource = "water"
                elif self.milk - 75 < 0:
                    low_resource = "milk"
                elif self.coffee_beans - 20 < 0:
                    low_resource = "coffee beans"
                elif self.disposable_cups - 1 < 0:
                    low_resource = "disposable cups"
                print("Sorry, not enough {}".format(low_resource))
        elif choice == "3":
            if not any(resource < 0 for resource in [self.water - 200, self.milk - 100, self.coffee_beans - 12,
                                                     self.disposable_cups - 1]):
                self.water = self.water - 200
                self.milk = self.milk - 100
                self.coffee_beans = self.coffee_beans - 12
                self.money = self.money + 6
                self.disposable_cups = self.disposable_cups - 1
                print("I have enough resources, making you a coffee!")
            else:
                if self.water - 200 < 0:
                    low_resource = "water"
                elif self.milk - 100 < 0:
                    low_resource = "milk"
                elif self.coffee_beans - 12 < 0:
                    low_resource = "coffee beans"
                elif self.disposable_cups - 1 < 0:
                    low_resource = "disposable cups"
                print("Sorry, not enough {}".format(low_resource))

    def take(self):
        print("I gave you ${}".format(self.money))
        self.money = 0

    def fill(self):
        add_water = int(input("Write how many ml of water do you want to add:\n"))
        add_milk = int(input("Write how many ml of milk do you want to add:\n"))
        add_beans = int(input("Write how many grams of coffee beans do you want to add:\n"))
        add_cups = int(input("Write how many disposable cups of coffee do you want to add:\n"))

        self.water = self.water + add_water
        self.milk = self.milk + add_milk
        self.coffee_beans = self.coffee_beans + add_beans
        self.disposable_cups = self.disposable_cups + add_cups


office_machine = CoffeeMachine()

while True:
    action = input("\nWrite action (buy, fill, take, remaining, exit):\n")

    if action == "buy":
        office_machine.buy()
    elif action == "take":
        office_machine.take()
    elif action == "fill":
        office_machine.fill()
    elif action == "remaining":
        print()
        office_machine.state()
    elif action == "exit":
        break
