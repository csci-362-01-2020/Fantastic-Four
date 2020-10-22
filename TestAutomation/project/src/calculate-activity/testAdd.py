from functions import *
import sys

def main(argv):
    x = add(eval(argv[0]), eval(argv[1]))
    print(x)


if __name__ == "__main__":
   main(sys.argv[1:])
