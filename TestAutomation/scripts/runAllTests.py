#!/bin/env python3 

import math
import os
import sys

def main():

    testFiles = []

    for i in range(1, 26):
        testFiles.append('testCase' + str(i) + '.txt')
    
    #print(testFiles)

    testCases = {}
    line = []
    parameters = []

    #for f in testFiles:

    inFile = open('../testCases/' + testFiles[0], 'r')
    fi = []
    
    for f in testFiles:
        
        inFile = open('../testCases/' + f, 'r')
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