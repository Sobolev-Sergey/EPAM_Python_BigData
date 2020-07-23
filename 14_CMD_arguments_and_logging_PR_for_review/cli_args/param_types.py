import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--count', default=1, type=int)
    args = parser.parse_args()

    for _ in range(args.count):
        print("Hello, world!")
