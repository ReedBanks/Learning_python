import csv

# class methods


class Item:
    # class attribute
    pay_rate = 0.8
    all = []  # creating array to store instances
# magic method _repr_ =representing your objs

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}',' {self.price}', '{self.quantity}')"

    def calculate_total_price(self):
        return self.price*self.quantity
    # constructors

    def apply_apply_discount(self):

        self.price = self.price*self.pay_rate

    def __init__(self, name: str, price: float, quantity=0) -> None:

        assert price >= 0, f"Price {price} is not greater than or equal to zero"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero"

        # assigning to self obj
        # double underscore =>private attribute
        self.__name = name
        self.price = price
        self.quantity = quantity
        # actions to execute
        Item.all.append(self)
# making the name read_only
    # @property decorator=read-only attribute

    @property
    def name(self):
        return self.__name
       # class method=can be accessed by the class only
    # method to instantiate from csv file
    # decorator =a way of calling the function be4 its creation

    @classmethod  # this makes the function a class method,the class is passed as an argument
    def instantiate_from_csv(cls):
        with open("C:\\Users\\rexxs\\Desktop\\PROJECT_FILES\\python\\learn\\OOP.py\\items.csv", "r") as objread:
            # converts file into .py dictionary
            reader = csv.DictReader(objread)
            items = list(reader)  # converting into a list

        for item in items:
            # print(item)
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity')),
            )
        # static method
# behaves like a regular function

    @staticmethod
    def is_integer(number):
        if isinstance(number, float):
            return number.is_integer()
        elif isinstance(number, int):
            return True
        else:
            return False
    # getters and setters

    @name.setter
    def setName(self, name):
        self.__name = name
        return self.__name

    # @property
    # def read_only_name(self):
    #     return "AAAA"

# we pass file for instatiation
# Item.instantiate_from_csv()

# print(Item.is_integer(7.65))
# printing instances
# print(Item.all)

# loop to print instances
# for instance in Item.all:
#     print(instance)

# CSV=Comma Seperated Value
# inheritance
