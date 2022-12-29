def frozen_set():
    """
    Doing Operations on Frozen Sets
    """

    frozen_set_1 = frozenset(('A', 'B', 'C', 'D'))   # Creating an arbitrary frozen set
    frozen_set_2 = frozenset(('A', 2, 'C', 4))       # Creating another arbitrary frozen set

    # Frozen Set Operations
    frozenset_union = frozen_set_1.union(frozen_set_2)                      # Combined Frozen Set
    frozenset_common = frozen_set_1.intersection(frozen_set_2)              # Common elements b/w 2 frozen sets
    frozenset_difference = frozen_set_1.difference(frozen_set_2)            # Elements in Frozen Set 1 and not in 2
    frozenset_distinct = frozen_set_1.symmetric_difference(frozen_set_2)    # Elements Distinct to Frozen Set 1 and 2

    # Displaying all the Frozen Sets
    print("frozen_set_1: %s" % frozen_set_1)
    print("frozen_set_2: %s" % frozen_set_2)
    print("frozenset_union: %s" % frozenset_union)
    print("frozenset_common: %s" % frozenset_common)
    print("frozenset_difference: %s" % frozenset_difference)
    print("frozenset_distinct: %s" % frozenset_distinct)


if __name__ == '__main__':
    frozen_set()