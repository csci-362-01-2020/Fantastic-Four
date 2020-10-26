#!/bin/env python3

# helper method for runAllTests
import sys

sys.path.append('../testCasesExecutables')

import testAdd, testSub, testMul, testDiv

def runTest(info):
    

    if 'add' in info[4]:
        
        result = testAdd.testAdd(info[5])
        
    elif 'sub' in info[4]:

        result = testSub.testSub(info[5])

    elif 'mul' in info[4]:

        result = testMul.testMul(info[5])

    elif 'div' in info[4]:

        result = testDiv.testDiv(info[5])

    else:

        return -1


