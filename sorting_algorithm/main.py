#!/usr/bin/python3

if __name__ == '__main__':
    import sorting
    import random
    from timeit import timeit

    # creating random lists for testing
    r = range(1000)
    list1 = [random.choice(r) for _ in range(100)]
    list2 = [random.choice(r) for _ in range(100)]
    list3 = [random.choice(r) for _ in range(100)]
    list4 = [random.choice(r) for _ in range(100)]
    
    # using my costum functions
    list1_sorted = 1
    list2_sorted = 2
    list3_sorted = 3
    list4_sorted = 4

    # see sorting result
    print(list1, list1_sorted)
    print(list2, list2_sorted)
    print(list3, list3_sorted)
    print(list4, list4_sorted)
