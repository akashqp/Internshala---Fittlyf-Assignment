# Base Exception Class
class Error(IndexError, ValueError):
    pass


# If the index is out of range
class IndexOutOfRangeError(Error):
    def __init__(self, index, start, end):
        self.index = int(index)
        self.start = start
        self.end = end
        # Combining the error message
        self.msg = "The index {} is incorrect and index should lie between {} and {}.".format(self.index, self.start,
                                                                                              self.end)


# If the Entered Index is Not Integer
class NonIntegerValueError(Error):
    def __init__(self):
        self.msg = "Use an Integer value as the input."

def main():
    try:
        list_a = [1, 2, 3, 4, 5]                # Take an arbitrary list
        start = -(len(list_a))                  # Starting negative index
        end = len(list_a) - 1                   # Ending Positive index
        index = input("Enter the index = ")     # Taking index as input from the user
        # Declaring objects of Custom Exception Classes
        error1 = NonIntegerValueError()
        error2 = IndexOutOfRangeError(index, start, end)
        # If the Index is not integer
        if not index.isdigit():
            raise NonIntegerValueError()
        # If the index is not in appropriate range
        elif int(index) > 4 and int(index) < -5:
            raise IndexOutOfRangeError(index, start, end)
        # Printing the Element is no Exception encountered
        print("Element at Index {} is {}".format(index, list_a[int(index)]))
    except IndexError:
        print(error2.msg)
    except ValueError:
        print(error1.msg)


if __name__ == '__main__':
    main()