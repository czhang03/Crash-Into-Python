from typing import List, Set, Dict, TypeVar, Callable, Generator, Tuple, Iterator, FrozenSet

#######################################
# EXERCISE!!!!!!!!!!!!!!!!!!
#######################################


# define all the type var used in the program
A = TypeVar("A")
B = TypeVar("B")
C = TypeVar("C")
Key = TypeVar("Key")
Val = TypeVar("Val")
Val1 = TypeVar("Val1")
Val2 = TypeVar("Val2")


def set_filter(condition: Callable[[A], bool], s: Set[A]) -> Set[A]:
    """implement the filter on set using set comprehension

    >>> set_filter(lambda n: n > 0, {-1, 1, -2, 3})
    {1, 3}
    >>> set_filter(lambda n: 10 % n == 0 , {1, 2, 3, 4, 5, 6, 7, 8, 9, 10})
    {1, 2, 5, 10}

    Please note, comprehension is a syntactic sugar for the function map and filter
    python `filter` function can also handle sets
    :param condition: a function maps element in `s` to either `True` or `False`
    :param s: the input set
    :return: the filtered set such that only contain elements in `s` that satisfy the `condition`
    """
    pass


# notice that this type var `A` is different from the `A` from above
def filter_dict_val(condition: Callable[[Val], bool], d: Dict[Key, Val]) -> Dict[Key, Val]:
    """implement filter on dict using dict comprehension

    >>> filter_dict_val(lambda n: n > 0, {"apple": -1, "orange": 1, "stuff": -2, "name": 3})
    {"orange": 1, "name": 3}
    >>> filter_dict_val(lambda s: len(s) > 3, {1: "apple", 2: "test", 3: "a", 5: "abcde", 4: "hi"})
    {1: "apple", 2: "test", 5: "abcde"}

    This function filter out only the corresponding key and val, where the val satisfies `condition`
    Notice, python `filter` behaves differently as this filter function on dict.
    :param condition: a function maps values in `d` to either `True` or `False`
    :param d:
    """
    pass


def list_to_gen(l: List[A]) -> Iterator[int]:
    """cast a list into a generator

    :param l: the input list
    :return: a generator that have exactly the same element as `l`
    """
    return (elem for elem in l)


def generator_zip(gen1: Iterator[int], gen2: Iterator[int]) -> Iterator[int]:
    """zips two generator, it is okay to mutate the value of gen1 and gen2

    in python there is a builtin function `zip` that behaves exactly like this
    >>> list(generator_zip(list_to_gen([1, 2, 3]), list_to_gen([10, 20, 30])))
    [(1, 10), (2, 20), (3, 30)]
    >>> list(generator_zip(list_to_gen([1, 2, 3]), list_to_gen([10, 20, 30, 40])))
    [(1, 10), (2, 20), (3, 30)]
    >>> list(generator_zip(list_to_gen(["t1", "t2", "t3", "t4"]), list_to_gen([1, 2, 3])))
    [('t1', 1), ('t2', 2), ('t3', 3)]

    :param gen1: the first generator to input
    :param gen2: the second generator to input
    :return: a generator of tuple containing the corresponding element of `gen1` and `gen2`
    """
    pass


def dict_zip_via_key(d1: Dict[Key, Val1], d2: Dict[Key, Val2]) -> Dict[Key, Tuple[Val1, Val2]]:
    """zips tow list, two values corresponds to each other if it has the same key in `d1` and `d2`

    >>> dict_zip_via_key({"t1": 1, "t2": 2, "t3": 3}, {"t2": 10, "t3": 20, "t1": 30})
    {'t1': (1, 30), 't2': (2, 10), 't3': (3, 20)}

    If there is some key that is not in both dictionary, then that key and value will all be discarded
    >>> dict_zip_via_key({"t1": 1, "t2": 2, "t3": 3}, {"t2": 10, "t4": 20, "t1": 30})
    {'t1': (1, 30), 't2': (2, 10)}
    >>> dict_zip_via_key({"t1": "apple", "t2": "orange", "t3": "stuff"}, {"t2": 10, "t4": 20, "t1": 30})
    {'t1': ('apple', 30), 't2': ('orange', 10)}

    :param d1: the input dict 1
    :param d2: the input dict 2
    :return: a dict mapping keys to tuples containing the corresponding value of that key in `d1` and `d2`
    """
    pass


