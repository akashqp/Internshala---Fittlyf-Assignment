def main():
    """
    Function to elements containing 'a' 'A' in the list
    Also used filter function along with lambda function to remove the words
    """

    list_a = ["car", "place", "tree", "under", "grass", "price"]    # Arbitrary list
    remove_items_containing_a_or_A = list(filter(lambda word: 'a' not in word and 'A' not in word, list_a))
    print(remove_items_containing_a_or_A)


if __name__ == '__main__':
    main()