def tuple_operations():
    """
    Doing some Tuple Operations
    """

    t_1 = (1, 4, 9, 16, 25, 36)
    t_modified = tuple([x**2 for x in t_1])     # Squaring each element of the tuple using list comprehension
                                                # and coverting it to tuple
    t_modified_4th_element = t_modified[4]      # Storing 4th element of the modified tuple
    t_sliced = t_modified[1:4]                  # Slicing the tuple to give 1st to 3rd elements of the tuple

    # Displaying all the Data
    print("t_1: %s" % (t_1,))
    print("t_modified: %s" % (t_modified,))
    print("Element at index position 4 of t_modified: %s" % (t_modified_4th_element,))
    print("t_sliced: %s" % (t_sliced, ))


if __name__ == '__main__':
    tuple_operations()
