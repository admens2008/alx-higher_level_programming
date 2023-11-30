#!/usr/bin/python3
import dis
import importlib.util
import sys

def discover_names():
    # Load the compiled module
    spec = importlib.util.spec_from_file_location("hidden_4", "./hidden_4.pyc")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    # Get all names in the module
    all_names = dir(module)

    # Filter names that do not start with '__' and print them in alphabetical order
    for name in sorted(all_names):
        if not name.startswith('__'):
            print(name)

if __name__ == "__main__":
    discover_names()
