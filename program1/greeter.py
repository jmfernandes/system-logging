#!/usr/bin/env python3

import time

def main():
    counter = 0
    print("greeter start")
    while (counter < 12):
        print(f"greeter number: {counter}")
        time.sleep(1)
        counter += 1

if __name__ == "__main__":
    main()