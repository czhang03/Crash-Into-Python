#########################################################
# we will cover basic data in Python, including 
# integer and boolean, 
# function definition and if statement


########################################
# basic syntax for functions
# `func` is the function name, `arg1` and `arg2` are inputs (arguments)
def func (arg1, arg2):  
    # this is the function body
    # the `return` keyword will specify what the function return
    return arg1   


# sample function
# this function adds one to the given input
def add1(n):
    add1n = n + 1
    return add1n


# here is a sample use of if statement
# this function gives the largest even number
# that is smaller or equal to the input
def greatest_even_below(n):
    # the % symbol is the modular, this means if n mod 2 = 0
    if n % 2 == 0:
        return n 
    else:
        return n-1

# compact if statement 
# we can compactify the if statement of previous function
# this is called "inline if statement"
def another_greatest_even_below(n):
    return n if (n % 2 == 0) else n - 1


##########################################
# Booleans 
# we have already make use of booleans 
# they are either `True` or `False` 
# for example the operator == will return a boolean 
# then that boolean will be fead into the `if then else statement`

# a function that will always return 1
def always_1():  # notice a function can take no arguments
    if True:
        return 1
    else:
        return 130493


# Here is a good excercise for boolean, 
# we want to implement the `and` function
# using only `if then else`
def my_and(b1, b2):
    # if b1 is true, then we need to look at b2
    if b1:
        # if both b1 and b2 is true  
        if b2:
            return True 
        else:
            return False 
    # if b1 is not true then the `and` will not be true
    # then we don't need to look at b2
    else:
        return False


# noticed that we can shorten this function
def my_and1(b1, b2):
    if b1:
        return b2
    else:
        return False 


# use inline if
def my_and2(b1, b2):
    # this becames quite unreadable.
    return b2 if b1 else False


# consecutive if statement
# say, our company produces 3 products with id (integer)
# we want to write a function that gives the name of the product 
# when a id is provided
def get_name_from_id_bad(prod_id):
    if prod_id == 1:
        return "apple"
    else:
        if prod_id == 2:
            return "orange"
        else:
            if prod_id == 3:
                return "pear"
            else:
                return "invalid product id"
# previous function quickly became unreadable, 
# due to too many nested if statements
# we use elif to flatten it
def get_name_from_id(prod_id):
    if prod_id == 1:
        return "apple"
    elif prod_id == 2:
        return "orange"
    elif prod_id == 3:
        return "pear"
    else:
        return "invalid product id"


#########################################
# EXCERSICE!!!!!
#########################################


# calculating the absolute value of a number
# notice < can be useful:
# `1 < 2` will be equal to `True`
# `1 < 1` will be equal to `False`
def my_abs(n):
    pass  # your solution here.


# determine if a year is leap year 
# if a year is devisible by 4, then it is a leap year;
# unless it is devisible by 100, then it is not;
# unless it is devisible by 400, then it is a leap year.
# therefore 
# `leap_year(2001)` should equal to `False` 
# `leap_year(2008)` should equal to `True` 
# `leap_year(1000)` should equal to `False` 
# `leap_year(2000)` should equal to `True` 
def leap_year(year):
    pass  # your solution here.


# implementing exclusive or of two boolean
# exclusive or are true when either each are true but not both
# `xor(True, True)` should equal to `False`
# `xor(False, True)` should equal to `True`
# `xor(True, False)` should equal to `True`
# `xor(False, False)` should equal to `False`
def xor(b1, b2):
    pass  # your solution here


# here is what get executed when you run the script
# kind of like main function in C++
if __name__ == "__main__":
    print("myabs(1) = ", my_abs(1))
    print("myabs(-1) = ", my_abs(-1))
    print("myabs(-10) = ", my_abs(-10))
    print("leap_year(2001) = ", leap_year(2001))
    print("leap_year(2008) = ", leap_year(2008))
    print("leap_year(1000) = ", leap_year(1000))
    print("leap_year(2000) = ", leap_year(2000))
    print("xor(True, True) = ", xor(True, True))
    print("xor(False, True) = ", xor(False, True))
    print("xor(True, False) = ", xor(True, False))
    print("xor(False, False) = ", xor(False, False))
