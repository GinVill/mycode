#!/usr/bin/env python3

def main():
    #create an empty list
    myEmptyList = []

    #add to the list with .extend, which adds item to list
    myEmptyList.extend('192.168.102.55')

    #display our list
    print(myEmptyList)

if __name__ == '__main__':
    main()

