import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--name', choices=['Ann', 'John', 'Eva'], default='world')
    args = parser.parse_args()
    print("Hello, {}!".format(args.name))
