import sys


def all_in(argv):
    states = {"Oregon": "OR", "Alabama": "AL", "New Jersey": "NJ", "Colorado": "CO"}
    capital_cities = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver",
    }

    # Create reverse lookup for capitals -> state abbreviations
    # abbrev is "OR" and city is "Salem", so it adds the entry "salem": "OR" to reverse_capitals
    reverse_capitals = {city.lower(): abbrev for abbrev, city in capital_cities.items()}

    # Normalize state names for case-insensitive lookup
    normalized_states = {state.lower(): abbrev for state, abbrev in states.items()}

    if ",," in argv:
        return

    # Split and clean input arguments, stripping spaces
    # This splits the input string argv at each comma and returns a list of strings
    inputs = [item.strip() for item in argv.split(",") if item.strip()]

    # item.strip
    # item is " Tren ton", then item.strip() will return "Tren ton"
    # if item.strip() -> exclude empty string in the final list

    for item in inputs:
        normalized_item = item.lower()  # Case-insensitive comparison

        # Check if input is a state (case-insensitive)
        if normalized_item in normalized_states:
            abbrev = normalized_states[normalized_item]
            print(f"{item} is a state, and its capital is {capital_cities[abbrev]}")

        # Check if input is a capital (case-insensitive)
        elif normalized_item in reverse_capitals:
            abbrev = reverse_capitals[normalized_item]
            state_name = [state for state, abbr in states.items() if abbr == abbrev][0]
            print(f"{item} is the capital of {state_name}")

        else:
            print(f"{item} is neither a capital city nor a state")


if __name__ == "__main__":
    if len(sys.argv) == 2:
        all_in(sys.argv[1])
