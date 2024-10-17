def my_var():
    variables = [
        42,
        "42",
        "quarante-deux",
        42.0,
        True,
        [42],
        {42: 42},
        (42,),
        set()
    ]

    for value in variables:
        print(f"{value} has a type {type(value)}")

if __name__ == "__main__":
    my_var()

#  "If I'm the main program being run, then do this stuff inside."