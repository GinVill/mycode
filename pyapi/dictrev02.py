#!/usr/bin env python3

def main():
    firewallDict = {'sip':'5060', 'ssh':'22', 'http':'80'}

    #display the current state of our dictionary
    print(firewallDict)

    #add another entry to the dictionary
    # note that it maps to an INT, not a string
    firewallDict['https'] = 443

    #display the dctionary with the new entry
    print(firewallDict)

    #display some dictionary data
    print('The print statement can be passed multiple items, provided they are separated by commas')
    print("The port in use for HTTP Secure is:", firewallDict['https'])

    #this SHOULD fail, but won't because we use the .get method
    print("A safer way to recall that data is the use the .get method:", \
            firewallDict.get('razzledazzlerootbeer'))

    #use the .keys method to return a list of keys
    print(firewallDict.keys())

    #use the .vaues method to return a list of values
    print(firewallDict.values())

    #to remove a single key from the dictionary
    del firewallDict['sip']
    print(firewallDict)

if __name__ == '__main__':
    main()

