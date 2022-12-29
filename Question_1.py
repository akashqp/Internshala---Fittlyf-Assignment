def sequence():
    """
    Function for squaring each element in a list and printing them
    """

    A = [1, 2, 3, 4, 5, 6]      # Sample List
    for i in range(len(A)):     # 'for' loop to traverse the List
        A[i] = A[i]**2          # Squaring each element of the list
    for a in A:                 # Printing the New list
        print(a)

    print("The sequence has ended")     # Showing that the sequence has ended


if __name__ == '__main__':
    sequence()
