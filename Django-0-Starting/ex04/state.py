import sys


def capital_list(argv):
    states = {"Oregon": "OR", "Alabama": "AL", "New Jersey": "NJ", "Colorado": "CO"}
    capital_cities = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver",
    }

    # Create a dictionary mapping capital cities to states
    capitals_to_states = {
        city: state # then  key-value pair in the new dictionary
        for state, abbr in states.items() # iterates over the states
        for code, city in capital_cities.items() # nested loop that iterates over the capital_cities CODE: OR
        if abbr == code #if egal
    }

    if argv in capitals_to_states:
        print(capitals_to_states[argv])
    else:
        print("Unknown state")


if __name__ == "__main__":
    if len(sys.argv) == 2:
        capital_list(sys.argv[1])

# e.g #
# From states, it gets "Oregon" and "OR"
#From capital_cities, it finds "OR" and "Salem"
#It checks if "OR" (abbr) equals "OR" (code), which is true
#It then adds "Salem": "Oregon" to the capitals_to_states dictionary
