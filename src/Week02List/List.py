#########################################################
# we will cover list in Python.
# We will also cover higher order function (function as input),
# and lambda expression


def list_sample():
    # list is one of the collection object in Python
    # you can write a list in the following way:
    my_list = [1, 2, 3]

    # you can iterate over a list
    for elem in my_list:
        print(elem)  # this will print out all the element of the list in order
    # if you run the previous code
    # you will get
    # 1
    # 2
    # 3
    # printed on your screen

    # you can also index your list
    first = my_list[0]  # first will be 1
    second = my_list[1]  # second will be 2
    third = my_list[2]  # third will be 3

    # and you can slice your list
    first_two = my_list[0:2]  # first_two will be [1, 2]
    last_two = my_list[1:3]  # last_two will be [2, 3]
    # you can omit the first index if you are slicing from the start
    # you can omit the second index if you are slicing to the end
    first_two = my_list[:2]  # first_two will be [1, 2]
    last_two = my_list[1:]  # last_two will be [2, 3]

    # you can also change some index of your list
    my_list[0] = second
    my_list[1] = third
    my_list[2] = first

    # notice that we cannot change the list via iteration
    for elem in my_list:
        elem = 2  # this will not have any effect on my_list
    print(my_list)
    # after you run this code, my_list will still be [2, 3, 1]
    # because you changed it in the previous block

    # IMPORTANT:
    # notice here that it is very dangerous to modify things stored in a variable,
    # since if you have not read this block:
    # my_list[0] = second
    # my_list[1] = third
    # my_list[2] = first
    # you will not know that `my_list` now is [2, 3, 1]
    # therefore TRY TO AVOID CHANGING YOUR VARIABLE.

    # it is sometimes very useful to create a list that have all the number
    # from our start number to the ending number
    one_to_five = list(range(1, 6))  # notice we need range(1, 6) to produce a list of 1 to 5
    zero_to_five = list(range(6))  # we can omit the start if we are starting from 0

    # to modify a list (you probably never have to do this)
    # we need to index it
    # notice that we cannot change the list via iteration
    for index in range(len(my_list)):  # len function will return the length of my_list
        my_list[index] = 2  # this will not have any effect on my_list
    print(my_list)
    # notice that this is kind of ugly,
    # since `range(len(my_list))` is very unreadable.

    # you can combine two lists:
    new_list = [1, 3, 4] + [2, 8, 9]  # new_list will be [1, 3, 4, 2, 8, 9]
    # list(range(3)) would be [0, 1, 2]
    # list(range(3, 6)) would be [3, 4, 5]
    # combining them will get [0, 1, 2, 3, 4, 5]
    zero_to_five = list(range(3)) + list(range(3, 6))


#######################################
# So, when doing data engineering, we constantly need to perform actions on lists
# here are some examples (bad implementations, we will show how to fix them later)

def bad_double_list(l):
    """ Doubling every element in the input list l

    >>> bad_double_list([1, 2, 3])
    [2, 4, 6]
    >>> bad_double_list([-2, 0, 1.3])
    [-4, 0, 2.6]

    :param l: the input list
    """
    # to avoid modifying l, we create a new list, the resulting list
    res = []
    # populate the res with elements
    for elem in l:
        res.append(2 * elem)  # this will append the integer 2 * elem to the end of res

    # return the result list populated with the elements
    return res


def bad_add_weight_to_list(l, weight):
    """ multiply the weight to all the element of the list

    :param weight: the weight that is assigned to this list
    :param l: the input list
    """
    # to avoid modifying l, we create a new list, the resulting list
    res = []
    # populate the res with elements
    for elem in l:
        res.append(weight * elem)  # this will append the integer weight * elem to the end of res

    # return the result list populated with the elements
    return res


def bad_is_0_dummy(l):
    """ create a {True, False} dummy list

    if the element in the original list is 0, the element of the return list is True
    otherwise, the element of the return list is False
    :param l: the input list
    """
    # to avoid modifying l, we create a new list, the resulting list
    res = []
    # populate the res with elements
    for elem in l:
        res.append(True if elem == 0 else False)

    # return the result list populated with the elements
    return res


