import csv

def replace_frames(infile, reorders):
    """Put frames into the right order, returning a list of binary objects"""
    return list()


def import_data(filename):
    """Imports CSV data from filename and returns a list of rows"""
    return list()


def combine_bytes(reorder):
    """Combine list of bytes into one binary sequence"""
    o = b''
    for r in reorder:
        o += r
    return o
