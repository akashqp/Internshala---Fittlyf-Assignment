def pattern1():
    """
    Function for displaying Pattern:
    * * * * *
     * * * *
      * * *
       * *
        *
    """

    for i in range(5, 0, -1):         # Outer loop for the number of rows
        for j in range(5, i, -1):     # Inner loop for Printing the spaces
            print(' ', end='')
        for j in range(i):          # Inner loop for Printing the Printing each row
            print('*', end=' ')
        print()                     # Print statement for changing to new line


def pattern2():
    """
    Function for displaying Pattern:
       _ _
      _ _ _
     _ _ _ _
    _ _ _ _ _

    """

    for i in range(1, 5):            # Outer loop for the number of rows
        for j in range(5-i-1):      # Inner loop for Printing the spaces
            print(' ', end='')
        for j in range(i+1):        # Inner loop for Printing the Printing each row
            print('_', end=' ')
        print()                     # Print statement for changing to new line


if __name__ == '__main__':
    ch = int(input("Enter choice: "))   # Asking the user for the choice
    if ch == 1:
        pattern1()                  # Calling Function pattern1 if choice is 1
    elif ch == 2:
        pattern1()                  # Calling function pattern1 and pattern2 if choice is 2
        pattern2()
    else:
        print("Invalid Input")      # Printing 'Invalid Input' if choice is other than 1 or 2
