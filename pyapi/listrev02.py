#!/usr/bin/env python3

def main():
    anotherEmptyList = []

    #This will throw an ERROR
    # because .extend expects exactly ONE argument
    anotherEmptyList.extend('10.0.0.1', 'retro game server')

    print(anotherEmptyList)

if __name__ == '__main__':
    main()

