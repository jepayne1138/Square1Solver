import argparse

def parse():
    parser = argparse.ArgumentParser(description='Solves Square1 Cube')
    parser.add_argument('input_file', help='Path to the input file')
    return parser.parse_args()