def bad_is_northeast_dummy(location_list):
    """ create a {1, 0} dummy list

    if the element in the original list is "northeast", the element of the return list is 1
    otherwise, the element of the return list is 0

    >>> bad_is_northeast_dummy(["southeast", "northeast", "southwest", "southwest", "northeast"])
    [0, 1, 0, 0, 1]

    :param location_list: list of location you need to analyze
    """
    # to avoid modifying l, we create a new list, the resulting list
    res = []
    # populate the res with elements
    for location in location_list:
        res.append(1 if location == "northeast" else 0)

    # return the result list populated with the elements
    return res


#######################################
# Notice that these previous functions are quite repetitive,
# most of the code are the same.
# basically, we want to apply some operation onto each element of the list
# therefore we an create a helper function to do that

def my_map(func, l):
    """this function applies the function f to each element of l
    In python, this function is called `map`

    :param func: the function to apply to each element
    :param l: the list to be mapped
    """
    # to avoid modifying l, we create a new list, the resulting list
    res = []
    # populate the res with elements
    for elem in l:
        res.append(func(elem))  # applies the function onto the elem.

    # return the result list populated with the elements
    return res


def better_double_list(l):
    """ Doubling every element in the input list l

    >>> better_double_list([1, 2, 3])
    [2, 4, 6]
    >>> better_double_list([-2, 0, 1.3])
    [-4, 0, 2.6]

    :param l: the input list
    """

    def double(n):  # you can define a function inside of a function
        return 2 * n

    # this function applies the function `double`
    # to each element of l
    # notice that you cannot put parenthesis after `double`
    # since that will invoke the function, but not send the function in as input
    return list(map(double, l))


def better_add_weight_to_list(l, weight):
    """ multiply the weight to all the element of the list

    :param weight: the weight that is assigned to this list
    :param l: the input list
    """

    def apply_weight(n):  # you can define a function inside of a function
        # notice that this function can access weight
        return weight * n

    # this function applies the function `apply_weight`
    # to each element of l
    return list(map(apply_weight, l))


def better_is_0_dummy(l):
    """ create a {True, False} dummy list
    where
    if the element in the original list is 0, the element of the return list is True
    otherwise, the element of the return list is False

    :param l: the input list
    """

    def gen_is_zero_dummy(n):  # you can define a function inside of a function
        return n == 0  # this is the same as `return True if n == 0 else False`

    # this function applies the function `gen_is_zero_dummy`
    # to each element of l
    return list(map(gen_is_zero_dummy, l))


def better_is_northeast_dummy(location_list):
    """ create a {1, 0} dummy list

    if the element in the original list is "northeast", the element of the return list is 1
    otherwise, the element of the return list is 0

    >>> better_is_northeast_dummy(["southeast", "northeast", "southwest", "southwest", "northeast"])
    [0, 1, 0, 0, 1]

    :param location_list: list of location you need to analyze
    """

    def gen_is_northeast_dummy(location):  # you can define a function inside of a function
        return 1 if location == "northeast" else 0

    # this function applies the function `double`
    # to each element of l
    # notice that you cannot put parenthesis after `double`
    # since that will invoke the function, but not send the function in as input
    return list(map(gen_is_northeast_dummy, location_list))


#######################################
# Things are getting better
# but there are still problems,
# we need to define a function every time we want to map it onto a list,
# but most of the function is trivial, we want to discard them after we use them.

def even_better_double_list(l):
    """ Doubling every element in the input list l

    >>> even_better_double_list([1, 2, 3])
    [2, 4, 6]
    >>> even_better_double_list([-2, 0, 1.3])
    [-4, 0, 2.6]

    :param l: the input list
    """
    # the `lambda n: 2*n` is called a "lambda expression"
    # the `n` is the input, and the `2 * n` is the return
    # `lambda n: 2*n` is exactly the same as the `double` function in the previous implementation
    return list(map(lambda n: 2 * n, l))


def even_better_add_weight_to_list(l, weight):
    """ multiply the weight to all the element of the list

    :param weight: the weight that is assigned to this list
    :param l: the input list
    """
    # the `lambda n: weight * n` defines a function where
    # the `n` is the input, and the `weight * n` is the return
    # `lambda n: weight * n` is exactly the same as the `apply_weight` function in the previous implementation
    return list(map(lambda n: weight * n, l))


