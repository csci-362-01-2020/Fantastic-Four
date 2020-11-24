#!/bin/env python3

import math
import sys

# Script Name: parser.py
# Method: parse(num)
# Purpose: Parses the input file and 
# returns a dictionary of all the test cases
# Inputs: the number of test case files
# Outputs: A dictionary with all the test case files information

def parse(num):

    # Return dictionary
    testCases = {}

    # List for the line data 
    line = []
    
    # List for the parameters
    parameters = []
    
    #  Loop to iterate over the test files
    for f in range(1, num):
        
        # Individual test file
        inFile = open('testCases/testCase' + str(f) + '.txt', 'r')
        
        # all the necessary data for the file
        fi = []

        # Parsing data in the file line by line separated by 
        # the ':', with the .strip() to clean up the whitespace on 
        # the second parameter, and then the append to fi to store 
        # the data
        for line in inFile:
            line = line.split(':')
            line = line[1].strip()
            fi.append(line)

        # This loop casts the parameters passed to the function into
        # the appropriate variable types or appropriate library call 
        # for the imported libraries. This will also check for the str()
        # function to cast parameters
        if ',' in fi[6]:
            parameters = fi[6].split(',')
            fi[6] = parameters

            for i in range(len(parameters)):
                
                if 'str' in parameters[i]:
                    parameters[i] = str(eval(parameters[i]))
                
                else:
                    parameters[i] = eval(parameters[i])

        else:
            fi[6] = eval(fi[6])
        
        # this casts the expected oracle to the appropriate type
        if 'str' in fi[7]:
            fi[7] = str(fi[7])
        
        else:
            fi[7] = eval(fi[7])

        # this assigns the key to the testcase ID and assigns the list
        # from the testcase ID to the end of the lsit as the value
        testCases[fi[1]] = fi[1:]

        inFile.close()

    # return the dictionary for further processing
    return testCases