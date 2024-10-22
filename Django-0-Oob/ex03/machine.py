import random
from beverages import HotBeverage, Coffee, Tea, Chocolate, Cappuccino


class CoffeeMachine:
    class EmptyCup(HotBeverage):
        def __init__(self):
            self.name = "empty cup"
            self.price = 0.90

        def description(self):
            return "An empty cup?! Gimme my money back!"

    class BrokenMachineException(Exception):
        def __init__(self):
            super().__init__("This coffee machine has to be repaired.")

    def __init__(self):
        self.drinks_served = 0

    def repair(self):
        self.drinks_served = 0

    def serve(self, drink_class):
        if self.drinks_served >= 10:
            raise self.BrokenMachineException()

        self.drinks_served += 1
        if random.randint(0, 1):
            return drink_class()
        return self.EmptyCup()


def test():
    machine = CoffeeMachine()
    drinks = [Coffee, Tea, Cappuccino, Chocolate]

    # Test for two cycles
    for cycle in range(2):
        print(f"\n=== Starting cycle {cycle + 1} ===")
        while True:
            try:
                drink_type = random.choice(drinks)
                print(f"\nTrying to serve {drink_type.__name__}...")
                print(machine.serve(drink_type))
            except machine.BrokenMachineException as e:
                print(f"\n{e}")
                print("\n---- method repair called ----\n")
                machine.repair()
                break


if __name__ == "__main__":
    test()
