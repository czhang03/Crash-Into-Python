from typing import List, Dict, Callable, Tuple, TypeVar


#########################################################
# we will cover collection data structure,
# such as string, dict, set in python.
# we will also cover type annotation, and methods


#########################################################
# String

def string_sample():
    """Some sample code for python string

    """
    # python string behaves almost exactly like lists

    # you can index it
    first_letter = "abc"[0]  # first letter will be "a"

    # you can iterate over it
    a = [letter for letter in "abc"]  # `a` will be a list ["a", "b", "c"]

    # there are some special method defined on them
    # here is some really useful ones

    # `split` method
    # the `split` method splits the string.
    # by default, it splits all the white space
    # therefore `a` will equal to ["a", "quick", "fox"]
    a = "a quick fox".split()
    # we can tell the method what to split on
    # then `a` will be equal to ['We must know', ' We will know', '']
    a = "We must know. We will know.".split(".")

    # IMPORTANT:
    # `split` is a "method" on string
    # "method" behaves almost like functions (with subtle difference), it is just different syntax.
    # but if you call `split("We must know. We will know.", ".")` python will give you an error
    # since `split` is defined as a method, therefore you cannot use it as a function.

    # Here is the difference between method and function (rather technical, but not that important)
    # method can make change to the value in front of them, for example:
    # `res.append("test")` will change the value in `res`
    # however, many method choose not to change the value in the front, like:
    # `string.spilt()` will not change the value stored in `string`
    # Function can change the value in its input, but only under very specific circumstances
    # for example the input is a list.
    # Python has messy design on when the function can change its input, I recommend you not to worry about it.

    # `strip` method
    # by default strip method removes start and ending spaces
    # so `a` will be "test"
    a = "  test    ".strip()
    # we can let them remove some start and ending character if we want
    # in this case strip will remove all the start and ending "s"s,
    # `a` will be equal to   "   test    "
    a = "ssss   test    sssss".strip("s")

    # `join` method
    # `join` method will join a list of string with some string
    # it behaves kind of like the inverse operation of split method
    # in here `a` will equal "a quick fox"
    # `b` will equal "aquickfox"
    a = " ".join(["a", "quick", "fox"])
    b = "".join(["a", "quick", "fox"])

    # `startswith` and `endswith` method
    # they test if a string start with some string or ends with some string
    a = "a quick fox".startswith("aquick")  # `a` will be false
    b = "a quick fox".endswith("k fox")  # `b` will be true

    # These are not all the methods on string, but just some useful ones


#########################################################
# Type annotation
# we have encountered the following bug in our program before

def operation_on_file(file_id):
    """Perform some operation on file with `file_id`

    :param file_id: specifies the file to perform operation on
    """
    pass


def operation_on_files(file_ids):
    """perform the operation on multiple file

    :param file_ids: a list of file_id to specify which file to perform operation on
    """
    for file_id in file_ids:
        operation_on_file(file_id)


# this is the buggy code
# the person want to call `operation_on_file`, but called `operation_on_files`
# and because you can iterate over a string,
# this line will perform operation on file 1 and file 0.
operation_on_files("10")


# this bug takes us a long time to find, mostly because it is hard to reproduce,
# since you need more than 10 files to trigger this bug,
# and during testing we want minimal example, and rarely sent too many files into the program
# also when you perform the operation on any file with id like "1", "5", "9",
# it behaves totally normal.

# we noticed that `operation_on_file` takes a string as input,
# and `operation_on_files` takes a list as input.
# then if we specified the type of the input, we will save us so much trouble:


def new_operation_on_file(file_id: str) -> None:
    """Perform some operation on file with `file_id`

    :param file_id: specifies the file to perform operation on
    """
    pass


def new_operation_on_files(file_ids: List[str]) -> None:
    """perform the operation on multiple file

    :param file_ids: a list of file_id to specify which file to perform operation on
    """
    for file_id in file_ids:
        new_operation_on_file(file_id)


# then when you try to call the wrong function, pycharm will complain.
# you should see a yellow highlight on "10" in your pycharm:
new_operation_on_files("10")


# IMPORTANT:
# From now on, we will require everyone to put type annotation on every function definition.


