def main():
    x = 5
    y = x
    z = "Sujon"
    print(x)
    print(y)
    print(z)

    # Many values to multiple variables
    a, b, c = "Oranges", "Bananas", "Apples"
    print(a)
    print(b)
    print(c)

    # One value to multiple variable
    x = y = z = "Oranges"
    print(x)
    print(y)
    print(z)

    # Unpack collection list (Mutable)
    fruits = ["apple", "banana", "cherry"]
    x, y, z = fruits
    print(x)
    print(y)
    print(z)
    print(type(fruits))

    # Unpack collection tuple (Immutable)
    numbers = (100, 200, 300)
    x, y, z = numbers
    print(x)
    print(y)
    print(z)
    print(x, y, z)
    print(numbers)
    print(type(numbers))


#Global Variable
d = "Awesome"


def my_function():
    print(d)


if __name__ == "__main__":
    main()
    my_function()
