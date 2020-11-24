#!/bin/env python3

# import necessary libraries
import math
import sys

# Script Name: testMul.py
# Method: testMul(operands)
# Purpose: test the multiplication of two numbers for 
# the calculate-activity
# Inputs: list of operands
# Outputs: the result of the mul(x, y) method

def testMul(operands):

    sys.path.append('project/src/calculate-activity')

    import functions as fun

    # invoke the mul method for the functions.py file 
    test = fun.mul(operands[0], operands[1])

    # return the result
    return test
