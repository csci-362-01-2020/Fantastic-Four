#!/bin/env python3 

import math
import os
import sys
import parser

def main():

    testFiles = []
    
    for f in os.walk('../testCases'):
        testFiles.append(f)

    testFiles = sorted(list(testFiles[0][2]))
    
    tests = parser.parse(testFiles)
    print(tests)


main()