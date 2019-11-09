from src.Week01BasicData.BasicData import *


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