def even_better_is_0_dummy(l):
    """ create a {True, False} dummy list
    where
    if the element in the original list is 0, the element of the return list is True
    otherwise, the element of the return list is False

    :param l: the input list
    """
    # the `lambda n: n == 0` defines a function where
    # the `n` is the input, and the `n == 0` is the return
    # `lambda n: n == 0` is exactly the same as the `gen_is_zero_dummy` function in the previous implementation
    return list(map(lambda n: n == 0, l))


def even_better_is_northeast_dummy(location_list):
    """ create a {1, 0} dummy list

    if the element in the original list is "northeast", the element of the return list is 1
    otherwise, the element of the return list is 0

    >>> better_is_northeast_dummy(["southeast", "northeast", "southwest", "southwest", "northeast"])
    [0, 1, 0, 0, 1]

    :param location_list: list of location you need to analyze
    """
    # the `lambda loc: 1 if loc == "northeast" else 0` defines a function where
    # the `loc` is the input, and the `1 if loc == "northeast" else 0` is the return
    # `lambda loc: 1 if loc == "northeast" else 0` is exactly the same as
    #  the `gen_is_northeast_dummy` function in the previous implementation
    return list(map(lambda loc: 1 if loc == "northeast" else 0, location_list))


#######################################
# functions are a lot more clean now
# but the main problem is that map and lambdas are not that readable
# therefore python nicely provided us a syntactic sugar for `map` called list comprehension
# (list comprehension is actually more powerful than map)

# NOTICE: although list comprehension looks like a for loop,
# but list comprehension is "pure", in that it does not mutate any inputs.

def good_double_list(l):
    """ Doubling every element in the input list l

    >>> good_double_list([1, 2, 3])
    [2, 4, 6]
    >>> good_double_list([-2, 0, 1.3])
    [-4, 0, 2.6]

    :param l: the input list
    """
    return [2 * elem for elem in l]


def good_add_weight_to_list(l, weight):
    """ multiply the weight to all the element of the list

    :param weight: the weight that is assigned to this list
    :param l: the input list
    """
    return [weight * elem for elem in l]


def good_is_0_dummy(l):
    """ create a {True, False} dummy list
    where
    if the element in the original list is 0, the element of the return list is True
    otherwise, the element of the return list is False

    :param l: the input list
    """
    return [elem == 0 for elem in l]


def good_is_northeast_dummy(location_list):
    """ create a {1, 0} dummy list
    where
    if the element in the original list is "northeast", the element of the return list is 1
    otherwise, the element of the return list is 0

    >>> good_is_northeast_dummy(["southeast", "northeast", "southwest", "southwest", "northeast"])
    [0, 1, 0, 0, 1]

    :param location_list: list of location you need to analyze
    """
    # notice you don't need the parentheses
    # `[1 if loc == "northeastern" else 0 for loc in location_list]`
    # will also work.
    return [(1 if loc == "northeast" else 0) for loc in location_list]


def nested_list_comprehension():
    """We can nest list comprehension in side of each other

    This feature is not possible with map.
    """

    # sum will be all the combination of sums:
    # [11, 21, 31, 12, 22, 32, 13, 23, 33]
    # but not
    # [11, 22, 33]
    # the latter can be done by a function called zip_with, which I will implement later
    sums = [a + b for a in [1, 2, 3] for b in [10, 20, 30]]


#######################################
# There are another class of problem we need to solve:
# when we want to combine all the elements of the list into one

def bad_sum_list(int_lst):
    """ sums all the elements of the list

    >>> bad_sum_list([1, 2, 3])
    6
    >>> bad_sum_list([1, 1, 1])
    3

    :param int_lst: a list of integer
    :return: the sum of all the element in that list
    """
    res = 0
    for elem in int_lst:
        # increment the res by elem
        res += elem
    return res


def bad_prod_list(int_lst):
    """ times all the elements of the list

    >>> bad_prod_list([1, 2, 4])
    8
    >>> bad_prod_list([2, 3, 4])
    24

    :param int_lst: a list of integer
    :return: the product of all the element in the list
    """
    res = 1
    for elem in int_lst:
        # times the res by elem, and assign the result into res
        res *= elem
    return res


