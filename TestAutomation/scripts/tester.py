#!/bin/env python3

# helper method for runAllTests
import os
import sys

sys.path.append('../testCasesExecutables')

import testAdd, testSub, testMul, testDiv

def runTest(info):
    
    if 'add' in info[4]:
        
        result = testAdd.testAdd(info[5])
        
        if result == info[6]:
            os.system('echo "True" >> ../temp/testCaseEvaluations.txt')
        
        else:
            os.system('echo "False" >> ../temp/testCaseEvaluations.txt')
        
    elif 'sub' in info[4]:

        result = testSub.testSub(info[5])

        if result == info[6]:
            os.system('echo "True" >> ../temp/testCaseEvaluations.txt')
        
        else:
            os.system('echo "False" >> ../temp/testCaseEvaluations.txt')


    elif 'mul' in info[4]:

        result = testMul.testMul(info[5])

        if result == info[6]:
            os.system('echo "True" >> ../temp/testCaseEvaluations.txt')
        
        else:
            os.system('echo "False" >> ../temp/testCaseEvaluations.txt')

    elif 'div' in info[4]:

        result = testDiv.testDiv(info[5])

        if result == info[6]:
            os.system('echo "True" >> ../temp/testCaseEvaluations.txt')
        
        else:
            os.system('echo "False" >> ../temp/testCaseEvaluations.txt')

    else:

        return -1


