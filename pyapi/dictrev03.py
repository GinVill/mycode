#!/usr/bin/env python3

def main():
    vendorDict = {'cisco': True, 'juniper': False, 'arista': True, 'netgear': True}
    custList = ['acme', 'globex corporation', 'soylent green', 'initech', 'umbrella corporation']

    # Display the current state of our dictionary
    print(vendorDict)

    # Display all of the dictionary methods
    # focus on those without underscores
    print(dir(dict))

    #use a few dictionary methods
    print(vendorDict.keys())
    print(vendorDict.values())
    print(vendorDict.get('juniper'))

    #remove the key:value pair for netgear
    vendorDict.pop('netgear')

    #display dictionary to verify 'netgear' is gone
    print(vendorDict.get('netgear'))

    #display all the list methods
    print(dir(list))
    
    # and use one of those methods
    custList.append('cyberdyne')

    #display list to verify change
    print(custList)

if __name__ == '__main__':
    main()

