from calculate-activity import functions

def main(argv):
    x = add(argv[0], argv[1])
    print(x)


if __name__ == "__main__":
   main(sys.argv[1:])
