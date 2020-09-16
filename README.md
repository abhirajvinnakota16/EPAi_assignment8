# Assignment 8 - Scopes and Closures

This assignment has 4 functions. They all use closures in one form or the other. Proper test cases have been written adn test for validation. 

## doc_string_length()
This function helps in checking if a particular funcs docstring is greater than 50 characters (default value). The variable 'l' that paramterizes the length that needs to be checked for can be defined by the user while initializing the function

## fibonnaci()
This function helps return the next fibonacci function each time it is called. When initialized, the first 2 values get declared, based on which the next() function [i.e, returned by the function] calculates the next number

## func_counter()
This function uses a global dictionary to count the number of times a particular function has been called. This function only tracks the 'add', 'sub' and 'div' functions. The tracked numbers are stored in a global dictionary that is commonly available to any instance of this function

## func_counter1()
This function is based of the previous function. However, this function accepts a dictionary from the user when initialized. It returns a function count which then tracks the number of times the 'add/sub/div' function is called. Each time it is called, the updated dictionary is returned. If another function that is not add/mul/div is sent, then func will return saying it is not a valid function ####