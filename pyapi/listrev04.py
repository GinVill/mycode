#!/usr/bin/env python3

def main():
    #create a list already containing IP addresses as strings
    ipList = ['10.0.0.1', '10.0.1.1', '10.3.2.1']

    #create a list of ports as strings
    ipList2 = ['5060', '80', '22']

    #display list
    print(ipList)

    #use .append() on our list object, ipList, which will take
    #whatever we pass and add it to the list object
    ipList.append(ipList2)

    #display the changed list
    print(ipList)

    #like .extend(), .append() expects exactly one argurment

if __name__ == '__main__':
        main()

