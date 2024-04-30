# creating data types of our own
#pascal_naming format

class Item:
    # class attribute
    pay_rate = 0.8  # pay rate aft 20% discount

    # pass indicates that the class is empty
    # pass
    # python assigns one argument to every method =>the obj

    def calculate_total_price(self):
        return self.price*self.quantity
    # constructors

    def apply_apply_discount(self):
        # pay_rate can't be accessed bcos is a class attribute
        # hence it can only be accessed by the class
        # self.price = self.price*Item.pay_rate
        self.price = self.price*self.pay_rate

    def __init__(self, name: str, price: float, quantity=0) -> None:
        # print(f"obj created for : {name} {price} {quantity}")
        # assert is used to check for match
        # run validation
        assert price >= 0, f"Price {price} is not greater than or equal to zero"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero"

        # assigning to self obj
        self.name = name
        self.price = price
        self.quantity = quantity


item1 = Item(5, 1000, 2) #creating an object of class Item
item1.apply_apply_discount()
print("i1 ", item1.price)
# item1.price = 100
# item1.quantity = 5
# print(item1.calculate_total_price(item1.price, item1.quantity))
# print(item1.name)

item2 = Item("Laptop", 5000, 3)
# apply discount
item2.pay_rate = 0.7
item2.apply_apply_discount()

print("i2 ", item2.price)

# display all attributes of this class
# print(Item.__dict__, "\n")
# print(item1.__dict__)
# print(Item.pay_rate)
# item2.has_numpad=True
# item2.price = 800
# item2.quantiy = 20
# print(item2.calculate_total_price(item2.price, item2.quantity))
# print(item2.name)
