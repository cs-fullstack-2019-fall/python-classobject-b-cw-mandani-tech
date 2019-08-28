# # python-classObject_b-cw
# Start with a main function and make each problem a function. Call those functions from your main function.
# ### Problem 1:
# Create a class Dog. Make sure it has the attributes name, breed, color, gender.
# Create a function that will print all attributes of the class.
# Create an object of Dog in your problem1 function and print all of it's attributes.
def main():
    dogFunction()
    quittingFunction()
    productFunction()

class Dog:
    def __init__(self, name, breed, color, gender):  # initializing the template for Dog class
        self.name = name
        self.breed = breed
        self.color = color
        self.gender = gender
    def printAttributes(self):  # prints all the attributes
        print(f'{self.name}')
        print(f'{self.breed}')
        print(f'{self.color}')
        print(f'{self.gender}')
def dogFunction ():
    dog1 = Dog("Star", "Poodle", "Grey", "Female")  # creating an instance dog1
    dog1.printAttributes()  # printing all the attributes for dog1

# ### Problem 2:
# ##### We will keep having this problem until EVERYONE gets it right without help
# Create a function that has a loop that quits with the equal sign.
# If the user doesn't enter the equal sign, ask them to input another string.
def quittingFunction():
    usrInput = ""
    while (usrInput != 'q'):
        usrInput = input("Enter a string or 'q' to quit :  ") # !! : that quits with the equal sign

# ### Problem 3:
# Create a class Product that represents a product sold online.
# A product has a name, price, and quantity.
# The class should have several functions:
# a) One function that can change the name of the product.
# b) Another function that can change the name and price of the product.
# c) A last function that can change the name, price, and quantity of the product.
# Create an object of Product and print all of it's attributes.
def productFunction():
    class Product:
        def __init__(self, name, price, quantity):  # initializing the template for Dog class
            self.name = name
            self.price = price
            self.quantity = quantity
        def printAttributes(self):  # prints all the attributes
            print(f'\nProduct Name is {self.name}')
            print(f'Product price is {self.price}')
            print(f'Product quantity is {self.quantity}\n')
        def changeNameFunction(self, newName):
            self.name = newName
        def changeNamePriceFunction(self, newName, newPrice):
            self.name = newName
            self.price = newPrice
        def changeNamePriceQuantityFunction(self, newName, newPrice, newQuantity):
            self.name = newName
            self.price = newPrice
            self.quantity = newQuantity
    product1 = Product("lotion", 5.99, 1000)  # creating an instance dog1
    product1.printAttributes()  # printing all the attributes for dog1
    product1.changeNameFunction("Bagpack")
    product1.changeNamePriceFunction("Bagpack", 25)
    product1.changeNamePriceQuantityFunction("laptop", 550, 1)
    product1.printAttributes()

main()
