class HotBeverage:
    def __init__(self):
        self.price = 0.30
        self.name = "HotBeverage"

    def description(self):
        return "Just some hot water in a cup."

    def __str__(self):
        return (
            f"name : {self.name}\n"
            f"price: {self.price:.2f}\n"
            f"description: {self.description()}"
            f"\n--------------------------------\n"
        )


class Coffee(HotBeverage):
    def __init__(self):
        super().__init__()  # Call parent's __init__ , initialize the parent class
        self.name = "Coffee"
        self.price = 0.40

    def description(self):
        return "A coffee, to stay awake."


class Tea(HotBeverage):
    def __init__(self):
        super().__init__()
        self.name = "Tea"
        self.price = 0.30


class Chocolate(HotBeverage):
    def __init__(self):
        super().__init__()
        self.name = "Chocolate"
        self.price = 0.50

    def description(self):
        return "Chocolate, sweet chocolate..."


class Cappuccino(HotBeverage):
    def __init__(self):
        super().__init__()
        self.name = "Cappuccino"
        self.price = 0.45

    def description(self):
        return "Un po' di Italia nella sua tazza!"


def drinks():
    print(HotBeverage())
    print(Coffee())
    print(Tea())
    print(Chocolate())
    print(Cappuccino())


if __name__ == "__main__":
    drinks()
