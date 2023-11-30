#!/usr/bin/python3
import sys

def infinite_add(args):
    try:
        result = sum(int(arg) for arg in args)
        print(result)
    except ValueError:
        print("Error: Please provide valid integers.")

if __name__ == "__main__":
    # Exclude the script name itself from the arguments
    arguments = sys.argv[1:]
    infinite_add(arguments)
