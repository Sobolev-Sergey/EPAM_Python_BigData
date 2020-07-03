import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--name', '-n', default='world')
    parser.add_argument('--count', '-c', type=int, required=True)
    args = parser.parse_args()

    for _ in range(args.count):
        print("Hello, {}!".format(args.name))
