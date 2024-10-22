class Coffee:
    def __str__(self):
        return "This is the worst coffee you ever tasted."


class Intern:
    # constructor
    def __init__(self, name="My name? I’m nobody, an intern, I have no name."):
        self.Name = name

    # returns the intern's name with str
    def __str__(self):
        return self.Name

    #  raises an exception
    def work(self):
        raise Exception("I’m just an intern, I can’t do that...")

    # creates and returns a Coffee instance
    def make_coffee(self):
        return Coffee()


def main():
    # Create first intern (without name)
    intern1 = Intern()
    print("First intern:", intern1)

    # Create second intern (Mark)
    intern2 = Intern("Mark")
    print("Second intern:", intern2)

    # Ask Mark to make coffee
    print("\nAsking Mark to make coffee...")
    coffee = intern2.make_coffee()
    print(coffee)

    # Ask the nameless intern to work
    print("\nAsking the first intern to work...")
    try:
        intern1.work()
    except Exception as e:
        print(f"Got an exception: {e}")


if __name__ == "__main__":
    main()
