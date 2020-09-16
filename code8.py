
## Question 1
def doc_string_length(l = 50):

    '''This function helps in checking if a particular funcs docstring is greater 
    than 50 characters (default value). The variable 'l' that paramterizes the length 
    that needs to be checked for can be defined by the user while initializing the function '''

    def check (func):
        nonlocal l 
        string = func.__doc__
        if string is None:
            return "Doc string is none"
        else:
            if (l > len(string)):
                return "Doc string is less than {} characters".format(l)
            else:
                return "Doc string is more than {} characters".format(l)
    return check



## Question 2
def fibonacci():
    ''' This function helps return the next fibonacci function each time it is called. 
    When initialized, the first 2 values get declared, based on which the next() function 
    [i.e, returned by the function] calculates the next number'''
    
    last = 1
    second_last = 0
    count = 0
    def next ():
        nonlocal last
        nonlocal second_last
        nonlocal count
        if count == 0:
            count += 1
            return 0
        if count == 1:
            count += 1
            return 1
        else:
            count += 1
            new = last + second_last
            second_last = last
            last = new
            return new
    return next



## Question 3
def add(a,b):
    return a+b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b

glo_dict = {'add': 0, 'mul': 0, 'div': 0}

def func_counter():
    ''' This function uses a global dictionary to count the number of times a particular 
    function has been called. This function only tracks the 'add', 'sub' and 'div' function. 
    The tracked numbers are stored in a global dictionary that is commonly available to any 
    instance of this function'''

    def count(func):
        global glo_dict
        if callable(func) == False:
            return 'Not a function'
        else:
            if func.__name__ in glo_dict:
                glo_dict[func.__name__] += 1
                return glo_dict
            else:
                return 'Not a valid function'
    return count



## Question 4

def func_counter1(dict_var):
    ''' This function is based of the previous function. However, this function accepts 
    a dictionary from the user when initialized. It returns a function count which then 
    tracks the number of times the 'add/sub/div' function is called. Each time it is called, 
    the updated dictionary is returned. If another function that is not add/mul/div is sent, 
    then func will return saying it is not a valid function'''

    def count(func):
        nonlocal dict_var
        if callable(func) == False:
            return 'Not a function'
        else:
            if func.__name__ in ['add','mul','div'] and func.__name__ in dict_var:
                dict_var[func.__name__] += 1
                return dict_var
            elif func.__name__ in ['add','mul','div']:
                dict_var[func.__name__] = 1
                return dict_var
            else:
                return 'Not a valid function'
    return count