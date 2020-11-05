#!/bin/env python3

# helper for runAllTests

import os
import sys
import datetime 

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
    
    #get current date and time and generate name of report
    now = datetime.datetime.now()
    reportName = 'reports/report-' + str(now.strftime('%Y-%m-%d-%H:%M:%S')) + '.html'
    
    #generate report with html formatting
    with open(reportName, 'w') as out:
        og = sys.stdout
        sys.stdout = out
        
        print('<html>')
        print('<style> hr {width:100%; height:10px; background-color:black} </style>')
        print('<body>')
        
        print('<h1 style="color:blue;"> Calculate Activity Test Report ' + str(now.strftime('%Y-%m-%d %H:%M:%S')) + '</h1>')
        print('<hr>')
        

    
    
        for i in range(1, len(testResult) + 1):
         
            result = info[keys[i - 1]]
            
            print('<b>Test ID:</b> ' + result[0] + '<br>')
            print('<b>Requirement:</b> ' + result[1] + '<br>')
            print('<b>Driver:</b> ' + result[2] + '<br>')
            print('<b>Component:</b> ' + result[3] + '<br>')
            print('<b>Method:</b> ' + result[4] + '<br>')
            print('<b>Inputs:</b> ' + str(result[5]) + '<br>')
            print('<b>Oracle:</b> ' + str(result[6]) + '<br>')
            print('<b>Output:</b> ' + str(testOutput[i-1]) + '<br>')
            
            if (str(testResult[i-1]) == "True"):
                print('<b style="color:green;">Test Passed</b> <br>')
                
            else:
                print('<b style="color:red;">Test Failed</b> <br>')
                
            print('<hr>')
            
            
            #print('<p>')
            #for item in result:
            #    print(item)
            #print(testOutput[i-1])
            #print(testResult[i-1])
            #print('</p>')
            
        
        print('</body>')
        print('</html>')
        sys.stdout = og
        
    #open the report    
    os.system('xdg-open ' + reportName)   
    
