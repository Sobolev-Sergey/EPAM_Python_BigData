import sys

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Hello, world!")
    else:
        if len(sys.argv) != 3:
            print("Error. There has to be 3 args. Received: {}".format(len(sys.argv)))
            sys.exit(1)

        param_name, param_value = sys.argv[1], sys.argv[2]

        if param_name == "--name" or param_name == "-n":
            print("Hello, {}!".format(param_value))
        else:
            print("Error. Unknown parameter '{}'".format(param_name))
            sys.exit(1)