# QUESTION: Does zip on set make sense? why or why not?
# Short Answer here:
#


def immutable_group_by(criteria: Callable[[A], B], s: FrozenSet[A]) -> FrozenSet[FrozenSet[A]]:
    """Group element of `l` using the given criteria, You can not use any variable mutation in implementing this

    This function will partition `s` into some smaller lists
    (elements in the smaller list should have the same order as in `l`),
    where in each smaller lists given any two element `e1` and `e2`, `criteria(e1) == criteria(e2)`
    >>> res1 = immutable_group_by(lambda e: e > 2, frozenset({1, 2, 3, 4}))
    >>> res1 == frozenset({frozenset({3, 4}), frozenset({1, 2})})
    True
    >>> res2 = immutable_group_by(lambda s: s in {"orange", "apple", "pear"},
    ...                         frozenset({"human", "pear", "pig", "orange"}))
    >>> res2 == frozenset({frozenset({'pig', 'human'}), frozenset({'pear', 'orange'})})
    True
    >>> res3 = immutable_group_by(lambda n: abs(n), frozenset({-1, 1, -1, 2, 3, -2}))
    >>> res3 == frozenset({frozenset({3}), frozenset({2, -2}), frozenset({1, -1})})
    True

    - You can assume equality (==) is defined on type `B`
    - We have to use frozen set because in python, set of set is not valid
        (try in the python console to create a set of set)
    :param criteria: a function maps each element to a value of type `B`,
        which will determine how the elements are grouped together
    :param s: the input frozen set
    :return: a frozen set of frozen set that is partitioned in the aforementioned fashion
    """
    pass


def mutable_group_by(criteria: Callable[[A], B], s: FrozenSet[A]) -> FrozenSet[FrozenSet[A]]:
    """Group element of `l` using the given criteria, implemented using index operation and mutation

    This function will partition `l` into some smaller lists
    (elements in the smaller list should have the same order as in `l`),
    where in each smaller lists given any two element `e1` and `e2`, `criteria(e1) == criteria(e2)`
    >>> res1 = mutable_group_by(lambda e: e > 2, frozenset({1, 2, 3, 4}))
    >>> res1 == frozenset({frozenset({3, 4}), frozenset({1, 2})})
    True
    >>> res2 = mutable_group_by(lambda s: s in {"orange", "apple", "pear"},
    ...                         frozenset({"human", "pear", "pig", "orange"}))
    >>> res2 == frozenset({frozenset({'pig', 'human'}), frozenset({'pear', 'orange'})})
    True
    >>> res3 = mutable_group_by(lambda n: abs(n), frozenset({-1, 1, -1, 2, 3, -2}))
    >>> res3 == frozenset({frozenset({3}), frozenset({2, -2}), frozenset({1, -1})})
    True

    - You can assume equality (==) is defined on type `B`
    - We have to use frozen set because in python, set of set is not valid
        (try in the python console to create a set of set)
    :param criteria: a function maps each element to a value of type `B`,
        which will determine how the elements are grouped together
    :param s: the input frozen set
    :return: a list of list (ideally set of list) that is partitioned in the aforementioned fashion
    """
    # IMPORTANT
    # this is a sample implementation, this shows you that imperative thinking (use of mutation variable)
    # often results in very non-robust and convoluted code

    # start with list, so that we can perform mutation
    res_list_list: List[List[A]] = []

    # iterate over the elements
    for elem in s:
        added_to_some_smaller_list = False  # haven't added the element into some smaller list yet

        # going through each smaller list in the result
        for index, smaller_list in enumerate(res_list_list):

            # we assume that the smaller_list is non-empty, this will be true because of our construction
            # by the way, making assumption on your code is always not recommended
            # because it will make making changes to your code a lot harder.
            # In general we want our assumption in code to be explicit
            # (the best way is to encode the assumption in type)
            if criteria(smaller_list[0]) == criteria(elem):
                # if the criteria matches, then we add elem to the smaller list
                res_list_list[index].append(elem)
                # indicate that we have added this into some smaller list
                added_to_some_smaller_list = True

        # if after all the smaller list, we cannot find a group to put it in,
        # then added it as a new group in `res_list_list`
        if not added_to_some_smaller_list:
            res_list_list.append([elem])

    # freeze each `smaller_list`
    res_list_fsets = []
    for lst in res_list_list:
        res_list_fsets.append(frozenset(lst))

    # freeze the entire list
    return frozenset(res_list_fsets)


