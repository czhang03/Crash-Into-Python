#########################################################
# we will cover collection data structure,
# such as string, tuple, dict, set in python.
# we will also cover type annotation, and methods


#########################################################
# String
from typing import List


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

    # split method
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

    # strip method
    # by default strip method removes start and ending spaces
    # so `a` will be "test"
    a = "  test    ".strip()
    # we can let them remove some start and ending character if we want
    # in this case strip will remove all the start and ending "s"s,
    # `a` will be equal to   "   test    "
    a = "ssss   test    sssss".strip("s")

    # join method
    # join method will join a list of string with some string
    # it behaves kind of like the inverse operation of split method
    # in here `a` will equal "a quick fox"
    # `b` will equal "aquickfox"
    a = " ".join(["a", "quick", "fox"])
    b = "".join(["a", "quick", "fox"])


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

# From now on, we will require everyone to put type annotation on every function definition.
