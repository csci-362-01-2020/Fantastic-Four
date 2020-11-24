#!/bin/env python3

# import necessary libraries
import math
import sys

# Script Name: testPow.py
# Method: testPow(operands)
# Purpose: test the exponentiation of two numbers for 
# the calculate-activity
# Inputs: list of operands
# Outputs: the result of the pow(x, y) method

def testPow(operands):

    sys.path.append('project/src/calculate-activity')

    import functions as fun


    # invoke the add method for the functions.py file 
    test = fun.pow(operands[0], operands[1])

    # return the result
    return test
