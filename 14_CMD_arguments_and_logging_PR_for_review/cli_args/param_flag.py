import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-g', '--goodbye', action='store_true')
    args = parser.parse_args()

    print("Hello, world!")
    if args.goodbye:
        print("Goodbye, world!")
