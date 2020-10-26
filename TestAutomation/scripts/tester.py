#!/bin/env python3

# helper method for runAllTests
# import necessary libraries
import os
import sys

sys.path.append('../testCasesExecutables')

# import the test drivers for selected methods
import testAdd, testSub, testMul, testDiv

def runTest(info):
    
    # checks if the substring for the function is in the list of items
    # from the test case text files
    if 'add(' in info[4][:4]:
        
        result = testAdd.testAdd(info[5])
        
        # compare the result from the test driver to the expected outcome 
        # and append the result to the temporary file
        if result == info[6]:
            os.system('echo "True" >> ../temp/testCaseEvaluations.txt')
        
        else:
            os.system('echo "False" >> ../temp/testCaseEvaluations.txt')

    # checks if the substring for the function is in the list of items
    # from the test case text files 
    elif 'sub(' in info[4][:4]:

        result = testSub.testSub(info[5])

        # compare the result from the test driver to the expected outcome 
        # and append the result to the temporary file
        if result == info[6]:
            os.system('echo "True" >> ../temp/testCaseEvaluations.txt')
        
        else:
            os.system('echo "False" >> ../temp/testCaseEvaluations.txt')

    # checks if the substring for the function is in the list of items
    # from the test case text files
    elif 'mul(' in info[4][:4]:

        result = testMul.testMul(info[5])

        # compare the result from the test driver to the expected outcome 
        # and append the result to the temporary file
        if result == info[6]:
            os.system('echo "True" >> ../temp/testCaseEvaluations.txt')
        
        else:
            os.system('echo "False" >> ../temp/testCaseEvaluations.txt')

    # checks if the substring for the function is in the list of items
    # from the test case text files
    elif 'div(' in info[4][:4]:

        result = testDiv.testDiv(info[5])

        # compare the result from the test driver to the expected outcome 
        # and append the result to the temporary file
        if result == info[6]:
            os.system('echo "True" >> ../temp/testCaseEvaluations.txt')
        
        else:
            os.system('echo "False" >> ../temp/testCaseEvaluations.txt')
    
    # final condition that appends "Invalid Test" if there is not a driver  
    # for the specified function
    else:

        os.system('echo "Invalid Test" >> ../temp/testCaseEvaluations.txt')


