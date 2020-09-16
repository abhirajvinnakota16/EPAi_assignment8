import subprocess
import sys
import pytest
import code8
from code8 import *
import time
import os.path
import re
import inspect 
import random


README_CONTENT_CHECK_FOR = [
    'doc_string_length()',
    'fibonnaci()',
    'func_counter()',
    'func_counter1()'
]





# Basic Functions 

def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"


def test_readme_contents():
    readme = open("README.md", "r")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 200, "Make your README.md file interesting! Add atleast 200 words"


def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"


def test_readme_file_for_formatting():
    f = open("README.md", "r")
    content = f.read()
    f.close()
    assert content.count("#") >= 10

def test_function_name_had_cap_letter():
    functions = inspect.getmembers(code8, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"







## Test cases for doc_string_length

# Helper functions

## Doc string less than 50 characters
def func1():
    ''' deoc '''
    print('a')

## Doc string more than 50 characters
def func2():
    ''' Write a closure that takes a function and then check whether the function passed has a 
    docstring with more than 50 characters. 50 is stored as a free variable - 200 
Write a closure that gives you the next Fibonacci number - 100 '''
    print('b')

## Doc string with 0 characters
def func3():
    ''''''
    print('a')

## Doc string == None
def func4():
    print('a')


##  Test 1 - 4 cases : Character length default to 50
def test_doc_string_length_1():
    check1 = doc_string_length()
    assert check1(func1) == "Doc string is less than 50 characters", "Issue with less than 50 characters"
    assert check1(func2) == "Doc string is more than 50 characters", "Issue with more than 50 characters"
    assert check1(func3) == "Doc string is less than 50 characters", "Issue with 0 characters"
    assert check1(func4) == "Doc string is none", "Issue with doc string being None"

##  Test 2 - 4 cases : Character length set to 100
def test_doc_string_length_2():
    check2 = doc_string_length(100)
    assert check2(func1) == "Doc string is less than 100 characters", "Issue with less than 100 characters"
    assert check2(func2) == "Doc string is more than 100 characters", "Issue with more than 100 characters"
    assert check2(func3) == "Doc string is less than 100 characters", "Issue with 0 characters"
    assert check2(func4) == "Doc string is none", "Issue with doc string being None"








## Test cases for fibonacci()

## Test 1 - 3 cases : Default values  of 0 , 1 and their first addition to 1
def test_fibonacci_1():
    fib = fibonacci()
    assert fib() == 0, 'Issue with first number of fibonnaci'
    assert fib() == 1, 'Issue with second number of fibonnaci'
    assert fib() == 1, 'Issue with third number of fibonnaci'


## Test 2 - 1 case : List of first ten numbers
def test_fibonacci_2():
    list1 = [0,1,1,2,3,5,8,13,21,34]
    list2 = []
    fib = fibonacci()
    for i in range(10):
        list2.append(fib())
    assert list2 == list1, 'Issue with list of first 10 numbers'


## Test 3 - 1 case : 100th fibonnaci number
def test_fibonacci_3():
    fib = fibonacci()
    for i in range(99):
        fib()
    assert fib() == 218922995834555169026, 'Issue with 100th fibonnaci number'








### Test cases for func_counter()
z = 10



# Helper function - runs 5 cases with 2nd Instance func_counter with global dict -  the dict should keep adding
def func_counter_abc():
    instance2 = func_counter()
    assert instance2(add) == {'add': 2, 'mul': 1, 'div': 1} , 'Issue with add function, instance 2' # add
    assert instance2(mul) == {'add': 2, 'mul': 2, 'div': 1} , 'Issue with mul function, instance 2' # mul
    assert instance2(div) == {'add': 2, 'mul': 2, 'div': 2} , 'Issue with div function, instance 2' # div
    assert instance2(z) == "Not a function" , 'Issue with not a function, instance 2'
    assert instance2(func1) == "Not a valid function" , 'Issue with not being a valid function, instance 2'


# Test1 - 10 cases : Instance 1 of func_counter with global dict 
def test_func_counter_1():
    instance1 = func_counter()
    assert instance1(add) == {'add': 1, 'mul': 0, 'div': 0} , 'Issue with add function, instance 1' # add
    assert instance1(mul) == {'add': 1, 'mul': 1, 'div': 0} , 'Issue with mul function, instance 1' # mul
    assert instance1(div) == {'add': 1, 'mul': 1, 'div': 1} , 'Issue with div function, instance 1' # div
    assert instance1(z) == "Not a function" , 'Issue with not a function, instance 1'
    assert instance1(func1) == "Not a valid function" , 'Issue with not being a valid function, instance 1'

    func_counter_abc()

    ### Using old instance - the dictionary should keep adding
    assert instance1(add) == {'add': 3, 'mul': 2, 'div': 2} , 'Issue with add function, instance 1, second time' # add
    assert instance1(mul) == {'add': 3, 'mul': 3, 'div': 2} , 'Issue with mul function, instance 1, second time' # mul
    assert instance1(div) == {'add': 3, 'mul': 3, 'div': 3} , 'Issue with div function, instance 1, second time' # div
    assert instance1(z) == "Not a function" , 'Issue with not a function, instance 1, second time'
    assert instance1(func1) == "Not a valid function" , 'Issue with not being a valid function, instance 1, second time'









## Test cases for func_counter2()

# Test1 - 5 cases : sending empty dict
def test_func_counter2_1():
    instance1 = func_counter1({})
    assert instance1(add) == {'add': 1} , 'Issue with add function, instance 1, func_counter2' # add
    assert instance1(mul) == {'add': 1, 'mul': 1} , 'Issue with mul function, instance 1, func_counter2' # mul
    assert instance1(div) == {'add': 1, 'mul': 1, 'div': 1} , 'Issue with div function, instance 1, func_counter2' # div
    assert instance1(z) == "Not a function" , 'Issue with not a function, instance 1, func_counter2'
    assert instance1(func1) == "Not a valid function" , 'Issue with not being a valid function, instance 1, func_counter2'


# Test2 - 5 cases : sending random value in dict 
def test_func_counter2_2():
    instance1 = func_counter1({'z' : 0, 'func1':0})
    assert instance1(add) == {'add': 1, 'z' : 0, 'func1':0} , 'Issue with add function, instance 1, func_counter2' # add
    assert instance1(mul) == {'add': 1, 'mul': 1, 'z' : 0, 'func1':0} , 'Issue with mul function, instance 1, func_counter2' # mul
    assert instance1(div) == {'add': 1, 'mul': 1, 'div': 1, 'z' : 0, 'func1':0} , 'Issue with div function, instance 1, func_counter2' # div
    assert instance1(z) == "Not a function" , 'Issue with not a function, instance 1, func_counter2'
    assert instance1(func1) == "Not a valid function" , 'Issue with not being a valid function, instance 1, func_counter2'


# Test3 - 5 cases : sending a correct dict
def test_func_counter2_3():
    instance1 = func_counter1({'add': 5, 'mul': 6, 'div': 10})
    assert instance1(add) == {'add': 6, 'mul': 6, 'div': 10} , 'Issue with add function, instance 1, func_counter2' # add
    assert instance1(mul) == {'add': 6, 'mul': 7, 'div': 10} , 'Issue with mul function, instance 1, func_counter2' # mul
    assert instance1(div) == {'add': 6, 'mul': 7, 'div': 11} , 'Issue with div function, instance 1, func_counter2' # div
    assert instance1(z) == "Not a function" , 'Issue with not a function, instance 1, func_counter2'
    assert instance1(func1) == "Not a valid function" , 'Issue with not being a valid function, instance 1, func_counter2'