#########################################################
# Dict
def dict_sample() -> None:
    """A dictionary is a structure that maps a key into a value

    Here is some sample code of dictionary
    """
    # you can create a dictionary like so
    dict1 = {"in1": "out1", "in2": "out2", "in3": "out3"}
    # IMPORTANT
    # notice that dictionary is a "unordered structure"
    # you cannot assume when you iterate over `dict1`, `in1` will appear first,

    # a dictionary can contain any type in its value part
    dict2 = {1: "test1", 2: "test2", 3: "test3"},
    dict3 = {1: lambda x: x + 1, 2: lambda x: 2 * x, 3: lambda x: x ** 2}

    # we can annotate the type of a variable if we want 
    # (everything between `dict4` and `= {` is the type annotation for `dict4`)
    # but it is customary to only annotate the function definition
    # (it is sometime useful to annotate the type of variables)
    # here we are saying that dict4 is a
    # dictionary that map a tuple of int and string, to a function (callable) that take a int and return a int
    dict4: Dict[Tuple[int, str], Callable[[int], int]] = {
        (1, "test1"): lambda x: x + 1,
        (2, "test2"): lambda x: 2 * x,
        (3, "test3"): lambda x: x ** 2
    }

    # we can index a dict by a key
    a = {1: "test1", 2: "test2"}
    b = a[1]  # a[1] will give you "test1"
    # this will assign the variable `f` the function `lambda x: x + 1`
    f = dict4[(1, "test1")]
    c = f(1)  # c will be 2

    # we can set values on a dictionary (remember mutation are usually bad, try to avoid them):
    a[1] = "test2"  # now the value for the key `1` is changed, so `a` will be changed to a = {1: "test2", 2: "test2"}

    # There are three method on dict that are most important:
    a_keys = a.keys()  # this will return a list of all the keys in `a`, which will be [1, 2]
    a_vals = a.values()  # this will return all the values in `a`, which will be ["test2", "test2"]
    # this will return all the keys and values in `a` in pair
    # which will be [(1, "test2"), (2: "test2")]
    # this is extremely useful in comprehensions
    a_items = a.items()

    # you can create new dict using dict comprehension just like list comprehension
    b = {"test" + str(n): n for n in range(2)}
    # this will create a dictionary that maps  `"test" + str(n)` to the integer `n`
    # (`str(n)` will change int `n` into a string, for example `str(1)` will be "1")

    t = TypeVar("t")  # dealers a type variable, it can represent any type

    # example use of items method:
    def add1_to_vals(inp_dict: Dict[t, int]) -> Dict[t, int]:
        """adds 1 to every value

        :param inp_dict: the input dictionary
        :return: a new dictionary where all the key maps to a value that is the original value plus 1
        """
        return {key: val + 1 for (key, val) in inp_dict.items()}


#########################################################
# generator
def generator_sample():
    # generator is something that can be created by generator comprehension:
    a = (i for i in "a quick brown fox".split())
    # a will be a generator contains `"a", "quick", "brown", "fox"`

    # IMPORTANT:
    # generator will generate the next element when it is needed to, hence the name "generator"
    # so that a generator is very memory efficient,
    # since there will not have more than 1 element in a generator that is in memory.

    # You can iterate over generator
    b = [("word" + str(idx + 1), word) for (idx, word) in enumerate(a)]
    # b will be a list of tuple: [("word1", "a"), ("word2", "quick"), ("word3", "brown"), ("word4", "fox")]

    # IMPORTANT:
    # Generator is very dangerous, in that when it is iterated over, it becomes empty.
    # If we do the following
    b2 = [("word" + str(idx + 1), word) for (idx, word) in enumerate(a)]

    # `b2` will be an empty list, because `a` is consumed by the generation of `b`.
    # Since the list comprehension generating `b` has iterated over `a`, therefore `a` became empty.
    # IMPORTANT:
    # when you use a generator, a good rule of thumb is not to assign a name to it

    # for example:
    def prime_test(n):
        """return whether `n` is a prime

        :param n: the input to check if it is a prime.
        :return a boolean to indicate if `n` is a prime.
        """
        if n is 1:
            return False
        else:
            # notice that without a parentheses around a comprehension,
            # then python will assume it is generator comprehension
            return not any(n % num is 0 for num in range(2, n))


def set_sample():
    # set in python, just like set in mathematics
    # is a unordered collection such that every element is distinct
    a = {1, 2, 4, 4, 3}
    # when you print out `a`, it will show `{1, 2, 3, 4}` because
    # 1. set is unordered, so that the order of the elements
    #       may not be the same as the way it is created ({1, 2, 4, 4, 3})
    # 2. set does not contain duplicated elements
    #       therefore the duplicated 4 will only appear 1 time in the `a`
    bool_val = a == {2, 1, 4, 3}  # bool_val will be true

    # you can get the union and intersection of set using `union` method and `intersection` method
    a = {1, 2}.union({3, 4, 1})  # `a` will be {1, 2, 3, 4}
    a = {1, 2}.intersection({3, 4, 1})  # `a` will be {1}

    # you can get if a element is in a set using the `in` keyword
    # (in the same way, you can get if an element is in a list, and also a string)
    bool_val = 1 in {4, 2, 3, 1}  # `bool_val` will be `True`
    bool_val = 5 in {4, 2, 3, 1}  # `bool_val` will be `False`

    # you can create a set using set comprehension
    a = {2 * x for x in [1, 2, 3] if x > 1}


