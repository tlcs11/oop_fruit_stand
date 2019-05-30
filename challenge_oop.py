# Build a fruit stand that has a barrel for fruit and fruits have 
# a name and a price
# you shoudl be able to get the total cost of the barrel given the number of fruit in it
# abd their cost
# a barrel can only hold one fruit type

# Fruit obj      
 
"""
1 add to a barrel
2 get the type of fruit in a barrel
3 remove an amount from the barrel
4 reset the barrel, emptying it and setting the type to none
5 exit                                                            
"""
class Menu:
    def __init__(self):
            self.choice = {
            "1": self.add_qty,
            "2": self.type_fruit,
            "3": self.decrease_qty,
            "4": self.reset_barrel,
            "5": exit
        }

    def display_menu(self):
        print( 
"""
Fruit Barrel Menu:
1. Increase the qty
2. Name the type of fruit
3. Decrease the qty
4. Reset the Barrel to Zero
5. Exit
"""
        )

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter an option:  ")
            action = self.choice.get(choice)
            if action:
                action()
            else:
                print(f"{choice} is not a valid choice")

    def add_qty(self):
        message = input("Enter the qty to add to the barrel: ")
        self.add_qty(message)
        print("The qty has been added.")

    def type_fruit(self):
        message = input("Enter the type of fruit you would like: ")
        self.type_fruit(message)
        print("This is the requested fruit.")

    def decrease_qty(self):
            message = input("Enter the qty to decrease from the barrel: ")
            self.add_qty(message)
            print("The qty has been added.")

    
    def update_note(self):
        note_id = input("Enter a note id: ")
        message = input("Enter a message: ")
        if message:
            result = self.notebook.update_message(note_id, message)
        if result == False:
            print("Failed to update note.")
        else:
            print("Note Updated")



class Fruit:
    def fruit(self, name, price):
        self.name = name
        self.price = price

# Barrel obj

class Barrel:
    def __init__(self):
        self.fruit_count = 0
        self.fruit_type = None

    def sum_total (self):
        return self.fruit_count *self.fruit_type.price

    def add_fruit(self,fruit):
        if self.fruit_type == fruit.name:
            self.fruit_count += 1
        elif self.fruit_type == None:
            self.fruit_type = fruit
            self.fruit_count += 1
        else:
            return "Invalid barrel for that fruit"

apple = Fruit("Apple", 1.2)

apple_barrel = Barrel()

apple_barrel.add_fruit (apple)
print(apple_barrel.sum_total())


"""
Make a menu class that asks a user if they want to do:
1 add to a barrel
2 get the type of fruit in a barrel
3 remove an amount from the barrel
4 reset the barrel, emptying it an dsettin gthe type to none
5 exit

ALSO Make the needed barrel methods
DUE: Start of class tomorrow
"""