def bad_any(bool_list):
    """if any of the element in `bool_list` is true

    :param bool_list: a list of bool
    :return: using "logical or" to combine the list
    """
    res = False  # default is false
    for elem in bool_list:
        # if the res is already true,
        # then there exists something in previous element that is true
        # then `res = res or elem` will not change the result
        # if the res is false,
        # we look into the elem, if elem is true, the res will be changed to true
        res = res or elem
    return res


#######################################
# We see a pattern on this class of problem
# 1. start with some start value (usually the identity element)
# 2. then keep apply some function onto the next element and previous result
# this is called `foldl` (stands for fold left)

def foldl(operation, lst, start):
    """implementing fold left using index operation

    :param operation: the operation performed on previous result and the next element
    :param lst: the input list
    :param start: the value to start with
    :return: all the element folded into start via the operation
    """
    res = start
    for elem in lst:
        res = operation(res, elem)
    return res


def sum_list(int_lst):
    """ sums all the elements of the list

    >>> sum_list([1, 2, 3])
    6
    >>> sum_list([1, 1, 1])
    3

    :param int_lst: a list of integer
    :return: the sum of all the element in that list
    """
    return foldl(
        # the operation performed is addition
        operation=lambda prev_res, elem: prev_res + elem,
        # the input list is the int list
        lst=int_lst,
        # starts the addition with 0
        start=0
    )


def prod_list(int_lst):
    """ times all the elements of the list

    >>> prod_list([1, 2, 4])
    8
    >>> prod_list([2, 3, 4])
    24

    :param int_lst: a list of integer
    :return: the product of all the element in the list
    """
    return foldl(
        # the operation performed is multiplication
        operation=lambda prev_res, elem: prev_res * elem,
        # the input list is the int list
        lst=int_lst,
        # starts the addition with 1
        start=1
    )


def my_any(bool_list):
    """if any of the element in `bool_list` is true

    Python has a builtin function called `any`
    :param bool_list: a list of bool
    :return: using "logical or" to combine the list
    """
    return foldl(
        # the operation performed is logical or
        operation=lambda prev_res, elem: prev_res or elem,
        # the input list is the bool list
        lst=bool_list,
        # starts the fold with False
        start=False
    )


# the any function can be really useful in seeing if any of the element satisfy a certain condition
def any_sample():
    """Sample code for the use of any

    """

    def exist_positive(int_list):
        # returns if the input list has a positive element
        return any([elem > 0 for elem in int_list])

    def exist_factor(n, int_list):
        # return if any element can be divisible by the input `n`
        return any([n % elem == 0 for elem in int_list])


#######################################
# Important:
# in general, writing code with `foldl` is extremely ugly and unreadable
# but it is nice exercise for higher order function and list manipulation
# Also fold is super powerful, almost all the list function can be defined with fold

def my_map_using_fold(func, lst):
    return foldl(
        # starts the fold with the empty list
        start=[],
        # keep adding the `func(elem)` to the end of prev_res
        # notice that we cannot use append here, since append will change prev_res, but return nothing.
        operation=lambda prev_res, elem: prev_res + [func(elem)],
        # perform the previous operation on the input list
        lst=lst
    )

#########################################################
# FINAL COMMENT:
# List comprehension, which are sugar for `map` and `filter` (will see in excercise) function,
# is the most important construct to work with list.
# `map` gives you a way to perform operation on list element safely and clearly
# `filter` provides you a way to discard unwanted elements. 
# Both functions are very important (and almost all you need) to process collective data.
# And processing collective data is one of the most important topics in programming, 
# since the reason to program is to automate huge amount of task that human cannot perform.
#
# foldl is super powerful, useful, and efficient.
# But due to its unreadablity, is rarely used in real-world programming,
# but are heavily used in library implementation, since it is consice and efficient.
# We are not concerned about library implementation, therefore we will only use foldl for excercises.


if __name__ == '__main__':
    # test if the examples in the documentation work
    import doctest
    doctest.testmod()
