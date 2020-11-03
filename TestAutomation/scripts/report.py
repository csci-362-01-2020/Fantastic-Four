#!/bin/env python3

# helper for runAllTests

import os
import sys

def generateReport(info, keys):

    #build an array of test results
    inFile1 = open('temp/testCaseEvaluations.txt', 'r')
    
    testResult = []

    for line in inFile1:
        line = line.strip()
        testResult.append(eval(line))

    inFile1.close()
    
    #build an array of test outputs
    inFile2 = open('temp/testCaseOutputs.txt', 'r')
    
    testOutput = []
    
    for line in inFile2:
        line = line.strip()
        testOutput.append((line))
        
    inFile2.close() 
    
    with open('reports/report.html', 'w') as out:
        og = sys.stdout
        sys.stdout = out
        print('<html>')
        print('<body>')
        print('<p style="color:red;">Test output</p>')
        print('</body>')
        print('</html>')
        #sys.stdout = og
    
    #testBreak = '*' * 50
    
        for i in range(1, len(testResult) + 1):
         
            result = info[keys[i - 1]]
            print('<p>')
            for item in result:
                print(item)
            print(testOutput[i-1])
            print(testResult[i-1])
            print('</p>')
            
        
        print('</body>')
        print('</html>')
        sys.stdout = og
        
    #open the report    
    os.system('xdg-open ' + 'reports/report.html')   
    
