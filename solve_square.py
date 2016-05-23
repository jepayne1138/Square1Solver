from square1 import argparser
from square1 import input_parser

def main():
    args = argparser.parse()
    with open(args.input_file) as input_fileobj:
        cube = input_parser.read_input(input_fileobj)
    print cube


if __name__ == '__main__':
    main()
