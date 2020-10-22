#!/bin/env python3 

import os
import parser
import tester
import report

def main():

    # path to functions.py
    path = '../project/src/calculate-activity/functions.py'

    # list for the test case files 
    testFiles = [] 
    
    # loop for grabbing the directory info with the testcase
    # files
    for f in os.walk('../testCases'):
        testFiles.append(f)

    # this takes the output of the list which is first a 
    # tuple, and then takes the third argument (the list of
    # the files), casts them to a list, and then sorts them

    testFiles = sorted(list(testFiles[0][2]))

    # helper file that parses the testcases and then returns
    # a dictionary with the following format:
    # {'testCaseID': [testcaseID, requiremnet tested, driver name,
    #  class being tested, function being tested, parameters, 
    #  expected oracle]} 

    tests = parser.parse(testFiles)

    # generates a list of the testcases as keys for running individual
    # tests
    testCases = list(tests.keys())
    

    


    # clears the output of the testCaseEvaluations.txt file
    os.system('cat /dev/null > ../temp/testCaseEvaluations.txt')

main()