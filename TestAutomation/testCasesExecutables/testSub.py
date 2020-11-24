#!/bin/env python3

# import necessary libraries
import math
import sys

# Script Name: testAdd.py
# Method: testAdd(operands)
# Purpose: test the addition of two numbers for 
# the calculate-activity
# Inputs: list of operands
# Outputs: the result of the add(x, y) method

def testSub(operands):

    sys.path.append('project/src/calculate-activity')

    import functions as fun

    # invoke the sub method for the functions.py file 
    test = fun.sub(operands[0], operands[1])

    # return the result
    return test
