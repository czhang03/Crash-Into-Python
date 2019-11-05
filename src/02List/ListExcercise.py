from .List import *


#######################################
# EXERCISE!!!!!!!!!!!!!!!!!!
#######################################

def filter_index_operation(condition, lst):
    """implementing the function filter using index operation

    Python has a built in function called `filter` that behave the same as this function
    the filter function will remove any element that does not satisfy the condition

    >>> filter_index_operation(lambda n: n > 0, [-1, 1, -2, 3])
    [1, 3]
    >>> filter_index_operation(lambda n: 10 % n == 0 , [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    [1, 2, 5, 10]

    The previous code are just factors of 10
    :param condition: a function take each element of the list to a boolean
    :param lst: the input list to be filtered
    :return: a list contains only elements that satisfy the condition (when sent into condition will return True)
    """
    pass


def filter_using_foldl(condition, lst):
    """implementing the function filter using foldl (no index operation allowed)

    Python has a built in function called `filter` that behave the same as this function
    the filter function will remove any element that does not satisfy the condition

    >>> filter_using_foldl(lambda n: n > 0, [-1, 1, -2, 3])
    [1, 3]
    >>> filter_using_foldl(lambda n: 10 % n == 0 , [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    [1, 2, 5, 10]

    The previous code are just factors of 10
    :param condition: a function take each element of the list to a boolean
    :param lst: the input list to be filtered
    :return: a list contains only elements that satisfy the condition (when sent into condition will return True)
    """
    pass


def filter_list_comprehension_sample():
    """Since filter is so wildly used, list comprehension has also sugar for filter

    """

    # remove the negative and double the positive
    a1 = map(lambda x: 2 * x, filter(lambda x: x > 0, [-1, 12, 3]))
    a2 = [2 * x for x in [-1, 12, 3] if x > 0]
    # both a1, a2 should equal to [24, 6]


def all_using_index(bool_list):
    """Implement the function all using index operation

    Python has a built in function called `all` that behave the same as this function
    This checks if a list is all True

    >>> all_using_index([True, True, False, True])
    False
    >>> all_using_index([True, True])
    True

    :param bool_list: a boolean list to check
    :return: if the input `bool_list` is all true
    """
    pass


def all_using_foldl(bool_list):
    """Implement the function all using foldl (no index operation allowed)

    Python has a built in function called `all` that behave the same as this function
    This checks if a list is all True

    >>> all_using_foldl([True, True, False, True])
    False
    >>> all_using_foldl([True, True])
    True

    :param bool_list: a boolean list to check
    :return: if the input `bool_list` is all true
    """
    pass


def all_using_any(bool_list):
    """Implement the function all using any and list comprehension (no foldl and index operation allowed)

    Python has a built in function called `all` that behave the same as this function
    This checks if a list is all True

    >>> all_using_foldl([True, True, False, True])
    False
    >>> all_using_foldl([True, True])
    True

    :param bool_list: a boolean list to check
    :return: if the input `bool_list` is all true
    """
    pass


def zip_with(func, lst1, lst2):
    """This function combines the corresponding element of `lst1` and `lst2` with the function `func`

    >>> zip_with(lambda a, b: a + b, [1, 2, 3], [10, 20, 30])
    [11, 22, 33]

    This function will also discard all the rest of the value of the longer list
    >>> zip_with(lambda a, b: a + b, [1, 2, 3], [10, 20, 30, 40, 50, 100])
    [11, 22, 33]
    >>> zip_with(lambda a, b: a + b, [10, 20, 30, 40, 50, 100], [1, 2, 3])
    [11, 22, 33]

    :param func: take a element of `lst1` and a element of `lst2` and return a element in the result
    :param lst1: the input list 1
    :param lst2: the input list 2
    :return: all the corresponding element of `lst1` and `lst2` combined with `func`
    """
    len_res = min(len(lst1), len(lst2))

    res = []
    for i in range(len_res):
        res.append(func(lst1[i], lst2[i]))
    return res


