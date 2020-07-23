import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--name', nargs='+', default=['world'])
    namespace = parser.parse_args()

    for name in namespace.name:
        print("Hello, {}!".format(name))
