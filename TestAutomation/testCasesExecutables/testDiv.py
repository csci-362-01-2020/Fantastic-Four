#!/bin/env python3

# import necessary libraries
import math
import sys

# Script Name: testDiv.py
# Method: testDiv(operands)
# Purpose: test the division of two numbers for 
# the calculate-activity
# Inputs: list of operands
# Outputs: the result of the div(x, y) method

def testDiv(operands):

    sys.path.append('project/src/calculate-activity')

    import functions as fun

    # invoke the div method for the functions.py file
    test = fun.div(operands[0], operands[1])

    # return the result
    return test
