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
        print('<style>table,th, td {border: 3px solid black;} </style>')
        
        print('<body>')
        print('<table style="width:100%">')
        print('<tr>\n <th>Test ID</th>\n <th>Requirement</th>\n <th>Driver</th>\n <th>Component</th>\n <th>Method</th>\n <th>Inputs</th>\n <th>Oracle</th>\n <th>Output</th>\n <th>Result</th> </tr>')
        
        print('<h1 style="color:blue;"> Calculate Activity Test Report ' + str(now.strftime('%Y-%m-%d %H:%M:%S')) + '</h1>')
        

    
    
        for i in range(len(testResult)):
         
            result = info[keys[i]]
            
            print('<tr>')
            print('<td> ' + result[0] + '</td>')
            print('<td> ' + result[1] + '</td>')
            print('<td> ' + result[2] + '</td>')
            print('<td> ' + result[3] + '</td>')
            print('<td> ' + result[4] + '</td>')
            print('<td> ' + str(result[5]) + '</td>')
            print('<td> ' + str(result[6]) + '</td>')
            print('<td> ' + str(testOutput[i]) + '</td>')
            
            if (str(testResult[i]) == "True"):
                print('<td style="color:green;">Test Passed</td>')
                
            else:
                print('<td style="color:red;">Test Failed</td>')
                

            print('</tr>')
            
       
            
        
        print('</body>')
        print('</html>')
        sys.stdout = og
        
    #open the report    
    os.system('xdg-open ' + reportName)   
    
