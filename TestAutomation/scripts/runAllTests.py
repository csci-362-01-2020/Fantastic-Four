#!/bin/env python3 

import os
import parser
import tester
import report

def main():
    
    # clears the output of the testCaseEvaluations.txt and
    # testCaseOutputs.txt files
    os.system('cat /dev/null > temp/testCaseEvaluations.txt')
    os.system('cat /dev/null > temp/testCaseOutputs.txt')

    # list for the test case files 
    testFiles = [] 
    
    # loop for grabbing the directory info with the testcase
    # files
    for f in os.walk('testCases'):
        testFiles.append(f)
    
    # this takes the output of the list which is first a 
    # tuple, and then takes the third argument (the list of
    # the files), casts them to a list, and then sorts them
    
    testFiles = sorted(list(testFiles[0][2]))

    # helper file that parses the testcases and then returns
    # a dictionary with the following format:
    # {'testCaseID': [testcaseID, requirement tested, driver name,
    #  class being tested, function being tested, parameters, 
    #  expected oracle]} 

    tests = parser.parse(len(testFiles) + 1)

    # generates a list of the testcases as keys for running individual
    # tests

    testCases = list(tests.keys())
    
    # loop to run the testcases

    for i in range(15):
        
        tester.runTest(tests[testCases[i]])
    
    # generate a professional grade report based on the testcases that 
    # have been run
    report.generateReport(tests, testCases)

main()
