import argparse
import os
import fileinput


def dir_path(string):
    """
    Checks if the passed string is a dir.
    """
    if os.path.isdir(string):
        return string
    else:
        raise NotADirectoryError(string)

parser = argparse.ArgumentParser(description='Example: app.py -f <log_to_scan>')
parser.add_argument("-f","--file",metavar='',help="Log file to scan.",required=True, default=os.getcwd())
args = parser.parse_args()

logfile = fileinput.input([args.file])


for lines in logfile:
    if 'Shannon memtest failed' in lines:
        print(f"found keyword:{lines}")