def zip_using_zip_with(lst1, lst2):
    """Uses zip_with to implement a zip function

    in python there is a builtin function `zip` that behaves exactly like this
    >>> zip_using_zip_with([1, 2, 3], [10, 20, 30])
    [(1, 10), (2, 20), (3, 30)]

    This function will also discard all the rest of the value of the longer list

    >>> zip_using_zip_with([1, 2, 3], [10, 20, 30, 40, 50, 100])
    [(1, 10), (2, 20), (3, 30)]
    >>> zip_using_zip_with([10, 20, 30, 40, 50, 100], [1, 2, 3])
    [(10, 1), (20, 2), (30, 3)]

    NOTICE: code like `(1, 2)` or `(1, 2, 3)` are called a tuple, they are very similar to lists
    :param lst1: the input list 1
    :param lst2: the input list 2
    :return: a list of tuple containing the corresponding element of `lst1` and `lst2`
    """
    pass


def zip_with_using_zip(func, lst1, lst2):
    """uses the `zip` function and list comprehension to implement zip_with function

    HINT: you can unpack a tuple, just like you expected
    >>> (a, b) = (1, 2)

    then a will equal to 1, and b will equal to 2
    You can also unpack tuple in list comprehension

    >>> zip_with(lambda a, b: a + b, [1, 2, 3], [10, 20, 30])
    [11, 22, 33]

    This function will also discard all the rest of the value of the longer list

    >>> zip_with(lambda a, b: a + b, [1, 2, 3], [10, 20, 30, 40, 50, 100])
    [11, 22, 33]
    >>> zip_with(lambda a, b: a + b, [10, 20, 30, 40, 50, 100], [1, 2, 3])
    [11, 22, 33]

    :param func: take a element of `lst1` and a element of `lst2` and return a element in the result
    :param lst1: the input list 1
    :param lst2: the input list 2
    :return: all the corresponding element of `lst1` and `lst2` combined with `func`
    """
    pass


def zip3_using_zip(lst1, lst2, lst3):
    """Uses zip with to implement a zip3 function

    zip3 function zips 3 lists
    >>> zip3_using_zip([1, 2, 3], [10, 20, 30], [2, 4, 6])
    [(1, 10, 2), (2, 20, 4), (3, 30, 6)]
    >>> zip3_using_zip([1, 2, 3], [10, 20, 30, 40, 50, 100], [2, 4, 6, 8])
    [(1, 10, 2), (2, 20, 4), (3, 30, 6)]
    >>> zip_using_zip_with([2, 4, 6, 8], [10, 20, 30, 40, 50, 100], [1, 2, 3])
    [(2, 10, 1), (4, 20, 2), (6, 30, 3)]

    NOTICE: code like `(1, 2)` or `(1, 2, 3)` are called a tuple, they are very similar to lists
    :param lst1: the input list 1
    :param lst2: the input list 2
    :param lst3: the input list 3
    :return: a list of tuple containing the corresponding element of `lst1` and `lst2`
    """
    pass


def is_elem(elem, lst):
    """see if `elem` is a element of the `lst`

    NOTICE: No index operation or foldl allowed, but you can use any other function that have been defined/used
    HINT: this is a one line function

    returns true if there exists any element in lst equals to `elem`:
    >>> is_elem(1, [2, 3, -1])
    False
    >>> is_elem(True, [False, True, True])
    True

    :param elem: the element to test
    :param lst: see if the `elem` is in here
    :return: a boolean indicating whether `elem` is a element of the `lst`
    """
    pass


def my_enumerate(lst):
    """returns a list of tuple, where the first element is the index,
    and the second is the corresponding element of the list

    HINT: this is a one line function

    python has a builtin function with the same functionality called `enumerate`

    >>> my_enumerate([True, False, False])
    [(0, True), (1, False), (2, False)]
    >>> my_enumerate([1, 2, 3])
    [(0, 1), (1, 2), (2, 3)]

    """
    pass


def find_all(elem, lst):
    """returns a list of index for every element that is equal to `elem`

    NOTICE: nothing like `range(len(lst))` will be allowed.
    Just use list comprehension and the function defined.
    HINT: this is a one line function

    >>> find_all(10, [1, 2, 3])
    []
    >>> find_all(10, [1, 10, 3, 10])
    [1, 3]

    :param elem: the element to find
    :param lst: to find `elem` in this list
    """
    pass