def get_word_count_dict(paragraph: str) -> Dict[str, int]:
    """This function generate the word count for the input paragraph

    The each word in the input paragraph are separated by some spaces,
    and possibly followed by comma (',') or period ('.') surrounded by quotes ("'" and '"'),
    and some letter might be capitalized.
    (common practice is to define a global constant called `PUNCTUATION = {",", ".", "'", '"'}`,
    but you can define punctuation as a local variable here)
    We need to remove all the punctuation at the beginning and end of the word,
    and un-capitalize all the words (`lower` method will do that).

    >>> res1 = get_word_count_dict("A fox jumped.")
    >>> res1 == {'a': 1, 'fox': 1, 'jumped': 1}
    True
    >>> res2 = get_word_count_dict("A fox, a brown fox. The fox is brown.")
    >>> res2 == {'a': 2, 'brown': 2, 'fox': 3, 'the': 1, 'is': 1}
    True
    >>> res3 = get_word_count_dict("weird 'punch' .this ,that,   weird     spacing")
    >>> res3 == {'weird': 2, 'punch': 1, 'this': 1, 'that': 1, 'spacing': 1}
    True

    :param paragraph: a paragraph of text to count all the word for
    :return a dictionary maps all the word to its count
    """
    pass


def count_pair(paragraph: str, word_pairs: Set[Tuple[str, str]]) -> Dict[Tuple[str, str], Tuple[int, int]]:
    """count the appearance of pair of words

    In some language, there are some words means the same thing, but are used by different group of people,
    for example in English: "eggplant" and "aubergine"; "think" and "reckon"; and "grocery" and "supermarket"
    By counting these words in pair, we can predict what group the author belongs in.

    >>> gb_us_word_pair = {("reckon", "think"), ("aubergine", "eggplant"), ("supermarket", "grocery")}
    >>> res1 = count_pair("I reckon there should be some aubergine." gb_us_word_pair)
    >>> res1 == {("reckon", "think"): (1, 0), ("aubergine", "eggplant"): (1, 0), ("supermarket", "grocery"): (0, 0)}
    True
    >>> res2 = count_pair("Supermarket is right at the corner, I reckon." gb_us_word_pair)
    >>> res2 == {("reckon", "think"): (1, 0), ("aubergine", "eggplant"): (0, 0), ("supermarket", "grocery"): (1, 0)}
    True
    >>> res3 = count_pair("Gonna get some grocery." gb_us_word_pair)
    >>> res3 == {("reckon", "think"): (0, 0), ("aubergine", "eggplant"): (0, 0), ("supermarket", "grocery"): (0, 1)}
    True
    >>> res4 = count_pair("" gb_us_word_pair)
    >>> res4 == {("reckon", "think"): (0, 0), ("aubergine", "eggplant"): (0, 0), ("supermarket", "grocery"): (0, 0)}
    True

    :param paragraph: a paragraph of text
    :param word_pairs: a list of pair of word to count.
    :return: a dictionary that maps the pair of words to their counts (also a pair)
    """
    pass


if __name__ == '__main__':
    # test if the examples in documentation work
    import doctest

    doctest.testmod()

    # add your own tests here:
