def my_sort():
    d = {
        "Hendrix": "1942",
        "Allman": "1946",
        "King": "1925",
        "Clapton": "1945",
        "Johnson": "1911",
        "Berry": "1926",
        "Vaughan": "1954",
        "Cooder": "1947",
        "Page": "1944",
        "Richards": "1943",
        "Hammett": "1962",
        "Cobain": "1967",
        "Garcia": "1942",
        "Beck": "1944",
        "Santana": "1947",
        "Ramone": "1948",
        "White": "1975",
        "Frusciante": "1970",
        "Thompson": "1949",
        "Burton": "1939",
    }

    def sort_key(item):  # define how the items in the dictionary will be sorted
        name, year = item
        return (int(year), name)

    # name is included in the return so that in case two people have the same year, their names will be sorted alphabetically

    # Sort the dictionary items by year, then by name
    sorted_musicians = sorted(d.items(), key=sort_key)
    # pass sort_key as the key parameter without parentheses. This passes the function itself, not its result

    # Print the sorted names without the year
    for name, _ in sorted_musicians:
        print(name)


if __name__ == "__main__":
    my_sort()
