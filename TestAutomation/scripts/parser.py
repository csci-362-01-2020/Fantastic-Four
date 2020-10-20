#1/bin/env python3

def parse(testFiles):

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

        if '.' in fi[7]:
             temp = float(fi[7])
        
        else:
             temp = int(fi[7])

        fi[7] = temp

        testCases[fi[1]] = fi[1:]

    return testCases