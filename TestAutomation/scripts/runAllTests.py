#!/bin/env python3 

import math
import os
import sys
import subprocess

def main():

    testFiles = []
    
    for f in os.walk('../testCases'):
        testFiles.append(f)

    testFiles = sorted(list(testFiles[0][2]))
    #print(list(testFiles[0][2]))
    
    #print(testFiles)

    # for i in range(1, 26):
    #     testFiles.append('testCase' + str(i) + '.txt')
    
    #print(testFiles)

    testCases = {}
    line = []
    parameters = []
    
    for f in range(1, len(testFiles) + 1):
        
        inFile = open('../testCases/testCase' + str(f) + '.txt', 'r')
        fi = []

        for line in inFile:
            line = line.split(':')
            line = line[1].strip()
            fi.append(line)

        if ',' in fi[6]:
            parameters = fi[6].split(',')
            fi[6] = parameters

            for i in range(len(parameters)):

                if '.' in parameters[i]:
                    temp = float(parameters[i])
                
                else:
                    temp = int(parameters[i])
                
                parameters[i] = temp
        
        #print(parameters)
        #print(type(fi[7]))

        if '.' in fi[7]:
             temp = float(fi[7])
        
        else:
             temp = int(fi[7])

        fi[7] = temp

        testCases[fi[1]] = fi[1:]

    print(testCases)

    


main()