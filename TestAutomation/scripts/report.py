#!/bin/env python3

# helper for runAllTests

def generateReport(info, keys):

    inFile = open('../temp/testCaseEvaluations.txt', 'r')

    testResult = []

    for line in inFile:
        line = line.strip()
        testResult.append(eval(line))

    inFile.close()
    
    testBreak = '*' * 50
    
    for i in range(1, len(testResult) + 1):
        
        result = info[keys[i - 1]]
        