def frozen_set_sample():
    """Introduction to Frozen Set

    Frozen Set is just a immutable set, so that all the things about set will be true
    the reason to introduce frozen set is that in python, you cannot have a set of set (because set is mutable)
    but you can have a frozen set of frozen set
    """
    # set in python, just like set in mathematics
    # is a unordered collection such that every element is distinct
    a = frozenset({1, 2, 4, 4, 3})
    # when you print out `a`, it will show `{1, 2, 3, 4}` because
    # 1. set is unordered, so that the order of the elements
    #       may not be the same as the way it is created ({1, 2, 4, 4, 3})
    # 2. set does not contain duplicated elements
    #       therefore the duplicated 4 will only appear 1 time in the `a`
    bool_val = a == frozenset({2, 1, 4, 3})  # bool_val will be true

    # you can get the union and intersection of set using `union` method and `intersection` method
    a = frozenset({1, 2}).union(frozenset({3, 4, 1}))  # `a` will be {1, 2, 3, 4}
    a = frozenset({1, 2}).intersection(frozenset({3, 4, 1}))  # `a` will be {1}

    # you can get if a element is in a set using the `in` keyword
    # (in the same way, you can get if an element is in a list, and also a string)
    bool_val = 1 in frozenset({4, 2, 3, 1})  # `bool_val` will be `True`
    bool_val = 5 in frozenset({4, 2, 3, 1})  # `bool_val` will be `False`

    # frozen set can be created using a generator comprehension
    # (you can also use list comprehension and set comprehension to create frozen set,
    # but generator is the most efficient)
    a = frozenset(2 * x for x in [1, 2, 3] if x > 1)
    # using list and set comprehension also works
    a = frozenset([2 * x for x in [1, 2, 3] if x > 1])
    a = frozenset({2 * x for x in [1, 2, 3] if x > 1})


# FINAL CONCLUSION:
#
# - List
#   - Construction
#       - explicit construction, like `[1, 2, 3]`
#       - can be generated using list comprehension
#   - Property and constrain:
#       - Ordered collection (can be sliced and indexed)
#   - Important methods:
#       - count (`a.count(1)`, this will count how many 1 in `a`)
#       - all the other method will mutate some value, therefore are all not recommended to use
#   - Fast to
#       - index (`a[2]`,
#               you can use negative number to index the last elements: `a[-2]` will give you the second last element)
#       - slice (`a[0:1]`,
#                `a[:-1]` will give you all the element except the last one)
#       - append element at end (most of the time)
#       - remove element at end
#   - Slow to
#       - determine if a element is in it (`a in [1,2, 3]`)
#       - remove element in the middle
#       - insert element in the middle
#
# - String
#   - Construction
#       - explicit construction, like `"test"`
#   - Property and constrain:
#       - Ordered collection (can be sliced and indexed)
#   - Important methods
#       - split
#       - strip
#       - join
#       - startswith and endswith (test if a string starts with or ends with a certain string)
#   - performance-wise exactly the same as a list
#
# - Generator
#   - Construction
#       - can be generated using generator comprehension
#   - Property and constrain:
#       - Ordered collection, but cannot be sliced or indexed
#       - but disappears after being iterated over (basically apply any operation on it will change its value)
#       - Good rule of thumb is not to assign name to it
#   - Memory efficient
#   - No method that are useful, this is basically a memory efficient alternative to list
#       - generator is useful to construct one use lists. (see example in generator and frozen set)
#
# - Dict
#   - Construction
#       - explicit construction, like  `{1: "test", 2: "test2"}`
#       - dict comprehension
#   - Property and constrain:
#       - unordered collection, cannot be sliced, but can be indexed using key
#       - keys needs to be distinct
#       - key needs to be "hashable" (basically means immutable at this point),
#           This means list, set, dict cannot be used as key, but frozenset, string, int, tuple can.
#       - no constrain on values, anything can be a value.
#       - fun fact: you can use functions as key, but you cannot index the dict:
#           `{lambda x: x: "", lambda x: x + 1: ""}[lambda x: x]` will give you an error
#   - Important Methods:
#       - keys (get all the keys)
#       - values (get all the values)
#       - items (get the keys and corresponding value paired in tuple)
#   - Fast to (basically everything going from key is fast)
#       - Find the value via key
#       - change a value of a key
#       - insert a new corresponding key and value
#       - remove a corresponding key and value (if given a key)
#   - Slow to
#       - determine if a value or key is in the dict
#       - change the key of a value
#
# - Set (frozen set)
#   - Construction
#       - explicit construction, like `{1, 2}` or `frozenset({1, 2})`, `frozenset([1,2])`
#       - set comprehension or the function `frozenset` followed by a generator comprehension
#   - Property and constrain:
#       - unordered collection, cannot be sliced or indexed
#       - elements needs to be distinct
#       - elements needs to be "hashable" (basically means immutable at this point),
#           This means list, set, dict cannot be set elements, but frozenset, string, int, tuple can.
#       - fun fact: you can use functions as elements, but you cannot test if the function is in the set:
#           `(lambda x: x) in {lambda x: x}` will give you false.
#   - important method:
#       - union
#       - intersection
#       - there are other useful method, but they will mutate the a value, therefore not recommended.
#   - Fast to (basically everything is fast,
#     but `set` is a very weak structure with many constrains, like all the element has to be distinct)
#       - determine if a element is in the set (`1 in {1, 2}`)
#       - insert element
#       - delete element
#   - Slow to: Not that I can think of
