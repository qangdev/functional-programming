#
# C H A P T E R  1
# ------------------------
# F L O W  C O N T R O L
#

if __name__ == '__main__':
    # I.   Pure function: Does not change the input and return new output
    def pure(alist):
        '''This function dose not change the input list but return a new list '''
        newlist = []
        for i in alist:
            newlist.append(i ** 2)
        return newlist
    # e.g
    input_list = [1, 3, 5, 7]
    new_list = pure(input_list)
    assert input_list != new_list
    print("*" * 30)

    # II.  Recursion: Replacement of `for` or `while` loop
    def sum(l, i):
        '''This function call it self to find the sum of a list of number'''
        count = 0
        # Stopping point
        if len(l) <= i:
            return count
        # Increase count
        count += l[i]
        # going into the recursion
        count += sum(l, i + 1)
        return count
    # e.g
    l = [1,2,3,4,5]
    count = 0
    n = len(l)
    print(sum(l, 0))
    print("*" * 30)

    # III. Function are First-Class and can be High-Other: functions are stored in data structure and passed as arguments
    #      - First Class function characteristics:
    #          1. A function is an instance of the Object Type
    #          2. Can be stored in a variable
    #          3. Can be passed as an argument to another function
    #          4. Can return the function from a function
    #          5. Can be stored in data structures such as hash table, list, etc
    def addiation(n):
        return n + n

    def call_map():
        numbers = [1, 2, 3, 4, 5]
        dbl_numbers = map(addiation, numbers)
        return dbl_numbers

    def call_map_lambda():
        numbers = [1, 2, 3, 4, 5]
        dbl_numbers = map(lambda x: x + x, numbers)
        return dbl_numbers

    def filter_letter(l):
        allow_letters = ["a", "e", "o", "u", "i"]
        return l in allow_letters

    def call_filter():
        seq = ['g', 'e', 'e', 'j', 'k', 's', 'p', 'r']
        filtered = filter(filter_letter, seq)
        return filtered

    def call_filter_lambda():
        allow_letters = ["a", "e", "o", "u", "i"]
        seq = ['g', 'e', 'e', 'j', 'k', 's', 'p', 'r']
        filtered = filter(lambda x: x in allow_letters, seq)
        return filtered

    call_lambda = lambda x: x ** 2  # Anonimous function


    # e.g
    print(list(call_map()))
    print(list(call_map_lambda()))
    print("*" * 30)

    print(list(call_filter()))
    print(list(call_filter_lambda()))
    print("*" * 30)

    print(call_lambda(13))

    #      - High Order function characteristics:
    #          1. Make the processing iterable objects and iterator much easier
    #          2. Python built-in like: Map, Reduce, Filter
    #          3. Lambda (Anonymous function. Function without a name)
    #               3.1. Function can have any number of argument but have only one expression
    def shout(text):
        return text.upper()

    def whisper(text):
        return text.lower()

    def say_greeting(func):
        greeting = func("greeting")
        return greeting
    # e.g
    print("S H O U T I N G:>", say_greeting(shout))
    print("w h i s p e r i n g:>", say_greeting(whisper))
    print("*" * 30)

    # IV.  Variables are immutable

    # F L O W  C O N T R O L
    #   1. Encapsulation: Focusing more on `What` than `How` by wrapping logic into a function
    #       1.1. Comprehensions: Helping Encapsulation by making code compact
    #           1.1.1. List comprehension
    my_list = [i if i % 3 == 0 else None for i in range(1, 11)]
    my_list = [i for i in my_list if i]
    print(my_list)
    #           1.1.2. Dict and Set comprehension
    my_dict = {i:chr(i+65) for i in range(6)}
    print(my_dict)
    my_set = {chr(i+65) for i in my_dict}
    print(my_set)
    print("*" * 30)
    #           1.1.3. Generator comprehension
    #   2. Recursion: Partition a problem into smaller problems and each approached in a similar way
    def factorialR(N):
        # recursive factorial function
        assert isinstance(N, int) and N >= 1
        return 1 if N <= 1 else N * factorialR(N - 1)

    def factorialI(N):
        # recursive factorial function
        assert isinstance(N, int) and N >= 1
        product = 1
        while N >= 1:
            product *= N
            N -= 1
        return product

    def factorialHOF(N):
        from functools import reduce
        from operator import mul
        return reduce(mul, range(1, N+1), 1)

    def quicksort(lst):
        # Quicksort
        if len(lst) == 0:
            return lst
        pivot = lst[0]
        pivots = [x for x in lst if x == pivot]
        small = quicksort([x for x in lst if x < pivot])
        large = quicksort([x for x in lst if x > pivot])
        print(pivot, small, pivots, large)
        return small + pivots + large

    lst = [3, 5, 1, 6, 1]
    print("quickshort:>", quicksort(lst))
    # e.g
    print(factorialR(4))
    print(factorialI(4))
    print(factorialHOF(4))
    print("*" * 30)


# Others
def power(val):
    return val**2


def sum(a_list, i=0):
    return a_list[i] if (i+1) == len(a_list) else a_list[i] + sum(a_list, i+1)


def power_list(a_list, i=0):
    return [power(a_list[i])] if (i+1) == len(a_list) else [power(a_list[i])] + power_list(a_list, i+1)
