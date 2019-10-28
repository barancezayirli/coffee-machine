class CoffeeMachine:
    def __init__(self, water, milk, beans, cups, deposit):
        self.water = water
        self.milk = milk
        self.beans = beans
        self.cups = cups
        self.deposit = deposit

    def current_state(self):
        print()
        print("The coffee machine has:")
        print(self.water, "of water")
        print(self.milk, "of milk")
        print(self.beans, "of coffee beans")
        print(self.cups, "of disposable cups")
        if self.deposit > 0:
            print("${} of money".format(self.deposit))
        else:
            print("{} of money".format(self.deposit))
        print()

    def take(self):
        print("I gave you ${}".format(self.deposit))
        self.deposit = 0

    def fill(self):
        self.water += int(input("Write how many ml of water do you want to add: "))
        self.milk += int(input("Write how many ml of milk do you want to add: "))
        self.beans += int(input("Write how many grams of coffee beans do you want to add: "))
        self.cups += int(input("Write how many disposable cups of coffee do you want to add: "))

    def make_coffee(self, water_amount, milk_amount, bean_amount, price):
        not_enough = []
        if water_amount > self.water:
            not_enough.append("water")
        if milk_amount > self.milk:
            not_enough.append("milk")
        if bean_amount > self.beans:
            not_enough.append("coffee beans")
        if self.cups == 0:
            not_enough.append("cups")

        if len(not_enough) == 0:
            self.cups -= 1
            self.water -= water_amount
            self.milk -= milk_amount
            self.beans -= bean_amount
            self.deposit += price
            print("I have enough resources, making you a coffee!")
            print()
        else:
            print("Sorry, not enough", *not_enough)
            print()

    def buy(self, choice):
        if choice == "1":
            self.make_coffee(250, 0, 16, 4)
        elif choice == "2":
            self.make_coffee(350, 75, 20, 7)
        elif choice == "3":
            self.make_coffee(200, 100, 12, 6)


if __name__ == "__main__":
    coffee_machine = CoffeeMachine(400, 250, 120, 9, 550)
    userInput = input("Write action (buy, fill, take, remaining, exit): ")
    while userInput != "exit":
        if userInput == "take":
            coffee_machine.take()
        if userInput == "fill":
            coffee_machine.fill()
        if userInput == "remaining":
            coffee_machine.current_state()
        if userInput == "buy":
            user_selection = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main "
                                   "menu: ")
            if user_selection == "back":
                userInput = input("Write action (buy, fill, take, remaining, exit): ")
            else:
                coffee_machine.buy(user_selection)

        userInput = input("Write action (buy, fill, take, remaining, exit): ")


