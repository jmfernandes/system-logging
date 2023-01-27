#!/usr/bin/env python3
import time
import sys
import os

# append the parent directory to the path
dirname = os.path.dirname(__file__)
parentdir = os.path.join(dirname, '../')
sys.path.append(parentdir)

from common.Logger import Logger

def main():
    counter = 0
    print("greeter start")
    Logger("greeter")
    while (counter < 12):
        print(f"greeter number: {counter}")
        time.sleep(1)
        counter += 1

if __name__ == "__main__":
    main()