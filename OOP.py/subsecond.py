# static method is used when we want to do something  that should not be unique
# per instance
# class method is used when we want to do something  that should  be unique
# per instance
from second import Item


class Phone(Item):
    all = []
# super allows access to all attributes of the parent class

    def __init__(self, name: str, price: float, quantity=0, brokenPhone=0):
        # call to super function to have access to all attributes & methods
        super().__init__(
            name, price, quantity
        )
        assert price >= 0, f"Price {price} is not greater than or equal to zero"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero"
        assert brokenPhone >= 0, f"Broken Phone {brokenPhone} is not greater than or equal to zero"

        self.brokenPhone = brokenPhone
        # actions to execute
        Phone.all.append(self)


phone1 = Phone("Nokia", 200, 2, 1)
print(phone1.calculate_total_price())

print(Item.all)
print(Phone.all)
