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
    print("responder start")
    Logger("responder")
    while (counter < 5):
        print(f"responder number: {counter}")
        time.sleep(3)
        counter += 1


if __name__ == "__main__":
    main()