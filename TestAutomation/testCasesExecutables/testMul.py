#!/bin/env python3

import math
import sys

sys.path.append('../project/src/calculate-activity')

import functions as fun

def testMul(operands):

    test = fun.mul(operands[0], operands[1])

    return test
