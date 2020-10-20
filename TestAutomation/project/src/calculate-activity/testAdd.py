from functiontest import *
import sys

def main(argv):
    x = add(argv[0], argv[1])
    print(x)


if __name__ == "__main__":
   main(sys.argv[1:])