def slicing(lst, start, end):
    """slice the list just like lst[start:end]

    NOTICE: nothing like `range(len(lst))` or `lst[start:end]` will be allowed.
    Just use list comprehension and the function defined.
    HINT: this is a one line function

    >>> slicing([1, 2, 3], 1, 4)
    [2, 3]
    >>> slicing([1, 2, 3], -1, 4)
    [1, 2, 3]
    >>>slicing([1, 2, 3], -1, 2)
    [1, 2]

    :param lst: the list to slice
    :param start: the start index (if smaller than 0, then slice from start)
    :param end: the end index (element of this index will not be included in the result,
        if larger than length of input list, then slice to the end)
    """


def drinking_game(student_matrix):
    """This function is to demonstrate that list comprehensions are extremely good at processing complex data

    NOTICE: Please give reasonable names to all the temp variable like `cs_total_score` or `cs_total_wine_drunk`
        If you cannot think of a reasonable name for the temp variable, you are doing it wrong.

    CS student and math student are playing a drinking game, you need to decide which of the major has won.
    You need to sum up all the beer and wine each major has drunk,
    - each wine drunk will give the major 4 point.
    - each beer drunk will give the major 1 point.
    and we need to finally divide the score of each major by the number of student participated

    >>> drinking_game([("Max", "Math", 5, 1), ("Alex", "CS", 1, 2), ("Bay", "Math", 3, 1), ("Test", "CS", 1, 4)])
    "CS"

    then there are 4 students:
    - Max of math major drunk 5 beer and 1 wine, then he will get 5 + 1 * 4 = 9 point
    - Alex of CS major drunk 1 beer and 2 wine, then he will get 1 + 2 * 4 = 9 point
    - Bay of math major drunk 3 beer and 1 wine, then he will get 3 + 1 * 4 = 7 point
    - Test of CS major drunk 1 beer and 4 wine, then he will get 1 + 4 * 4 = 17 point
    Therefore math major have 9 + 7 = 16 points, and CS major will have 9 + 17 = 26 points.
    Then we divide by number of participant,
    math will have 8 point average, CS major will have 13 point average,
    Therefore the function will return "CS" because CS major has won

    >>> drinking_game([("Max", "Math", 5, 1), ("Alex", "Math", 1, 2), ("Bay", "Math", 2, 1), ("Test", "CS", 1, 4)])
    "CS"

    then there are 4 students:
    - Max of math major drunk 5 beer and 1 wine, then he will get 5 + 1 * 4 = 9 point
    - Alex of math major drunk 1 beer and 2 wine, then he will get 1 + 2 * 4 = 9 point
    - Bay of math major drunk 3 beer and 1 wine, then he will get 2 + 1 * 4 = 6 point
    - Test of CS major drunk 1 beer and 4 wine, then he will get 1 + 4 * 4 = 17 point
    Therefore math major have 9 + 9 + 6 = 24 points, and CS major will have 17 points.
    Then we divide by number of participant,
    math will have 24/3 = 8 point average, CS major will have 17 point average,
    Therefore the function will return "CS" because CS major has won (again)

    :param student_matrix: a list of tuple, where in each tuple
        - first element is student name
        - second element is the student major
        - third element is the beer drunk
        - fourth element is the wine drunk
    """
    pass


def prime_test(n):
    """return whether `n` is a prime

    NOTICE: You cannot use a for loop, but list comprehension and all the other functions are allowed

    >>> prime_test(1)
    False
    >>> prime_test(2)
    True
    >>> prime_test(97)
    True
    >>> prime_test(57)
    False

    Being a prime means nothing between 1 and `n` is divisible by `n`, and 1 is not a prime
    :param n: the input to check if it is a prime.
    :return a boolean to indicate if `n` is a prime.
    """
    pass


if __name__ == '__main__':
    # test if the examples in documentation work
    import doctest
    doctest.testmod()

    # add your own tests here:
