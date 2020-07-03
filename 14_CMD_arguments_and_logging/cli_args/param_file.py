import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--name', type=argparse.FileType(), required=True)
    args = parser.parse_args()

    text = args.name.read()
    print(text)
    args.name.close()
