import argparse

NAME = 'mr_hello'
DESCRIPTION = '''This is a program that are able to greet a person for a number of times'''
EPILOG = '(c) Andrei Gorlanov 2020'
VERSION = '0.0.1'

if __name__ == '__main__':
    p = argparse.ArgumentParser(prog=NAME, description=DESCRIPTION, epilog=EPILOG, add_help=False)
    p.add_argument('--name', '-n', default='world', help='Name of a person to greet')
    p.add_argument('--count', '-c', type=int, required=True, metavar='COUNT', help='Number of greetings')
    p.add_argument('--help', '-h', action='help', help='Help message')
    p.add_argument('--version', '-v', action='version', help='Version', version='%(prog)s {}'.format(VERSION))
    args = p.parse_args()

    for _ in range(args.count):
        print("Hello, {}!".format(args.name))
