from functions import *
import sys

def main(argv):
    a = _d(argv[0])
    x = add(a, argv[1])
    print(x)


if __name__ == "__main__":
   main(sys.argv[1:])
