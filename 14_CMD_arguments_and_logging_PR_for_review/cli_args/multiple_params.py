import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('name')
    parser.add_argument('count', type=int)
    args = parser.parse_args()

    for _ in range(args.count):
        print("Hello, {}!".format(args.name))
