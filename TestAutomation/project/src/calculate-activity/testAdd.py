from functions import *
import sys

def main(argv):
    x = add(int(argv[0]), int(argv[1]))
    print(x)


if __name__ == "__main__":
   main(sys.argv[1:])
