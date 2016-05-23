import csv

def read_input(fileobj):
    """Parses an input csv into a Cube instance"""
    reader = csv.reader(fileobj)
    for line in reader:
        print line
    return None
