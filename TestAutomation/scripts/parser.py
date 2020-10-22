#!/bin/env python3

import math
import sys

def parse(testFiles):

    # return dictionary
    testCases = {}

    # list for the line data 
    line = []
    
    # list for the parameters
    parameters = []
    
    #  loop to iterate over the test files
    for f in range(1, len(testFiles) + 1):
        
        # individual test file
        inFile = open('../testCases/testCase' + str(f) + '.txt', 'r')
        
        # all the necessary data for the file
        fi = []

        # parsing data in the file line by line separated by 
        # the ':', with the .strip() to clean up the whitespace on 
        # the second parameter, and then the append to fi to store 
        # the data
        for line in inFile:
            line = line.split(':')
            line = line[1].strip()
            fi.append(line)
        
        # this loop casts the parameters passed to the function into
        # the appropriate variable types or appropriate library call 
        # for the imported libraries
        if ',' in fi[6]:
            parameters = fi[6].split(',')
            fi[6] = parameters

            for i in range(len(parameters)):
                parameters[i] = eval(parameters[i])

        else:
            fi[6] = eval(fi[6])
        
        # this casts the expected oracle to the appropriate type
        fi[7] = eval(fi[7])

        # this assigns the key to the testcase ID and assigns the list
        # from the testcase ID to the end of the lsit as the value
        testCases[fi[1]] = fi[1:]

    # return the dictionary for further processing
    return testCases