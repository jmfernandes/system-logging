#!/usr/bin/env python3

import time

def main():
    counter = 0
    print("responder start")
    while (counter < 5):
        print(f"responder number: {counter}")
        time.sleep(3)
        counter += 1


if __name__ == "__main__":
    main()