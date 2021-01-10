#!/usr/bin/env python3

def main():
    #create a list containing IP addresses as strings
    ipList = ['10.0.0.1', '10.0.1.1', '10.3.2.1']

    #create a list of ports as strings
    ipList2 = ['5060', '80', '22']

    #display list
    print(ipList)

    #use .extend on ipList, our list object
    #.extend iterates over each "thing" passed and adds them to 
    # the list object
    ipList.extend(ipList2)

    #show how ipList had changed
    print(ipList)

if __name__ == '__main__':
    main()

