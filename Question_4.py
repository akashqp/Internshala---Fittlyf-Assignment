def tuple_immutability_check():
    """
    Showing Immutability of Tuple
    Immutable means unchanging over time or unable to be changed
    In Python, Immutability means that the value of an object cannot be changed once
    it is assigned some value. The value of the object becomes permanent once created.
    Even when passed to a function a copy of the immutable object is passed keeping the
    original same.
    """

    tup = (1, 2, 3, 4, 5)   # Arbitrary Tuple
    try:
        tup[2] = 9              # Changing the value of one of the elements of tuple
    except TypeError:           # Execute this block if TypeError is encountered
        print(" Tuple is of immutable type\n It's value can't be changed\n It doesn't support item assignment")


if __name__ == '__main__':
    tuple_immutability_check()