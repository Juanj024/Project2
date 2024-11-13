from Beverage import BeverageDrink

menuItems = []
sprite = BeverageDrink("Sprite", 3.00,1)
menuItems.append(sprite)
milk = BeverageDrink("Milk", 5.00, 2)
menuItems.append(milk)
monster = BeverageDrink("Monster", 10.00, 3)
menuItems.append(monster)
redbull = BeverageDrink("Red Bull", 7.50, 4)
menuItems.append(redbull)
tea = BeverageDrink("Tea", 4.00, 5)
menuItems.append(tea)
water = BeverageDrink("Water", 1.99, 6)
menuItems.append(water)

class VendingMachine:
    def __init__(self, listItems):
        self.items = listItems
        self.money = 0
        self.choice = 0
        self.change = 0

    def showMenu(self):
        return (f"1. {sprite.name}    => ${sprite.price}\n"
                f"2. {milk.name}      => ${milk.price}\n"
                f"3. {monster.name}   => ${monster.price}\n"
                f"4. {redbull.name}  => ${redbull.price}\n"
                f"5. {tea.name}       => ${tea.price}\n"
                f"6. {water.name}     => ${water.price}\n")

#reconizing which item the user pick depending on the number
    def inputs(self):
        self.choice = int(input("Select a number from the machine "))
        while self.choice > len(menuItems):
            self.choice = int(input("Select a number from the machine "))
        if self.choice == sprite.place:
            self.items = sprite
        elif self.choice == milk.place:
            self.items = milk
        elif self.choice == monster.place:
            self.items = monster
        elif self.choice == redbull.place:
            self.items = redbull
        elif self.choice == tea.place:
            self.items = tea
        elif self.choice == water.place:
            self.items = water

#asking for money and making sure is enough and the change or amount due depending on the choice already made
    def insertMoney(self):
        self.money = float(input("Enter money for the item you selected "))
        if self.money >= self.items.price:
            self.change = self.money - self.items.price
            round(self.change, 2)
            return print(f"Thank you! here is your {self.items.name} *🍾* your change is ${self.change}")
        else:
            self.change = self.items.price - self.money
            round(self.change,2)
            return print(f"Sorry the money inserted is not enough, you need ${self.change} more!!!")




power = True
while power is True:
    machine = VendingMachine(menuItems)
    menu = machine.showMenu()
    print()
    print(menu)
    print()
    machine.inputs()
    machine.insertMoney()